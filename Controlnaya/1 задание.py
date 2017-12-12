f = open("/Users/victoriagevorkyan/Desktop/Ozhegov.txt", encoding="utf-8")
lines = f.readlines()
for line in lines:
    words = line.split("|")
    word = words[0]
    if len(word) >= 20:
        print(line)
    
