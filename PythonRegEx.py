# Python RegEx
import re

# txt = "When Ctrl-C is pressed on the keyboard, the while loop will terminate"
txt = "Yes, the string starts with hello. When Ctrl-C is pressed on the keyboard, the while loop will terminate cv.WaitKey(7) % 0x100!"
a = re.search("^When.*terminate$", txt)
if a:
    print("YES! We have a match!")
else:
    print("No match")
print()

# Metacharacters
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
print()

# Special Sequences
# Returns a match if the specified characters are at the beginning of the string
x = re.findall("\AYes", txt)

print(x)

if x:
  print("Yes, there is a match!")
else:
  print("No match")
print()

# Returns a match where the specified characters are at the beginning or at the end of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")
x = re.findall(r"\bstring", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

x = re.findall(r"ing\b", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

# Returns a match where the specified characters are present, but NOT at the beginning (or at the end) of a word
# (the "r" in the beginning is making sure that the string is being treated as a "raw string")
x = re.findall(r"\Bin", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

x = re.findall(r"rin\B", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

# 	Returns a match where the string contains digits (numbers from 0-9)
x = re.findall("\d", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

# Returns a match where the string DOES NOT contain digits
x = re.findall("\D", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

# Returns a match where the string contains any word characters (characters from a to Z, digits from 0-9, and the underscore _ character)
x = re.findall("\w", txt)

print(x)

if x:
  print("Yes, there is at least one match!")
else:
  print("No match")
print()

# Returns a match where the string DOES NOT contain any word characters (characters NOT between a and Z. Like "!", "?" white-space etc.)
x = re.findall("\W", txt)
print(x)
if x:
  print("Yes, there is at least one match")
else:
  print("No match")
print()

# Returns a match if the specified characters are at the end of the string

k = re.findall("0x100!\Z", txt)
print(k)

if k:
  print("Yes, there is a match!")
else:
  print("No match")
print()

# Sets