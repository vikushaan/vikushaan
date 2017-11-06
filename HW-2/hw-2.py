
flag=True
while flag==True:
 flag=False
 print('Сколько раз будем вводить слово?') 
 #
 while True :
         try:
             inp = int(input())
             print(inp)
             if inp<0:
                 flag=True
                 print('Число должно быть натуральним')
         except ValueError:
            print('Вы ввели не число')
            print('Сколько раз будем вводить слово?')
        
         else:
            
            break
        
 #     
 else:
    break

 
for i in range(0,inp):
 print("Введите слово(Если ввести <программирование> то программа"+
            " завершит работу ) ")
 nam = input()
 if nam =="программирование":
     break 
 else:   
     print(nam)
