import re
pattern = re.compile('</?!?[A-Z]*[a-z]*[a-z0-9]*>?')
string =  open("demo.html", "r", encoding='utf-8')
#print(string.read())
result = re.findall(pattern, string.read())
print(result)
