import re # re - регулярные выражения
text = "abbbbba"
a = re.match(r'ab*', text) #re.match - ищет совпадения , a - значит начинаеться должно с а , и b* ноль или более б
print(a)
# 2
import re
text = "abbbb"
a = re.match(r'abbb?', text) # обязательно а потом 3 б и в конце либо одна либо нет б
print(a)
# 3
import re
text = "ab_ asdlkfjals_ alsdkjflasdjf  _"
a = re.findall(r'[a-z]+_', text) # [a-z] одна или более маленьких латинскиих букв
print(a)
# 4
text = "aQb_ Aasdlkfjals_ alsdkjfBlasdjf  _"
a = re.findall(r'[A-Z][a-z]+', text) # [A-Z] одна заглавная и одна или более маленьких букв
print(a)
# 5
import re

text ="asdjfka;skdhjflkahdsfklahsdfj # ) b"
a = re.match(r"a.*b\b", text) # сначала а потом любые символы потом буква б и чтобы после нее не было букв
print(a)
# 6
cnt = re.sub(r"[ .,]", ":", cnt) # [] - ищем замену символов внутри кв скобок "" на то что мы заменяем

with open("row.txt", "w", encoding="utf-8") as file:
    file.write(cnt)
# 7
cnt = re.sub(r"(_[a-z])", lambda x: x.group(1)[1].upper(), cnt) #x.group(1) — это совпадение из группы . [1] — берем второй символ . .upper() — переводим букву в заглавную, то есть W.

with open("row.txt", "w", encoding="utf-8") as file:
    file.write(cnt)
# 8
cnts = re.split(r"([A-Z][^A-Z]*)", cnt) # ищет заглавную букву после чего ищет любые символы кроме заглавных букв
# 9
cnt = re.sub(r"([a-z])([A-Z])", r"\1 \2", cnt) # ищет сначала маленькую букву после которой сразу должна идти большая буква re.sub() - находит место между маленькой и заглавной буквой и между ними ставит пробел 

with open("row.txt", "w", encoding="utf-8") as file:
    file.write(cnt)

# 10
cnt = re.sub(r"([a-z])([A-Z])", r"\1_\2", cnt).lower() # тоже самое только между буквами ставит _ и .lower() - преобразовывает весь текст в маленькие буквы

with open("row.txt", "w", encoding="utf-8") as file:
    file.write(cnt)
