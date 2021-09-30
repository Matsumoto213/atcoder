import re
S = input()
judge = False
 
if S[0]=="A":
  judge = True
  if judge:
    num = (S[2:-1]).count("C")
    if num == 1:
      uppercase_characters = re.findall(r"[A-Z]", S)
      num = len(uppercase_characters)
      if num == 2:
        print("AC")
      else :
        judge = False
    else :
      judge = False
 
if judge == False:
  print("WA")