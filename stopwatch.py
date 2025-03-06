import time 
import sqlalchemy as sa 
class stopWatch:
    
    
    def __init__(self, startTime):
        self.engine = sa.create_engine('sqlite:///time.db')
        self.conn = self.engine.connect()
        self.meta = sa.MetaData() 
    
        self.watch_table = sa.Table('watch', self.meta,
                     sa.Column('row', sa.Integer,primary_key=True),
                     sa.Column('passedTime',sa.REAL),
                     sa.Column('startTime',sa.REAL)
                    )

        self.elaspedTime: float = 0
        self.startTime: float = startTime
        self.passedTime: float = 0 
        
        
    def currentTime(self,currentTime: float):
        self.elaspedTime =  ((currentTime - self.startTime) - self.passedTime)
        self.elaspedTimeFormat: tuple = time.strftime("%H:%M:%S",time.gmtime(self.elaspedTime))
        return (self.elaspedTimeFormat)
    
    
    def getPassedTime(self):
        return (self.passedTime)  
    
    
    def getStartTime(self):
        return (self.startTime)  
    
        
    def pauseTime(self, pausedTime:float):
        self.passedTime += pausedTime
        return(self.elaspedTimeFormat)


    def pausedTime(self,currentTime:float):
        pausedTime = currentTime - self.startTime
        return (pausedTime)

        
    def retrieveData(self):
        pass


    def storeData(self,pT,sT):
       self.conn.execute(self.watch_table.update().where(self.watch_table.c.row == 1).values(passedTime = pT, startTime=sT))

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
    
    def retrieveData(self):
        pass

    def storeData(self):
        pass
    
    
if __name__ == "__main__":
    timer = stopWatch(startTime=time.time())
    timer.meta.create_all(timer.engine)
    counter = 0
    while counter <= 10:
        #1741239562.36468
        print(timer.currentTime(time.time()))
        counter += 1
        time.sleep(1)
    timer.storeData(pT=timer.getPassedTime(), sT=timer.getStartTime())
    timer.conn.commit()
    timer.conn.close()