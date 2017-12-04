with open("text.txt", "a", encoding="utf-8") as f: 
     print("Введите латинские слова.") 
     a=input() 
     if a=="": 
      print("Вы ничего не ввели.") 
     else: 
      while a!="": 
         if a.endswith("re"): 
             f.write(a) 
             f.write("\n")
         if a.endswith("ri"):
             f.write(a)
             f.write("\n")
         a=input()
