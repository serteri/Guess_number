import json






class Player:
    def __init__(self,name,point = 0):
       self.name =name
       self.point= point

    def point_show(self):
        return print(f"{self.name} point is {self.point}")
    @classmethod    
    def update_json(self,filename="scores.json",scores={}):
         with open(filename) as json_file:
               data1 = json.load(filename)
               temp = data1
               y = {"firstname":scores["firstname"] , "score": scores["score"]}
               temp.append(y)
         with open (filename,"w") as f:
               json.dump(data1,f)      

   
            