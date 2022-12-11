
def update(list,dic):
   return list.append(dic)


dic={}
list =[]
dic['name'] ='serter'
dic['age'] = 36
update(list,dic)
print(dic)
print(list)
dic['name'] ='mehmet'
list.append(dic)
print(list)