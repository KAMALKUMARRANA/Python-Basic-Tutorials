print("Hello world")
name="Kamal"
age=20
sal=25.5
print(type(sal))
#name=input("What your name? ")
print("hello "+name)
#old_age=int(input("Enter your old age: "))
#new_age=old_age+2
#print(new_age)
#float(),str(),bool()
#first=input("Enter the first number: ")
##second=input("Enter the second number: ")
#sum=int(first)+int(second)
#print(sum)

# List------------------------------>Mutable
marks=[1,4,6,7,2]
print(marks[3])
print(marks[-5])
print(marks[1:5])
for i in marks:
    print(i)

marks.append(10)
marks.insert(0,11)
print(11 in marks)
print(marks)

#print(len(marks))

i=0
while i<len(marks):
    print(marks[i])
    i+=1
marks.clear()
print(marks)

students=["ram","shyam","kishan","radha","radhika"]
for i in students:
    if i=="radha":
        #break
        continue
    print(i)

#  Tuple----------------------->Immutable
marks=(95,96,98,96)
name="kd","js","hd"
print(type(name))
#marks[0]=99 not work
print(marks.count(96))
print(marks.index(96))
# Set--------------------------->
marks={98,96,95,95} # all unique value # index does not exist-- unorderd
print(marks)
for i in marks:
    print(i)

# Dictionary---------------------------->
marks={"English":97,"Chemistry":99}
print(marks["Chemistry"])

