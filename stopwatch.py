import time 
class stopWatch:
    def __init__(self, startTime):
        self.lapNum: int = 1
        self.lapTime: int = 0
        self.lap: dict = {self.lapNum : self.lapTime}
        self.elaspedTime: float = 0
        self.startTime: float = startTime
        self.passedTime: float = 0
        
        
    def currentTime(self,currentTime: float):
        self.elaspedTime =  ((currentTime - self.startTime) - self.passedTime)
        self.elaspedTimeFormat: tuple = time.strftime("%H:%M:%S",time.gmtime(self.elaspedTime))
        return (self.elaspedTimeFormat)
    
    def lap(self):
        self.lapNum += 1
        self.lapTime = self.currentTime()
        self.lap[self.lapNum] = self.lapTime
        
        
    def pauseTime(self, pausedTime:float):
        self.passedTime += pausedTime
        return(self.elaspedTimeFormat)


    def pausedTime(self,currentTime:float):
        pausedTime = currentTime - self.startTime
        return pausedTime
        


        
        
if __name__ == "__main__":
    timer = stopWatch(startTime=time.time())
    counter = 0
    while counter <= 90:
        print(timer.currentTime(time.time()))
        counter += 1
        time.sleep(1)