# Python RegEx
import re
import os
import datetime

os.system('cls')

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
os.system("cls")
print(datetime.datetime.now())

# Sets
# Returns a match where one of the specified characters (a, r, or n) are present
e = re.findall("[ing]", txt)
print(e)

if e:
  print("yes, there is at least one match!")
else:
  print("No match")
print()
print(datetime.datetime.now())

# Returns a match for any lower case character, alphabetically between a and n
e = re.findall("[a-d]", txt)
print(e)

if e:
  print("yes, there is at least one match!")
else:
  print("No match")
print()
print(datetime.datetime.now())

# Returns a match for any character EXCEPT a, r, and n
e = re.findall("[^a-z]", txt)
print(e)

if e:
  print("yes, there is at least one match!")
else:
  print("No match")
print()
print(datetime.datetime.now())

# Returns a match where any of the specified digits (0, 1, 2, or 3) are present
e = re.findall("[120]", txt)
print(e)

if e:
  print("yes, there is at least one match!")
else:
  print("No match")
print()
print(datetime.datetime.now())

# Returns a match for any digit between 0 and 9
e = re.findall("[0-9]", txt)
print(e)

if e:
  print("yes, there is at least one match!")
else:
  print("No match")
print()
print(datetime.datetime.now())

# Returns a match for any two-digit numbers from 00 and 59
e = re.findall("[0-2][0-9][0-9]", txt)
print(e)

if e:
  print("yes, there is at least one match!")
else:
  print("No match")
print()
print(datetime.datetime.now())

# Returns a match for any character alphabetically between a and z, lower case OR upper case
e = re.findall("[a-zA-Z]", txt)
print(e)

if e:
  print("yes, there is at least one match!")
else:
  print("No match")
print()
print(datetime.datetime.now())

# In sets, +, *, ., |, (), $,{} has no special meaning, so [+] means: return a match for any + character in the string
e = re.findall("[()]", txt)
print(e)

if e:
  print("yes, there is at least one match!")
else:
  print("No match")
print(datetime.datetime.now())
print()

# The findall() Function
t = re.findall("in", txt)
print(t)
print(datetime.datetime.now())
print()

# The search() Function
a1 = re.search("\s", txt)
print("The first white-space character is located in position:", a1.start())
print(datetime.datetime.now())
print()

# The split() Function
a2 = re.split("\s", txt)
print(a2)
print(datetime.datetime.now())
print()

# Split the string only at the first occurrence
a2 = re.split("\s", txt, 3)
print(a2)
print(datetime.datetime.now())
print()

# The sub() Function
a3 = re.sub("\s", "_", txt)
print(a3)
print(datetime.datetime.now())
print()

# You can control the number of replacements by specifying the count parameter
x = re.sub("\s", "_", txt, 4)
print(x)
print(datetime.datetime.now())
print()

# Match Object
x = re.search("es", txt)
print(x) #this will print an object
print(x.span())
print(x.string)
print(x.group())
print(datetime.datetime.now())
print()