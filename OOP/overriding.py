class Emp:
    def fun(self,x,y):
        return(x+y)
    
    


class St(Emp):
    def fun(self,x,y):
        print(super().fun(x, y))
        return(x*y)




emp=St()
print(emp.fun(10,12))