import random

print("1 is Heads.  0 is Tails")
flip = random.randint(0,1)
if flip == 0:
  print(f"{flip} Tails")

if flip == 1:
  print(f"{flip} Heads")