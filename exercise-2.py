lines = []

with open("main.txt", "w") as f:
    text = str(input("Informe o texto: "))
    splitedText = " ".join(text.strip().split(" "))
    for splited in splitedText:
        f.writelines(splited)
    f.close()

with open("main.txt", "r") as f:
    for line in f:
        lines.append(line)
totalLine = " ".join(lines).split(" ")
print(totalLine)
repeatedWords = []
for line in totalLine:
    lineCount = totalLine.count(line)
    if lineCount >= 2:
        if not line in repeatedWords:
            repeatedWords.append(line)
            print(f"A palavra \"{line}\" se repete {lineCount} vezes!")
