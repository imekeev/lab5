import re
text = "abbbbba"
a = re.match(r'ab*', text)
print(a)
#Exercise 2--------------------------------------------------------------------------
import re
text = "abbbb"
a = re.match(r'abbb?', text)
print(a)
#Exercise 3--------------------------------------------------------------------------
import re
text = "ab_ asdlkfjals_ alsdkjflasdjf  _"
a = re.findall(r'[a-z]+_', text)
print(a)
#Exercise 4-------------------------------------------------------------------------- import re
text = "aQb_ Aasdlkfjals_ alsdkjfBlasdjf  _"
a = re.findall(r'[A-Z][a-z]+', text)
print(a)
#Exercise 5-------------------------------------------------------------------------- ^ ensures it starst with a, $ ensures it ends with b, .* means whatever even nothing counts
import re

text ="asdjfka;skdhjflkahdsfklahsdfj # ) b"
a = re.match(r"a.*b\b", text)
print(a)
#Exercise 6-------------------------------------------------------------------------- [ .,] everything inside [] is counted, its quite useful
cnt = re.sub(r"[ .,]", ":", cnt)

with open("row.txt", "w", encoding="utf-8") as file:
    file.write(cnt)
#Exercise 7--------------------------------------------------------------------------
cnt = re.sub(r"(_[a-z])", lambda x: x.group(1)[1].upper(), cnt)

with open("row.txt", "w", encoding="utf-8") as file:
    file.write(cnt)
#Exercise 8--------------------------------------------------------------------------
cnts = re.split(r"([A-Z][^A-Z]*)", cnt)
# Exercise 9-------------------------------------------------------------------------- () captures the whole things \1 is first part, \2 is second part
cnt = re.sub(r"([a-z])([A-Z])", r"\1 \2", cnt)

with open("row.txt", "w", encoding="utf-8") as file:
    file.write(cnt)

# Exercise 10-------------------------------------------------------------------------
cnt = re.sub(r"([a-z])([A-Z])", r"\1_\2", cnt).lower()

with open("row.txt", "w", encoding="utf-8") as file:
    file.write(cnt)
