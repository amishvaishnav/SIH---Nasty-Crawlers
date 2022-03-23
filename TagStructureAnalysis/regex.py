import re
pattern = re.compile('</?!?[A-Z]*[a-z]*[a-z0-9]*>?')
string =  open("demo.html", "r")

result = re.findall(pattern, string.read())

for i in range(len(result)):
    result[i] = result[i].replace("<", "")
    result[i] = result[i].replace(">", "")
    # result[i] = result[i].replace("/", "")

print(result)