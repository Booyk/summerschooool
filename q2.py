class classy:
     def _init_(self,arr,value):
       self.arr = []
       self.value = 1
       
       
     def _init_show(self,list1,summ):
       self.arr=list1
       self.value=summ
    
     def ans(self):
       for a in range(n):
         for b in range(n):
           if self.arr[a]+self.arr[b]==self.value:
             print("the index are :", a, end="")
             print(b)
   
          

list1= []

n = int(input("Enter number of elements : "))
summ= int(input("enter the sum : ")) 

for i in range(n):
    num = int(input())
 
    list1.append(num) 

c1= classy(list1,summ) 

c1.ans()