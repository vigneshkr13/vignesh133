lis=['a','e','i','o','u']
a=input()
if a.isalpha():
  if a in lis:
    print("Vowel")
  else:
    print("Consonant")
else:
  print("invalid")
