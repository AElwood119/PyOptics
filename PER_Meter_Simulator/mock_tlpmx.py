# mock_tlpmx.py
import random
from ctypes import c_double

TLPM_DEFAULT_CHANNEL = 1


class MockTLPMX:
    def __init__(self):
        self.devices = [
            b"USB0::0x1234::0x5678::PM100123::INSTR",
            b"USB0::0x1234::0x5678::PM100456::INSTR",
        ]
        self.connected = False

    def findRsrc(self, device_count_ptr):
        # This works with byref(c_uint32()) from the GUI
        device_count_ptr[0] = len(self.devices)

    def getRsrcName(self, index, buffer):
        if index.value < len(self.devices):
            buffer.raw = self.devices[index.value].ljust(1024, b"\x00")
        else:
            raise IndexError("Device index out of range")

    def open(self, resource_name, ID_query, reset_device):
        self.connected = True
        self.selected_device = resource_name.value.decode()

    def getCalibrationMsg(self, message_buffer, channel):
        message_buffer.raw = b"Calibrated: 2024-01-01".ljust(1024, b"\x00")

    def measPower(self, power_ptr, channel):
        power_ptr[0] = random.uniform(0.0, 5.0)

    def close(self):
        self.connected = False
