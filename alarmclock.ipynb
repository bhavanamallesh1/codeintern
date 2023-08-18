import tkinter as tk
import time
import winsound
from threading import Thread

class AlarmClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Alarm Clock")

        self.label = tk.Label(root, text="Enter alarm time (HH:MM:SS):")
        self.label.pack()

        self.entry = tk.Entry(root)
        self.entry.pack()

        self.set_button = tk.Button(root, text="Set Alarm", command=self.set_alarm)
        self.set_button.pack()

        self.stop_button = tk.Button(root, text="Stop Alarm", command=self.stop_alarm, state=tk.DISABLED)
        self.stop_button.pack()

        self.alarm_time = None
        self.alarm_thread = None
        self.running = False

    def set_alarm(self):
        alarm_time_str = self.entry.get()
        try:
            self.alarm_time = time.strptime(alarm_time_str, "%H:%M:%S")
        except ValueError:
            self.label.config(text="Invalid time format. Please use HH:MM:SS format.")
            return

        self.label.config(text=f"Alarm set for {alarm_time_str}")
        self.set_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)

        self.running = True
        self.alarm_thread = Thread(target=self.check_alarm)
        self.alarm_thread.start()

    def check_alarm(self):
        while self.running:
            current_time = time.localtime()
            if self.alarm_time.tm_hour == current_time.tm_hour and \
               self.alarm_time.tm_min == current_time.tm_min and \
               self.alarm_time.tm_sec == current_time.tm_sec:
                self.trigger_alarm()
                self.running = False
            time.sleep(1)

    def trigger_alarm(self):
        winsound.Beep(1000, 1000)  # Beep for 1 second

    def stop_alarm(self):
        self.running = False
        self.label.config(text="Alarm stopped.")
        self.set_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)

def main():
    root = tk.Tk()
    app = AlarmClockApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
