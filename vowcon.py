a=input()
c=['a','e','i','o','u','A','E','I','O','U']
if((a>='a' and a<='z')or(a>='A' and a<='Z')):
 if(a in c):
  print("vowels")
 else:
  print("Consonants")
else:
 print("Invalid")
