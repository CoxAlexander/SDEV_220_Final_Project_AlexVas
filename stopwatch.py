import time 
class stopWatch:
    def __init__(self, startTime):
        self.startTime = startTime
    def currentTime(self,currentTime):
        timepassed = currentTime-self.startTime
        return timepassed
timer = stopWatch(startTime=time.time())
time.sleep(10)
print(timer.currentTime(currentTime=time.time()))

    
