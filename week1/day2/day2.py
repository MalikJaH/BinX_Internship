#loops
for v in [1,2,3,4,5]:
    if v == 3:
        break
    print(v)
#functions    
def greet(name,age):
    print(f"Hello {name} you are {age} years old")
greet("BinX", 20)
    
#list
list1  = [x for x in range(5) if x!=3] 
list2= [x+1 for x in range(5) if x %2 !=0]
print(list2)




#step1 - >>>>>>>

def stats(numbers):
    return {"mean":sum(numbers)/len(numbers),"max":max(numbers),"min":min(numbers)} 
print(stats([1,2,3,4,5]))

#step2 - >>>>>>>

def even(numbers):
    return [x for x in numbers if x%2==0]
print(even([1,2,3,4,5]))

#step3 - >>>>>>>

class BinX:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def greet(self):
        print(f"Hello {self.name} you are {self.age} years old")
        
b=BinX("BinX",20)
b.greet()

