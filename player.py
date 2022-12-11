import json






class Player:
    def __init__(self,name,point = 0):
       self.name =name
       self.point= point

    def point_show(self):
        return print(f"{self.name} point is {self.point}")
    @classmethod    
    def update_json(self,filename="scores.json"):
        with open(filename) as f:
            data1 = json.load(f)
            temp = data1["names"]
            y ={"firstname": self.name,"score":self.point}
            temp.append(y)
    @classmethod       
    def write_json(self,data,filename="scores.json"):
        with open(filename,"w") as f:
            json.dump(data,f,indent=4)    

            