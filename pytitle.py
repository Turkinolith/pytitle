import pyperclip

print("lets build a title")
usertext = input("type in a string:")

headerFooter =  "".join(["*****"] + (["*"] * len(usertext)) + ["*****"])
titleLine = "".join(["**** "] + [usertext] + [" ****"])
combinedText = headerFooter + "\n" + titleLine + "\n" + headerFooter
pyperclip.copy(combinedText)
