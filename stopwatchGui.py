import stopwatch as sw
import tkinter as tk
import time

class gui:
    stop = True
    paused = False
    pause_count = 0
    def __init__(self):
        self.timer = sw.stopWatch(startTime=time.time())
        self.root = tk.Tk()
        self.root.geometry('500x250')
        self.root.title('Timer')
        self.time_label = tk.Label(self.root, font = ('Helvetica', 30), text = self.timer.currentTime(time.time()))
        self.time_label.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)        
        self.start_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'Begin', command = self.start)
        self.start_button.grid(row = 1, column = 0, padx = 10, pady = 5)
        self.stop_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'End', command = self.stop)
        self.stop_button.grid(row = 1, column = 1,  padx = 10, pady = 5)
        self.pause_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'Pause', command = self.pause)
        self.pause_button.grid(row = 1, column = 2,  padx = 10, pady = 5)
        self.root.mainloop()
    
    
    def countup(self):
        while not(gui.stop and gui.pause):
           self.time_label.config(text=self.timer.currentTime(time.time()))
           self.timer.currentTime(time.time())
           self.root.update()
           
    def pause(self):
        self.pause_count += 1
        if  (gui.pause):
            self.timer.pauseTime(time.time())
            self.time_label.config(text=self.timer.pauseTime(time.time()))
            self.pause_button.config(text="Pause")
            gui.pause = False
        else:
            self.pause_button.config(text="Unpause")
            gui.pause = True
            gui.stop = True
        self.countup()
           
    def start(self):
        gui.stop = False
        gui.pause = False
        self.countup()
        
    def stop(self):
        gui.stop = True
        gui.pause = True
        self.pause_button.config(text="Pause")
        self.time_label.config(text="00:00:00")
        self.timer = sw.stopWatch(startTime=time.time())
        self.countup()
        
if __name__ == "__main__":
    gui()