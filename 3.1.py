text = input()
print(text[0], text[-1])
for i in range (len(text)):
    print(text[len(text)-i-1], end="")