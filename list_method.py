a=[1,4,6,7,8,6]
a.append([10,12])
print(a)
#a.clear()
b=a.copy()
print(b)
b.clear()
print(a.count(6))
a.extend("kamal")
print(a)
print(a.index(6,3))#(element,start,end)
a.insert(0, [0,1,5])
print(a)
a.pop(0)
print(a)
a.remove(6)
print(a)
#a.reverse()
#print(a)
#a.sort(reverse=True)
print(a)
