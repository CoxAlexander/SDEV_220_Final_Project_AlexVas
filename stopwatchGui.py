import stopwatch as sw
import tkinter as tk
import time
import sqlalchemy as sa
import subprocess
class gui:
    stoped: bool = True
    paused: bool = True
    def __init__(self):
        self.lapNum:int = 0
        self.lapList = []
        self.timer = sw.stopWatch(startTime = time.time())
        self.pausedTimer = sw.stopWatch(startTime=time.time())
        self.lapTimer = sw.lap(startTime=time.time())
        self.timer.retrieveData()
        if self.timer.getStartTime() == 0:
            self.timer = sw.stopWatch(startTime = time.time())
        self.lapTimer.retrieveData()
        self.lapNum = self.lapTimer.getLapNum()
        self.height: int = 300 + (50*self.lapNum)
        self.length: int = 600
        self.root = tk.Tk()
        self.screenWidth = self.root.winfo_screenwidth()
        self.screenHeight = self.root.winfo_screenheight()
        x = (self.screenWidth/2) - (self.length/2)
        y = (self.screenHeight/2) - (self.height/2)
        self.root.geometry('%dx%d+%d+%d' % (self.length,self.height,x,y))
        self.root.title('StopWatch')
        self.time_label = tk.Label(self.root, font = ('Helvetica', 30), text =  self.timer.currentTime(time.time())) 
        self.time_label.grid(row = 0, column = 0, columnspan = 5, padx = 5, pady = 5)
        for x in range (1,self.lapNum+1):
            self.lapList.append(tk.Label(self.root, font=('Helvetica' ,20), text=f'lap {x}: {self.lapTimer.getLapTime(x)}')) #-1
            self.lapList[x-1].grid(row=(x),column = 0, columnspan = 5, padx = 10, pady = 5)        #-1
            
        self.start_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'Begin', command = self.start)
        self.start_button.grid(row = (self.lapNum+1), column = 0, padx = 10, pady = 5)
        self.stop_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'End', command = self.stop)
        self.stop_button.grid(row = (self.lapNum+1), column = 1,  padx = 10, pady = 5)
        self.pause_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'Pause', command = self.pause)
        self.pause_button.grid(row = (self.lapNum+1), column = 2,  padx = 0, pady = 5)
        self.lap_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'Lap', command = self.lap)
        self.lap_button.grid(row = (self.lapNum+1), column = 3,  padx = 10, pady = 5)
        self.other_program_button = tk.Button(self.root, font = ('Helvetica', 30), text = 'Menu', command = lambda: self.run_script('Menu.py'))
        self.other_program_button.grid(row = (self.lapNum+2), column = 1, columnspan = 10, padx = 5, pady = 5)
        self.root.mainloop()
        
    
    def countup(self):
        while not(gui.stop or gui.pause):
            self.timer.currentTime(time.time())
            self.time_label.config(text = self.timer.currentTime(time.time()))
            self.root.update()
            self.timer.storeData(pT=self.timer.getPassedTime(), sT=self.timer.getStartTime())
    
           
    def lap(self):
        if not(gui.stop or gui.pause):
            self.height: int = 300 + (50*self.lapNum)
            self.length: int = 600 
            #self.lapTimer = sw.lap(startTime=time.time())
            self.lapNum += 1
            lapTimestr = self.timer.currentTime(time.time())
            self.lapList.append(tk.Label(self.root, font=('Helvetica' ,20), text=f'lap {self.lapNum}: {lapTimestr}'))
            self.lapList[self.lapNum-1].grid(row=(self.lapNum),column = 0, columnspan = 5, padx = 10, pady = 5) #-1
            self.start_button.grid(row = (self.lapNum+1), column = 0, padx = 10, pady = 5)
            self.stop_button.grid(row = (self.lapNum+1), column = 1,  padx = 10, pady = 5)
            self.pause_button.grid(row = (self.lapNum+1), column = 2,  padx = 0, pady = 5)
            self.lap_button.grid(row = (self.lapNum+1), column = 3,  padx = 10, pady = 5)
            self.other_program_button.grid(row = (self.lapNum+2), column = 1, columnspan = 10, padx = 5, pady = 5)
            self.root.geometry(f'{self.length}x{self.height}')
            self.timer.storeData(pT=self.timer.getPassedTime(), sT=self.timer.getStartTime())
            self.lapTimer.storeLapData(lN=self.lapNum,lT=lapTimestr) 
            self.root.update()
        

    def pause(self):
        if not(gui.stop and gui.paused):
            if(gui.pause):
                
                gui.pause = False
                self.pausedTimer.pausedTime(currentTime=time.time())
                self.timer.pauseTime(pausedTime=self.pausedTimer.pausedTime(currentTime=time.time()))
                self.pause_button.config(text="Pause")
            else:
                self.pausedTimer = sw.stopWatch(startTime=time.time())
                self.pause_button.config(text="Resume")
                gui.pause = True
            self.timer.storeData(pT=self.timer.getPassedTime(), sT=self.timer.getStartTime())
            self.countup()
  
  
    def run_script(self,script_name):
        subprocess.Popen(['python', script_name])
        self.root.destroy()      
        
        
    def start(self):
        
        if self.timer.retrieveData() == 0:
            self.timer = sw.stopWatch(startTime = time.time())
        gui.stop = False
        gui.pause = False
        self.countup()
        
    
    def stop(self):
        if not gui.stop:
            gui.stop = True
            gui.pause = True
            self.pause_button.config(text = "Pause")
            self.time_label.config(text = "00:00:00")
            for x in range(0,len(self.lapList)):
                self.lapList[x].destroy()
            self.lapNum = 0
            self.lapList = [] 
            self.height: int = 300 + (50 * self.lapNum)
            self.length: int = 600
            self.root.geometry(f'{self.length}x{self.height}')
            self.lapTimer.dropLapTable()
            self.run_script("stopwatch.py")
            self.root.update()
            
        
if __name__ == "__main__":
    gui()