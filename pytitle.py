import pyperclip

print("lets build a title")
usertext = input("type in a string:")


headerFooter =  "".join(["*****"] + (["*"] * len(usertext)) + ["*****"])
titleLine = "".join(["**** "] + [usertext] + [" ****"])

#print(headerFooter)
#print(titleLine)
#print(headerFooter)

combinedText = headerFooter + "\n" + titleLine + "\n" + headerFooter
pyperclip.copy(combinedText)
