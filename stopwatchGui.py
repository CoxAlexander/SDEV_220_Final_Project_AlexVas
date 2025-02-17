import stopwatch 
import tkinter as tk
import time

class gui:
    stop = True
    def __init__(self):
        self.timer = stopwatch.stopWatch(startTime=time.time())
        self.root = tk.Tk()
        self.root.geometry('500x250')
        self.root.title('Timer')
        self.time_label = tk.Label(self.root, font = ('Helvetica', 30), text = self.timer.currentTime(time.time()))
        self.time_label.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)        
        self.start_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'Begin', command = self.start)
        self.start_button.grid(row = 1, column = 0, columnspan = 2, padx = 5, pady = 5)
        self.stop_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'End', command = self.stop)
        self.stop_button.grid(row = 1, column = 2, columnspan = 2, padx = 5, pady = 5)
        self.root.mainloop()
    
    
    def countup(self):
        while not(gui.stop):
           self.timer.currentTime(time.time())
           self.time_label.config(text=self.timer.currentTime(time.time()))
           self.root.update()
    
           
    def start(self):
        gui.stop = False
        self.timer = stopwatch.stopWatch(startTime=time.time())
        self.countup()
    
        
    def stop(self):
        gui.stop = True
        self.time_label.config(text="00:00:00")
        self.timer = stopwatch.stopWatch(startTime=time.time())
        self.countup()
    
        
if __name__ == "__main__":
    gui()