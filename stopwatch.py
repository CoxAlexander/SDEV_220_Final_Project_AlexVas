import time 
class stopWatch:
    def __init__(self, startTime):
        self.elaspedTime: float = 0
        self.startTime: float = startTime
        self.passedTime: float = 0
        
        
    def currentTime(self,currentTime: float):
        self.elaspedTime =  ((currentTime - self.startTime) - self.passedTime)
        self.elaspedTimeFormat: tuple = time.strftime("%H:%M:%S",time.gmtime(self.elaspedTime))
        return (self.elaspedTimeFormat)
        
        
    def pauseTime(self, pausedTime:float):
        self.passedTime += pausedTime
        return(self.elaspedTimeFormat)


    def pausedTime(self,currentTime:float):
        pausedTime = currentTime - self.startTime
        return pausedTime
        


class lap(stopWatch):
    def __init__(self, startTime):
        super().__init__(startTime)
        self.lapNum: int = 0
        self.lapTime: int = 0
        self.lapList: list = []
        
    def lapFunc(self,lapTime):
        self.lapNum += 1
        self.lapTime = lapTime
        self.lapList.append(self.lapTime)
        print(self.lapList[self.lapNum-1])
        return self.lapList[self.lapNum-1]   
        
if __name__ == "__main__":
    timer = stopWatch(startTime=time.time())
    counter = 0
    while counter <= 90:
        print(timer.currentTime(time.time()))
        counter += 1
        time.sleep(1)