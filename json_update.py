import json

def json_update(filename,scores1):
     
      with open("scores.json") as json_file:
               data1 = json.load(json_file)
               temp = data1
               y = {"firstname":scores1["firstname"] , "score": scores1["score"]}
               temp.append(y)
      with open (filename,"w") as f:
               json.dump(data1,f)      
