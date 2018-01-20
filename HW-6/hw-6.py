# Нигде не нужно ничего вставлять, кроме своего пути в 47 строке!
import random
import re

def file_read(filepath): #читаем текст из файла
	with open(filepath, "r", encoding="utf-8") as text:
		return text.read()

def get_words(text): #разбиваем текст на слова, длина которых > 1
	return list(filter(lambda x: len(x) > 1, re.findall(r"[\w']+", text.lower())))

def replace_tongs_with_sounds(word): #заменяем дифтонги и трифтонги на соостветствующее слогам кол-во @
	for tong in ('aio', 'aia', 'aiu', 'uoi', 'iei'):
		word = word.replace(tong, '@@') #трифтонги
	for tong in ('ia', 'ie', 'ai', 'ui', 'eu', 'io', 'iu', 'oi', 'uo', 'ei'):
		word = word.replace(tong, '@') #дифтонги
	return word
	

def get_syllable_count(word): #возвращаем колличество гласных (слогов) в слове
	word = replace_tongs_with_sounds(word)
	return sum(word.count(vowel) for vowel in ('a','e','i','o','u', '@')) #@ – не гласная, но обозначает кол-во звуков

def choose_word(words, max_syllables): #рандомно выбираем слово с подходящим кол-вом гласных (слогов)
	while True:
		word = random.choice(words)
		if get_syllable_count(word) <= max_syllables: #если количество слогов меньше максимального
			return word, get_syllable_count(word) #возвращаем количество слогов

def generate_five_syllables_string(words): #генерируем строку с 5 слогами
	syllables_sum = 0
	string = ""
	while(syllables_sum != 5): #пока сумма слогов в строке не равна 5
		word, syllable_count = choose_word(words, 5-syllables_sum) #выбираем слово
		string += word + " " #прибавляем его к строке
		syllables_sum+=syllable_count; #прибавляем кол-во слогов к общему
	return string

def generate_seven_syllables_string(words): #то же самое только для 7 слогов
	syllables_sum = 0
	string = ""
	while(syllables_sum != 7):
		word, syllable_count = choose_word(words, 7-syllables_sum)
		string += word + " "
		syllables_sum+=syllable_count;
	return string

if __name__ == '__main__':
	words = get_words(file_read("/Users/victoriagevorkyan/Desktop/Хокку python/Itallian_text.txt"))
	print(generate_five_syllables_string(words))
	print(generate_seven_syllables_string(words))
	print(generate_five_syllables_string(words))
