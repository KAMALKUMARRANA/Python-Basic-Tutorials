print("Kamal Kumar Rana")
n=int(input("Enter a number:: "))
print(n)
num=n
rev=0
length=len(str(n))
while(n!=0):
    rem=n%10
    rev=(rev)+(rem**length)
    n=n//10
    
print(rev)

if(rev==num):
    print(num,"is armstrong!")
else:
    print(num,"is not armstrong!")
    