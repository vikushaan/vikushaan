with open("text.txt", encoding="utf-8") as f:
   text = f.read()
splited_text = text.split()
a = 0
b = 0

for i in enumerate(splited_text, start=1):
    if i[1] == '-':
        b += 1
    al = i[0] - b

    let = list(i[1])
    if let[-1] != '.' and let[-1] != ',' and i[1] != '-':
        a += 1
p = 100 * a / al
print("Процент от общего количества слов не оканчивается знаком препинания = ", round(p, 2), "%")

    
