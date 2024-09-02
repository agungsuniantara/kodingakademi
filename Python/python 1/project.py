data = [10,100,20,30,60] 
# data.sort()
# print(data)

urut = [] 

for i in range(len(data)): 
    kecil = min(data) 
    urut.append(kecil)
    data.remove(kecil)

print(urut)
