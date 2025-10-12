# power_meter_gui.py
import tkinter as tk
from tkinter import ttk, messagebox
from ctypes import (
    create_string_buffer,
    byref,
    c_uint32,
    c_int,
    c_char_p,
    c_bool,
    c_double,
)

from mock_tlpmx import MockTLPMX as TLPMX, TLPM_DEFAULT_CHANNEL


class PowerMeterGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Power Meter Emulator")
        self.geometry("400x300")

        self.tlPM = TLPMX()
        self.connected = False

        self.device_list = self.find_devices()

        self.device_var = tk.StringVar()
        self.result_var = tk.StringVar()

        ttk.Label(self, text="Select Power Meter:").pack(pady=5)
        self.device_combo = ttk.Combobox(
            self, values=self.device_list, textvariable=self.device_var
        )
        self.device_combo.pack(pady=5)

        ttk.Button(self, text="Connect", command=self.connect).pack(pady=10)
        ttk.Button(self, text="Measure Power", command=self.measure_power).pack(pady=10)

        self.result_label = ttk.Label(
            self, textvariable=self.result_var, font=("Helvetica", 14)
        )
        self.result_label.pack(pady=20)

    def find_devices(self):
        from ctypes import pointer

        device_count = c_uint32()
        device_count_ptr = pointer(device_count)
        self.tlPM.findRsrc(device_count_ptr)
        devices = []
        resource_name = create_string_buffer(1024)

        for i in range(device_count.value):
            self.tlPM.getRsrcName(c_int(i), resource_name)
            name = c_char_p(resource_name.raw).value.decode()
            devices.append(name)
        return devices

    def connect(self):
        name = self.device_var.get()
        if not name:
            messagebox.showwarning("No Device", "Please select a device.")
            return
        resource = create_string_buffer(name.encode())
        self.tlPM.open(resource, c_bool(True), c_bool(True))
        self.connected = True
        messagebox.showinfo("Connected", f"Connected to {name}")

    def measure_power(self):
        if not self.connected:
            messagebox.showwarning(
                "Not Connected", "Please connect to a power meter first."
            )
            return
        power = c_double()
        self.tlPM.measPower(byref(power), TLPM_DEFAULT_CHANNEL)
        self.result_var.set(f"Power: {power.value:.3f} W")


if __name__ == "__main__":
    app = PowerMeterGUI()
    app.mainloop()
