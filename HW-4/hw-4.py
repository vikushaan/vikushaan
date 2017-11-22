with open("text.txt", encoding="utf-8") as f:
   text = f.read()
splited_text = text.split()
wt = 0
t = 0

for i in enumerate(splited_text, start=1):
    if i[1] == '-':
        t += 1
    al = i[0] - t

    let = list(i[1])
    if let[-1] != '.' and let[-1] != ',' and i[1] != '-':
        wt += 1
p = 100 * wt / al
print("Процент от общего количества слов не оканчивается знаком препинания = ", round(p, 2), "%")

    
