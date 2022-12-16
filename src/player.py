import json

class Player:
    def __init__(self,name,point = 0):
       self.name =name
       self.point= point

    def point_show(self):
        return print(f"{self.name} point is {self.point}")
     

   
            