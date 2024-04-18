import tkinter as tk
import time
import random
import winsound

class TimerApp:
    def __init__(self, master):
        self.master = master
        master.title("Timer")

        self.min_label = tk.Label(master, text="Mindestdauer (Minuten):")
        self.min_label.pack()

        self.min_entry = tk.Entry(master)
        self.min_entry.pack()

        self.max_label = tk.Label(master, text="Maximaldauer (Minuten):")
        self.max_label.pack()

        self.max_entry = tk.Entry(master)
        self.max_entry.pack()

        self.start_button = tk.Button(master, text="Start", command=self.start_timer)
        self.start_button.pack()

        self.stop_button = tk.Button(master, text="Stop", command=self.stop_timer)
        self.stop_button.pack()
        self.stop_button.config(state=tk.DISABLED)  # Deaktiviert, bis der Timer gestartet wird

        self.time_label = tk.Label(master, text="")
        self.time_label.pack()

        self.running = False
        self.start_time = None

    def start_timer(self):
        if not self.running:
            self.running = True
            self.start_time = time.time()
            self.stop_button.config(state=tk.NORMAL)  # Aktiviert den Stop-Button
            self.start_button.config(state=tk.DISABLED)  # Deaktiviert den Start-Button

            try:
                min_minutes = int(self.min_entry.get())
                max_minutes = int(self.max_entry.get())
            except ValueError:
                min_minutes = 0
                max_minutes = 0

            min_seconds = min_minutes * 60
            max_seconds = max_minutes * 60
            wait_time = random.randint(min_seconds, max_seconds)

            self.master.after(wait_time * 1000, self.end_timer)

            self.update_time()

    def end_timer(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)  # Aktiviert den Start-Button
        self.stop_button.config(state=tk.DISABLED)  # Deaktiviert den Stop-Button
        winsound.Beep(1000, 1000)  # Spielt einen Alarmklang ab

    def stop_timer(self):
        self.running = False
        self.start_button.config(state=tk.NORMAL)  # Aktiviert den Start-Button
        self.stop_button.config(state=tk.DISABLED)  # Deaktiviert den Stop-Button

    def update_time(self):
        if self.running:
            elapsed_time = time.time() - self.start_time
            minutes = int(elapsed_time / 60)
            seconds = int(elapsed_time % 60)
            self.time_label.config(text=f"Vergangene Zeit: {minutes} Minuten und {seconds} Sekunden")
            self.master.after(1000, self.update_time)  # Aktualisiert die Anzeige jede Sekunde

def main():
    root = tk.Tk()
    app = TimerApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()