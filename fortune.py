import random

def fortune():
  c = random.randint(1,8)
  if c == 1:
    print("Don't pursue happiness – create it.")
  elif c == 2:
    print("All things are difficult before they are easy.")
  elif c == 3:
    print("The early bird gets the worm, but the second mouse gets the cheese.")
  elif c == 4:
    print("Someone in your life needs a letter from you.")
  elif c == 5:
    print("Don't just think. Act!")
  elif c == 6:
    print("Your heart will skip a beat.")
  elif c == 7:
    print("The fortune you search for is in another cookie.")
  elif c== 8:
    print("Help! I'm being held prisoner in a Chinese bakery!")
  else:
    print("not your day")



fortune()
fortune()
fortune()