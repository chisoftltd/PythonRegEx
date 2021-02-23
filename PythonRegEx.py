# Python RegEx
import re

# txt = "When Ctrl-C is pressed on the keyboard, the while loop will terminate"
txt = "Yes, the string starts with hello. When Ctrl-C is pressed on the keyboard, the while loop will terminate cv.WaitKey(7) % 0x100"
a = re.search("^When.*terminate$", txt)
if a:
    print("YES! We have a match!")
else:
    print("No match")
print()

b = re.findall("[a-i]", txt)
print(b)
print()

c = re.findall("\d", txt)
print(c)
print()

d = re.findall("W..n", txt)
print(d)
print()

x = re.findall("^Yes", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
print()

x2 = re.findall("0x100$", txt)
if x2:
  print("Yes, the string ends with '0x100'")
else:
  print("No match")