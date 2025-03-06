import stopwatch as sw
import tkinter as tk
import time

class gui:
    stop: bool = True
    paused: bool = False
    def __init__(self):
        self.lapNum:int = 0
        self.height: int = 200 + (50*self.lapNum)
        self.length: int = 600
        self.lapList = [] 
        self.timer = sw.stopWatch(startTime = time.time())
        self.pausedTimer = sw.stopWatch(startTime=time.time())
        self.root = tk.Tk()
        self.screenWidth = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()
        x = (self.screenWidth/2) - (self.length/2)
        y = (self.screenHeight/2) - (self.height/2)
        self.root.geometry('%dx%d+%d+%d' % (self.length,self.height,x,y))
        self.root.title('StopWatch')
        self.time_label = tk.Label(self.root, font = ('Helvetica', 30), text =  "00:00:00") 
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
           self.timer.storeData(pT=self.timer.getPassedTime(), sT=self.timer.getStartTime)
    
           
    def lap(self):
        self.height: int = 300 + (50*self.lapNum)
        self.length: int = 600 
        self.lapTime = sw.lap(startTime=time.time())
        self.lapNum +=1
        self.lapList.append(tk.Label(self.root, font=('Helvetica' ,20), text=f'lap {self.lapNum}: {self.lapTime.lapFunc(self.timer.currentTime(time.time()))}'))
        self.lapList[self.lapNum-1].grid(row=(self.lapNum),column = 0, columnspan = 5, padx = 10, pady = 5)
        self.start_button.grid(row = (self.lapNum+1), column = 0, padx = 10, pady = 5)
        self.stop_button.grid(row = (self.lapNum+1), column = 1,  padx = 10, pady = 5)
        self.pause_button.grid(row = (self.lapNum+1), column = 2,  padx = 0, pady = 5)
        self.lap_button.grid(row = (self.lapNum+1), column = 3,  padx = 10, pady = 5)
        self.root.geometry(f'{self.length}x{self.height}')
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
        for x in range(0,len(self.lapList)):
            self.lapList[x].destroy()
        self.lapNum = 0
        self.lapList = [] 
        self.timer = sw.stopWatch(startTime=time.time())
        self.height: int = 200 + (50*self.lapNum)
        self.length: int = 600
        self.root.geometry(f'{self.length}x{self.height}')
        self.root.update()
        
        
        
if __name__ == "__main__":
    gui()