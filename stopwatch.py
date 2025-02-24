import time 
class stopWatch:
    def __init__(self, startTime):
        self.lap = 0
        self.elaspedTime = 0
        self.startTime = startTime
        
    def currentTime(self,currentTime):
        timepassedsec = currentTime-self.startTime
        self.elaspedTime += timepassedsec
        elaspedTimeFormat = time.strftime("%H:%M:%S",time.gmtime(self.elaspedTime))
        return elaspedTimeFormat
    
    def pauseTime(self,currentTime):
        timepassedsec = currentTime - self.startTime
        self.elaspedTime += timepassedsec
        elaspedTimeFormat = time.strftime("%H:%M:%S",time.gmtime(self.elaspedTime))
        self.startTime = currentTime
        return(elaspedTimeFormat)

    
    
if __name__ == "__main__":
    timer = stopWatch(startTime=time.time())
    time.sleep(10)
    print(timer.currentTime(time.time()))
