import time 
import sqlalchemy as sa
import re
import subprocess


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
        
        
    def closeDatabase(self):
        self.conn.close()
        self.engine.dispose()
        
            
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


    def restart(self):
        self.storeData(pT=0,sT=0)
            
            
    def retrieveData(self):
        sql = sa.text('SELECT * FROM watch ORDER BY row')
        resultSet = self.conn.execute(sql)
        resultsDict = resultSet.mappings().all()
        pattern = (r"(\[{'row': 1,)( 'passedTime': )(0|\d+.\d+), ('startTime': )(0|\d+.\d+)}]")
        re_match = re.match(pattern,str(resultsDict))
        self.passedTime = float(re_match[3])
        self.startTime = float(re_match[5])
        return self.startTime
    
    
    def storeData(self,pT,sT):
        self.conn.execute(self.watch_table.update().where(self.watch_table.c.row == 1).values(passedTime = pT, startTime=sT))
        self.conn.commit()
        
        
class lap(stopWatch):
    def __init__(self, startTime):
        super().__init__(startTime)
        self.engine = sa.create_engine('sqlite:///time.db')
        self.conn = self.engine.connect()
        self.meta = sa.MetaData() 
        self.lap_table = sa.Table('lap', self.meta,
                     sa.Column('lapNum', sa.Integer,primary_key=True),
                     sa.Column('lapTime',sa.TEXT),
                    )
        self.lapNum: int = 0
        self.lapTime: str = 0
        self.lapList: list = []
    

    def dropLapTable(self):
        sql = sa.delete(self.lap_table)
        with self.engine.connect() as connection:
            result = connection.execute(sql)
            connection.commit()
        
    
    def getLapNum(self):
        return self.lapNum
    

    def getLapTime(self,lapNum):
        print(self.lapList[lapNum-1])
        print(self.lapList)
        return self.lapList[lapNum-1]
        

    def lapFunc(self,lapTime):
        self.lapNum += 1
        self.lapTime = lapTime
        self.lapList.append(self.lapTime)
        return self.lapList[self.lapNum-1]   
    

    def retrieveData(self):
        sql = sa.text('SELECT * FROM lap ORDER BY lapNum')
        resultSet = self.conn.execute(sql)
        resultsDict = resultSet.mappings().all()
        print(resultsDict)
        pattern = (r"{'lapNum': (\d), 'lapTime': '(\d{2}:\d{2}:\d{2})'}")
        for row in resultsDict:
            re_match = re.match(pattern=pattern,string=str(row))
            self.lapTime = (re_match[2])
            self.lapList.append(self.lapTime)
        self.lapNum = len(resultsDict)
        
        
    def storeLapData(self,lN,lT):
        sql = sa.insert(self.lap_table).values(lapNum=lN, lapTime=lT)
        with self.engine.connect() as connection:
            result = connection.execute(sql)
            connection.commit()
     

if __name__ == "__main__":
    
    timer = stopWatch(startTime=time.time())
    timer.storeData(pT=0,sT=0)
    subprocess.Popen(['python', "stopwatchGui.py"])