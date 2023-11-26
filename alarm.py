import datetime
import tkinter as tk
from playsound import playsound
import threading
import time

class AlarmApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")

        # Variables
        self.alarm_time_var = tk.StringVar()
        self.alarm_time_var.set("00:00")

        # GUI Components
        self.label = tk.Label(root, text="Set Alarm Time (HH:MM):")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, textvariable=self.alarm_time_var, font=("Helvetica", 24))
        self.entry.pack(pady=20)

        self.set_button = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Alarm", command=self.stop_alarm, state=tk.DISABLED)
        self.stop_button.pack(pady=10)

    def set_alarm(self):
        alarm_time_str = self.alarm_time_var.get()
        try:
            alarm_time = datetime.datetime.strptime(alarm_time_str, "%H:%M")
            current_time = datetime.datetime.now()
            if alarm_time < current_time:
                # If the alarm time is in the past, set it for the next day
                alarm_time = alarm_time.replace(day=current_time.day + 1)
        except ValueError:
            tk.messagebox.showerror("Error", "Invalid time format. Please use HH:MM.")
            return

        alarm_thread = threading.Thread(target=self.alarm_thread, args=(alarm_time,))
        alarm_thread.start()

    def alarm_thread(self, alarm_time):
        current_time = datetime.datetime.now()

        while current_time < alarm_time:
            time.sleep(1)
            current_time = datetime.datetime.now()

        self.play_alarm()
        self.stop_button["state"] = tk.NORMAL

    def play_alarm(self):
        alarm_file = "ali.mp3"  # Replace with the path to your alarm sound file
        playsound(alarm_file)

    def stop_alarm(self):
        self.stop_button["state"] = tk.DISABLED

# Main Program
if __name__ == "__main__":
    root = tk.Tk()
    app = AlarmApp(root)
    root.mainloop()
