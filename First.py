import re
text = "bgugubnijmokn yf jkm@gmail.com."
pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9+-]+\.[A-Z|a-z]{2,}\b'
regex = re.compile(pattern)
matches = regex.findall(text)
for i in matches:
    print(i)
