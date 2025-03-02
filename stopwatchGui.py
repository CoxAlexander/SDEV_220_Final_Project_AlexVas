import stopwatch as sw
import tkinter as tk
import time

class gui:
    stop: bool = True
    paused: bool = False
    def __init__(self):
        self.lapNum:int = 0
        height: int = 300 + (50*self.lapNum)
        length: int = 600 
        self.timer = sw.stopWatch(startTime = time.time())
        self.pausedTimer = sw.stopWatch(startTime=time.time())
        self.root = tk.Tk()
        self.root.geometry(f'{length}x{height}')
        self.root.title('StopWatch')
        self.time_label = tk.Label(self.root, font = ('Helvetica', 30), text =  "00:00:00") #self.timer.currentTime(time.time()))
        self.time_label.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)        
        self.start_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'Begin', command = self.start)
        self.start_button.grid(row = (self.lapNum+1), column = 0, padx = 10, pady = 5)
        self.stop_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'End', command = self.stop)
        self.stop_button.grid(row = (self.lapNum+1), column = 1,  padx = 10, pady = 5)
        self.pause_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'Pause', command = self.pause)
        self.pause_button.grid(row = (self.lapNum+1), column = 2,  padx = 0, pady = 5)
        self.lap_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'Lap', command = self.lap)
        self.lap_button.grid(row = (self.lapNum+1), column = 3,  padx = 10, pady = 5)
        self.root.mainloop()
    
    
    def countup(self):
        while not(gui.stop and gui.pause):
           self.timer.currentTime(time.time())
           self.time_label.config(text = self.timer.currentTime(time.time()))
           self.root.update()
    
           
    def lap(self):
        self.lapNum +=1
        self.lap_label = tk.Label(self.root, font=('Helvetica' ,30), text=self.timer.lapTime[self.lap])
        self.lap_label.grid(row=self.lap,column = 0, padx = 10, pady = 5)
        self.root.update()
    
               
    def pause(self):
        if(gui.pause):
            gui.stop = False
            gui.pause = False
            self.pausedTimer.pausedTime(currentTime=time.time())
            self.timer.pauseTime(pausedTime=self.pausedTimer.pausedTime(currentTime=time.time()))
            self.pause_button.config(text="Pause")
            
            
        else:
            self.pausedTimer = sw.stopWatch(startTime=time.time())
            self.pause_button.config(text="Resume")
            gui.pause = True
            gui.stop = True
        self.countup()
        
    def start(self):
        gui.stop = False
        gui.pause = False
        self.timer = sw.stopWatch(startTime = time.time())
        self.countup()
        
        
    def stop(self):
        gui.stop = True
        gui.pause = True
        self.pause_button.config(text = "Pause")
        self.time_label.config(text = "00:00:00")
        self.timer = sw.stopWatch(startTime=time.time())
        
        
        
if __name__ == "__main__":
    gui()