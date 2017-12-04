with open("text.txt", "a", encoding="utf-8") as f: 
     print("Введите латинские слова.") 
     w=input() 
     if w=="": 
      print("Вы ничего не ввели.")
     else: 
      while w!="": 
         if w.endswith("re"): 
             f.write(w) 
             f.write("\n")
         if w.endswith("ri"):
             f.write(w)
             f.write("\n")
         if w.endswith("isse"):
             f.write(w)
             f.write("\n")
         w=input()
