S1=""                        
flag_probel=0
while S1=="" or flag_probel==0: 
                                  
 flag_probel=1    
                  
 print("Напишите свое слово")
 S1 = input( )
 i=len(S1)
 if " " in S1: 
               
       flag_probel=0
       print("Наша строка не должна содержать пробел")
       
 if i==0:
     
      flag_probel=0
      print("Вы не ввели строку")
 
flag=i 
S2=S1
print("========результат=================")
print()
print(S1)
while flag>1:
  flag=flag-1
  S2=S2[i-1]+S2[0:i-1]

  
  print(S2)
print()
print("==================================")
