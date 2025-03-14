import re
text = "abbbbba"
a = re.match(r'ab*', text)
print(a)
# 2
import re
text = "abbbb"
a = re.match(r'abbb?', text)
print(a)
# 3
import re
text = "ab_ asdlkfjals_ alsdkjflasdjf  _"
a = re.findall(r'[a-z]+_', text)
print(a)
# 4
text = "aQb_ Aasdlkfjals_ alsdkjfBlasdjf  _"
a = re.findall(r'[A-Z][a-z]+', text)
print(a)
# 5
import re

text ="asdjfka;skdhjflkahdsfklahsdfj # ) b"
a = re.match(r"a.*b\b", text)
print(a)
# 6
cnt = re.sub(r"[ .,]", ":", cnt)

with open("row.txt", "w", encoding="utf-8") as file:
    file.write(cnt)
# 7
cnt = re.sub(r"(_[a-z])", lambda x: x.group(1)[1].upper(), cnt)

with open("row.txt", "w", encoding="utf-8") as file:
    file.write(cnt)
# 8
cnts = re.split(r"([A-Z][^A-Z]*)", cnt)
# 9
cnt = re.sub(r"([a-z])([A-Z])", r"\1 \2", cnt)

with open("row.txt", "w", encoding="utf-8") as file:
    file.write(cnt)

# 10
cnt = re.sub(r"([a-z])([A-Z])", r"\1_\2", cnt).lower()

with open("row.txt", "w", encoding="utf-8") as file:
    file.write(cnt)
