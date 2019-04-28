import codecs

alphabet = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZzАаБбВвГгДдЕеЁёЖжЗзИиЙйКкЛлМмНнОоПпРрСсТтУуФфЦцЧчШшЩщХхЬьЪъЫыЭэЮюЯяΨ&Ǻλ∆0123456789!•−⋅→.—"‘±’,/\?%#@^$*+-_– №:;©‐[]=|(){}<>«»\r\n\ufeff\t'
filename = "hello.txt"
file_alphabet = "alphabet.txt"
m = []
word_mass = []
word_size = []
index_word = []
index_key = []
secret = []
secret_word = []
test = []
test2 = []
no_found = []
k = 0
h = 0
z1 = 0
z2 = 0
u = '\n\r\ufeff'
numb = int(input("1)Ввод с клавиатуры \n"+"2)Чтения из файла \n"))
key = input("key: ") 
if numb == 1:
	word = input("message: ")
	v = 0
if numb == 2:
	
	with codecs.open(filename,'r', encoding = "utf8") as file: # --> файл нужно сохранять в UTF-8 кодировки
		word_txt = file.readlines()
		for i in range(0, len(word_txt)):
			word_size.append(word_txt[i])
			
		print("message: ",word_size)
	word = ''.join(word_size)

with codecs.open(file_alphabet,'r', encoding = "utf8") as file: # --> файл нужно сохранять в UTF-8 кодировки
	f_alphabet = file.readlines()
	for i in range(0, len(f_alphabet)):
		test2.append(f_alphabet[i])
	
########################################################################
for i in range(0,len(word)):

		test.append(word[i])
########################################################################		


c = 0
for j in range(0,len(test)):
	for i in range(0, len(alphabet)):
		if test[j] == alphabet[i]:
			c += 1
		
number = int(input(" 1)Шифрование \n"+" 2)Дешифрование \n")) 
########################################################################
for i in range(0,len(test)):
	m.append(0)
	secret.append(0)
	secret_word.append(0)
	word_mass.append(test[i])
	
for i in range(0,len(test)):
	k = k + 1
	m[i] = key[k-1]
	if k == len(key):
		k = 0
print(m)
for i in range(0,len(test)):
	for j in range(0,len(alphabet)):
		if test[i] == alphabet[j]:
			index_word.append(j)
			
			z1 += 1
		if m[i] == alphabet[j]:
			index_key.append(j)
			z2 += 1
			
	if z1 != z2:
		print("error")
		h = 1
		break


	if number == 1:	
		secret[i] = index_word[i] + index_key[i] #для шифрования + для дешифровани -
		if secret[i] >= len(alphabet):
			secret[i] = secret[i] - len(alphabet) #для шифрования secret - len(alphabet) для дешифрования secret + len(alphabet) - index_key
		secret_word[i] = alphabet[secret[i]]
	if number == 2:	
		secret[i] = index_word[i] - index_key[i] 
		if secret[i] >= len(alphabet):
			secret[i] = secret[i] + len(alphabet) - index_key[i] 
		secret_word[i] = alphabet[secret[i]]

if h == 1:
	print(" z1 = ",z1,"\nz2 = ",z2)
	print(" no found: "+word_mass[z2-1])
	with codecs.open(file_alphabet, 'a',encoding='utf8') as file: # --> запись в текстовый файл 
		file.write(word_mass[z2-1])

else:
	s = ''.join(secret_word) # --> преобразование из списка в строку 
	print(s)
	with codecs.open(filename, 'w',encoding='utf8') as file: # --> запись в текстовый файл 
		file.write(s)

