class Fibonacci:
	def __init__(self,n):
		self.n=n
		f=0
		s=1
		i=0
		print(f"fibo upto {n}: ")
		if f==1:	
			print(f)
		else:
			while n>i:
				print(f)
				sum=f+s
				f=s
				s=sum
				i=i+1
		
	
		
		
		
fibo1=Fibonacci(10)

