import time 
class stopWatch:
    def __init__(self, startTime):
        self.startTime = startTime
    def currentTime(self,currentTime):
        timepassedsec = currentTime-self.startTime
        timepassed = time.strftime("%H:%M:%S",time.gmtime(timepassedsec))
        return timepassed
timer = stopWatch(startTime=time.time())
counter = 0
while counter in range(0,100):
    print(timer.currentTime(currentTime=time.time()))
    time.sleep(1)
    counter += 1
