import threading
import time
import tkinter as tk
import os
import sys
import subprocess
class Timer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('850x300')
        self.root.title('Timer')

        width = 850
        height = 300

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)

        self.root.geometry(f'{width}x{height}+{int(x)}+{int(y)}')

        self.hours_label = tk.Label(self.root, font = ('Helvetica', 20), text = 'Hours:')
        self.hours_label.grid(row = 0, column = 0, padx = 5, pady = 5)
        self.hours_entry = tk.Entry(self.root, font = ('Helvetica', 20), width = 5)
        self.hours_entry.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.minutes_label = tk.Label(self.root, font=('Helvetica', 20), text = 'Minutes:')
        self.minutes_label.grid(row = 0, column = 2, padx = 5, pady = 5)
        self.minutes_entry = tk.Entry(self.root, font = ('Helvetica', 20), width = 5)
        self.minutes_entry.grid(row = 0, column = 3, padx = 5, pady = 5)

        self.seconds_label = tk.Label(self.root, font = ('Helvetica', 20), text = 'Seconds:')
        self.seconds_label.grid(row = 0, column = 4, padx = 5, pady = 5)
        self.seconds_entry = tk.Entry(self.root, font = ('Helvetica', 20), width = 5)
        self.seconds_entry.grid(row = 0, column = 5, padx = 5, pady = 5)

        self.start_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'Begin', command = self.start_thread)
        self.start_button.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)
        self.pause_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'Pause', command = self.pause)
        self.pause_button.grid(row = 1, column = 1, columnspan = 3, padx = 5, pady = 5)
        self.refresh_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'Refresh', command = self.refresh)
        self.refresh_button.grid(row = 1, column = 5, columnspan = 2, padx = 5, pady = 5)
        self.reset_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'Reset', command = self.reset)
        self.reset_button.grid(row = 1, column = 3, columnspan = 2, padx = 5, pady = 5)
        self.other_program_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'Menu', command = self.menu)
        self.other_program_button.grid(row = 2, column = 5, columnspan = 10, padx = 5, pady = 5)

        self.time_label = tk.Label(self.root, font = ('Helvetica', 30), text = 'Time: 00:00:00')
        self.time_label.grid(row = 2, column = 0, columnspan = 6, padx = 5, pady = 5)

        self.stop_loop = False
        self.seconds_remaining = 0
        self.paused = False
        self.root.mainloop()

    def start_thread(self):
        t = threading.Thread(target = self.start)
        t.start()

    def start(self):
        self.stop_loop = False
        try:
            hours = int(self.hours_entry.get()) if self.hours_entry.get() else 0
            minutes = int(self.minutes_entry.get()) if self.minutes_entry.get() else 0
            seconds = int(self.seconds_entry.get()) if self.seconds_entry.get() else 0
        except ValueError:
            print('Invalid input')
            return

        self.seconds_remaining = hours * 3600 + minutes * 60 + seconds
        self.countdown()

    def countdown(self):
        while self.seconds_remaining > 0 and not self.stop_loop:
            if not self.paused:
                self.seconds_remaining -= 1
                minutes, seconds = divmod(self.seconds_remaining, 60)
                hours, minutes = divmod(minutes, 60)
                self.time_label.config(text = f'Time: {hours:02d}:{minutes:02d}:{seconds:02d}')
                self.root.update()
                time.sleep(1)

    def pause(self):
        self.paused = not self.paused
        if self.paused:
            self.pause_button.config(text = 'Resume')
        else:
            self.pause_button.config(text = 'Pause')

    def refresh(self):
        self.stop_loop = True
        self.seconds_remaining = 0
        self.time_label.config(text = 'Time: 00:00:00')
        self.pause_button.config(text = 'Pause')
        self.root.destroy()
        os.execl(sys.executable, sys.executable, *sys.argv)

    def reset(self):
        self.stop_loop = True
        self.seconds_remaining = 0
        self.time_label.config(text = 'Time: 00:00:00')
        self.pause_button.config(text = 'Pause')

    def menu(self):
        subprocess.Popen(['python', "Menu.py"])
        self.root.destroy()
        
        

if __name__ == '__main__':
    Timer()

