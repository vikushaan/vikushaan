with open("englishtext.txt", encoding='utf-8') as f:
        text = f.read()
        text = text.replace('-', '')
        text = text.replace(',', '').replace('.', '')
        text = text.replace('!', '').replace('?', '')
        text = text.replace(':', '').replace(';', '')
        text = text.lower()
        words = text.split()
        d = {}
        for word in words:
            end1 = word[-2:]
            if end1 in d: 
                d[end1] += 1
            else:
                d[end1] = 1
            end2 = word[-3:]
            if end2 in d: 
                d[end2] += 1
            else:
                d[end2] = 1
        count1 = 0
        count2 = 0
        for key, value in d.items():
            if key == 'ed':
                count1 += value
            if key == 'ied':
                count2 += value
        print('Количество форм на -ed в тексте: ', count1)
        print('Образованных от глаголов на -y и -e: ', count2)



