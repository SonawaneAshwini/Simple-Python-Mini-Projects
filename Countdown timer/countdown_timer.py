import tkinter as tk
from tkinter import messagebox
import time

def start_countdown():
    try:
        total_seconds = int(entry_time.get())

        if total_seconds < 0:
            messagebox.showerror("Error", "Please enter a positive integer")
            return


        while total_seconds > 0:
            mins, secs = divmod(total_seconds, 60)
            time_format = '{:02d}:{:02d}'.format(mins, secs)
            label_time.config(text=time_format)
            root.update()
            time.sleep(1)
            total_seconds -= 1

        label_time.config(text="Time's up!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid integer")

root = tk.Tk()
root.title("Countdown Timer")


label_prompt = tk.Label(root, text="Enter time in seconds:")
label_prompt.pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack(pady=5)


label_time = tk.Label(root, text="00:00", font=("Helvetica", 48))
label_time.pack(pady=20)

button_start = tk.Button(root, text="Start", command=start_countdown)
button_start.pack(pady=5)

root.mainloop()
