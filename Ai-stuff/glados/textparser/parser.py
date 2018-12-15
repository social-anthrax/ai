import codecs
openfile = codecs.open("linesUnparsed.txt", encoding="utf8")
text = openfile.read()
printFile = codecs.open("../source/parsed.txt", mode="w",)
text = text.lower()
newText = ""
comment = True
for line in text.splitlines():
    for x in line:
        if x == '"':
            if comment == False:
                comment = True
            else:
                comment = False
        elif comment == False and line != "":
            newText += x
            # print(x)
        else:
            line = ""
    if line != "":
        newText += "\n"


newText = newText.replace('| download download | play icon.png play', '')
newText = newText.replace('"', '')

printFile.write(newText.upper())
printFile.close()
openfile.close()
