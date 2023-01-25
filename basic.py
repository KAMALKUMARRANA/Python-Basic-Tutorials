a=10
b=10
c="string"
d="string"
e=True
f=False
print(id(a),id(b))
print(id(c),id(d))
print(id(e),id(f))

# Arithmetic op-------------------------> + - * / % // **
# Assignment-----------------------> = += -=
# Comparision Op--------------------------> == != > < >= <=
# Logical ----------------------------> and or not 
# Bitwise op------------------------------>& | ^(XOR)  it perform binary bits

# in - membership operators
str1="Hello"
print('H' in str1)
l=[2,5,68,9]
print(5 not in l)


#identify operator-----------------------------> is(==), is not(!=)
x=10
y=10
print(x is y,x==y)
print(x is not y,x!=y)


x=10
y=8
print(bin(x)) 
print(bin(y))

print(x|y,bin(x|y))
print(x&y,bin(x&y))
print(x^y,bin(x^y))
# 0b1010
# 0b1000
# 10 0b1010
# 8 0b1000
# 2 0b10


# Mutable--------------------->
# list
# Dictionary
# byte array

# Immutable-------------------->
# int
# float
# complex
#  bool
# string
# tuple
# set

a=2+5j
print(type(a))

s="hi"
s2='''jdjj
hjhjhjc
kjkjkcj
'''
print(len(s))

# print(s2,type(s2))
# a=eval(input("1st: "))
# b=eval(input("2nd: "))
# print(a+b)

a=10
if a%2==0:
    print("Even")
else:
    print("Odd")

for i in range(1,11,2):
    print(i)
    
    
print(range(5))# (0 to 4)

for i in range(10,0,-1): # reverse
    print(i)
    
i=1    
while i<=10:
    print(i)
    i+=1
    
print(i) #---> 11

i=10
while i>=1:
    print(i)
    i=i-1
print(i)


# string----------------------------------------------->
s="hi"
s2='''jdjj
hjhjhjc
kjkjkcj
'''

print(s,s2)

w="Welcome to Kamal World!"
print(w[6])
print(w[-1])
print(w[8])

# Slicing------------------------------------------------------------------------->
w="Welcome to Kamal World!"
print(w[0:7])
print(w[0::2])
print(w[-1::-2])
print(w[-1:-10:-2])
print(w[-1::-1])
print(w[::-1])
print(w[::-2])
print(w[0::2])

w="Welcome to KamalWorld!"
print(w[-1::-1])
print(len(w))
for i in range(len(w)):
    print(w[i],end=" ")
print()
for j in range(len(w)-1,-1,-1):
    print(w[j],end=" ")

for i in w:
    print(i,end=" ")
print()

w="welcome to KamalWorld!"
print(w.lower())
print(w)
print(w.upper())
print(w.title())
print(w.capitalize())

w="Welcome"
n="123456hdg "
print(w.find('e',2)) # 2 is start index ,if not available return -1
print(w.index('c',3)) # 3, occurred run time error

print(w.isalpha())
print(n.isdigit())
print(w.isalnum())
print(n.isalnum())



# chr()- ASCII value  and ord() function---------------------------------------------->
a=65
print(chr(a))

h='a'
print(ord(h))


w="welcome {} to {} KamalWorld!".format("Hello",20);
print(w)

w="welcome {1} to {0} KamalWorld!".format("Hello",20);
print(w)



w="welcome {a:^10} to {b} KamalWorld!".format(a="Hello",b=20);
print(w)

w="welcome {a:>10} to {b} KamalWorld!".format(a="Hello",b=20);
print(w)

w="welcome {a:<10} to {b:^8} KamalWorld!".format(a="Hello",b=20);
print(w)


# List-------------------------------------->
l=[1,3,4,"hello",[12,56,"hi"]]
print(type(l))
print(l[4][2])

print(l[-2])
print(l[-1][-3])

# slicing--------------->
print(l[0:2])
print(l[1:])

print(l[0::2]) # gap 1 
print(l[-1::-1])

# Iteration------------>
l=[10,20,30,40,50,60]
for i in range(len(l)-1,-1,-1):
	print(l[i],end=" ")
 
print()
for i in l:
	print(i)


l=[]
for i in range(1,101):
    l.append(i)
print(l)
print(s)
# List comprehension------------------------>
n=[m for m in range(1,101) if m%2==0]
print(n)

# List Function--------------------------->
l=[20,30,40,50,60]
del l[1]
print(l)

l=[20,30,40,50,60]
print(l.pop(2))
print(l)
l.remove(60)
print(l)
l.clear()
print(l)


l=[20,30,40,50,60]
l[0]=10
print(l)

l.insert(0,[5,6]) # insert any position
print(l)

l.append(70)
print(l)

l.append(["Hello","Hi"])
print(l)

l.extend([50,60])
print(l)

l=[20,30,40,50,60,20,10]
q=["Hello","World"]
print(l.count(20))
print(l.index(20))
print(max(l))
print(max(q))
l.sort()
print(l)
l.sort(reverse=True)
print(l)

l=[20,30,40,50,60,(12,"hy",[50,60])]
l.reverse()
print(l)


# string to list--->

# n=input("Enter the string: ")
# l=n.split()
# print(l)


l=[]
for i in range(1,4):
    n=input("Enter element no"+str(i)+": ")
    l.append(n)
print(l)
    
    
# Tuple----------------------------------->immutable, more than 1 value
t=(20,30,40,50,"hello",[10,20],(70,80))
print(t)
print(t[2])
for i in range(len(t)):
    print(t[i],end=" ")
print()
for a in t:
    print(a)
    
t=[10,20,60,70,20]
print(max(t))
print(sum(t))
print(t.count(20))
print(t.index(70))