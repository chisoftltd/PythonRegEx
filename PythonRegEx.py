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

# A set of characters
b = re.findall("[a-i]", txt)
print(b)
print()

# Signals a special sequence (can also be used to escape special characters)
c = re.findall("\d", txt)
print(c)
print()

# 	Any character (except newline character)
d = re.findall("W..n", txt)
print(d)
print()

# Starts with
x = re.findall("^Yes", txt)
if x:
  print("Yes, the string starts with 'hello'")
else:
  print("No match")
print()

# Ends with
x2 = re.findall("0x100$", txt)
if x2:
  print("Yes, the string ends with '0x100'")
else:
  print("No match")
print()

# Zero or more occurrences
x = re.findall("rix*", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

# One or more occurrences
x = re.findall("erm+", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

# Exactly the specified number of occurrences
x = re.findall("s{2}", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

# Either or
x = re.findall("while|terminate ", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
