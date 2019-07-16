ac = int(input())  
  
if ac > 1:  
   for i in range(2,ac):  
       if (ac % i) == 0:  
           print("no")  
           break  
   else:  
       print("yes")  
         
else:  
   print("no")
