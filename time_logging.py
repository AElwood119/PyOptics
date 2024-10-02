import csv
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox

# Predefined activities
activities = [
    "Writing Code",
    "Documentation",
    "Github Page",
    "Planning",
    "Testing and Debugging",
    "Research",
]


def log_time():
    date = datetime.now().strftime("%Y-%m-%d")
    start_time = start_time_entry.get()
    end_time = end_time_entry.get()
    activity = activity_combobox.get()
    comment = comment_text.get("1.0", tk.END).strip()  # Get text from Text widget

    # Calculate total time spent
    try:
        start = datetime.strptime(start_time, "%H:%M")
        end = datetime.strptime(end_time, "%H:%M")
        total_time = (end - start).seconds / 3600  # Convert to hours

        # Log to CSV
        with open("time_log.csv", mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([date, start_time, end_time, total_time, activity, comment])

        messagebox.showinfo("Success", "Time logged successfully!")
        start_time_entry.delete(0, tk.END)
        end_time_entry.delete(0, tk.END)
        activity_combobox.set("")
        comment_text.delete("1.0", tk.END)  # Clear the Text widget

    except ValueError:
        messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")


# Set up the GUI
root = tk.Tk()
root.title("Time Logger for PyOptics Project")

# Start time label and entry
tk.Label(root, text="Start Time (HH:MM):").grid(row=0, column=0, padx=10, pady=10)
start_time_entry = tk.Entry(root)
start_time_entry.grid(row=0, column=1, padx=10, pady=10)

# End time label and entry
tk.Label(root, text="End Time (HH:MM):").grid(row=1, column=0, padx=10, pady=10)
end_time_entry = tk.Entry(root)
end_time_entry.grid(row=1, column=1, padx=10, pady=10)

# Activity selection
tk.Label(root, text="Select Activity:").grid(row=2, column=0, padx=10, pady=10)
activity_combobox = ttk.Combobox(root, values=activities)
activity_combobox.grid(row=2, column=1, padx=10, pady=10)

# Comment label and Text widget for larger input
tk.Label(root, text="Comment:").grid(row=3, column=0, padx=10, pady=10)
comment_text = tk.Text(root, height=4, width=40)  # Set height and width
comment_text.grid(row=3, column=1, padx=10, pady=10)

# Log button
log_button = tk.Button(root, text="Log Time", command=log_time)
log_button.grid(row=4, column=0, columnspan=2, pady=20)

# Start the GUI event loop
root.mainloop()
