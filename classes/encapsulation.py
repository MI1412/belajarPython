class DataRepository:
   def __init__(self):
       self.data = []
 
   def setData(self,*response):
       self.data.append(response)
       
 
   def getData(self):
       print(self.data)

data = DataRepository()
data.setData(True,False)
data.getData()