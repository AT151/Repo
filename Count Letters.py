count = {}
text = input("Type in your text here: ").lower()
for letter in text:
    count[letter] = count.get(letter, 0) + 1


for x in sorted(count.keys()):
    print(x,count[x])

