import os
import time
breakout=False
crimeseverity=False
crimesevereaction=False

# variables = 
# text
# gender
# name
# age
# height
# drunk


print ("Welcome to the test, Citizen.")
time.sleep(1)
print("Today you are applying for a job at the Agency.")
time.sleep(1)
print("By participating in this test, you agree to the terms and conditions.")
time.sleep(1)
print("Please type 'I agree.' if you agree to the terms above. ")
while True:
  try:
    text = (input("Your Answer: ")) 
    if text == ("I agree."): 
      print("Then we may begin.")
      time.sleep(1)
      break;
    elif text == ("I agree"):
      print("Then let's begin.")
      time.sleep(1)
      break;
    else:
      print("Please follow instructions.")
  except ValueError:
    print("Answer properly!")
    continue

os.system("clear")

print("You will fill out a survey for us.")
time.sleep(1)
print("It will be reviewed.")
time.sleep(1)
print("Please answer honestly.")
time.sleep(1)
name = (input('What is your name, Citizen? '))
print('Hello, %s.' % name)
time.sleep(1)
print ('How old are you?')
while True:
  try:
    age = int(input("Your answer: ")) 
    if age <= 40 and age >=18:
      break;
    elif age > 40:
      print ("You are too old to enlist!") 
    elif age < 18:
      print("You are too young to enlist!") 
  except ValueError:
    print("Please input your age.")
    continue
print("Okay.")
time.sleep(0.9)
os.system("clear")

time.sleep(1)
print("Are you a male or female?")
while True:
  try:
    gender = (input("Answer honestly: "))
    if gender == "Male":
      print("So you are a man?")
      time.sleep(1)
      break;
    elif gender == "Female":
      print("So you are a woman?")
      time.sleep(1)
      break;
    elif gender == "female":
      print("So you are a woman?")
      time.sleep(1)
      break;
    elif gender == "male":
      print("So you are a man?")
      time.sleep(1)
      break;
    else:
      print("Please input your gender.") 
  except ValueError:
    print("Please answer correctly.")
    continue
print("I see.")
time.sleep(1)
os.system("clear")

print("Have you drunk before?")
while True:
  try:
    drunk = (input('Answer : '))
    if drunk == "Y":
      print ("So you have drunk before?")
      break;
    elif drunk == "N":
      print ("So you have not drunk before?")
      break;
    else:
      print("Answer with Y/N")
  except ValueError:
    print("Answer with Y/N")
    continue
time.sleep(1)
os.system("clear")


print("Do you have any experience with firearms?")
while True:
  try:
    experience = (input("Answer : "))
    if experience == ("Y"):
      print("So you have shot a gun before?")
      break;
    elif experience == ("N"):
      print("So you have not shot a gun before?")
      break;
    else:
      print("Please answer with [Y/N]")
  except ValueError:
    print("Please answer with [Y/N]")
    continue

time.sleep(1)
print("Very well.")
time.sleep(1)
os.system("clear")

print("How tall are you?")

while True:
  try:
    height = int(input('cm : '))
    if height >= 165 and height <=195:
      break;
    elif height < 165:
      print("You are too short!")
    elif height > 195:
      print("You are too tall!")
    else: 
      print("Please enter your height in cm.")
  except ValueError:
    print ("Please enter your height in cm.")
    continue

print ("You are %d cm tall?" % height)
time.sleep(1)
print ("Very well.")
time.sleep(1)

os.system("clear")

print ("Have you commited any crimes?")
while True:
  try:
    crime = (input("Answer : "))
    if crime == "N":
      print("So you have not comitted any crimes?")
      time.sleep(1)
      break;
    elif crime == "Y":
      print("Was it a severe, or minor one?")

      while True:
        try:
          severity = (input("Answer : "))
          if severity == "Minor": 
            crimeseverity=True
            print("Very well then.")
            time.sleep(1)
            breakout=True
            break;
          elif severity == "Severe":
            crimeseverity=True
            crimesevereaction=True
            print("So, you have comitted a severe crime?")
            time.sleep(1)
            print("Like what?")
            time.sleep(1)
            os.system("clear")
            print("1. Homicide")
            print("2. Extortion")
            print("3. Blackmail")
            print("4. Use of drugs")
            print("5. Rape")
            print("6. Other")

            while True:
              try:
                actions = (input("Answer : "))
                if actions == "1":
                  print ("So you have killed someone before?")
                  time.sleep(1)
                  print ("That's okay, we do that alot here.")
                  time.sleep(1)
                  breakout=True
                  break
                elif actions == "2":
                  print("So you have extorted someone before?")
                  time.sleep(1)
                  print("Do not be ashamed, we do that alot here.")
                  time.sleep(1)
                  breakout=True
                  break
                elif actions == "3":
                  print("So you have blackmailed people before?")
                  time.sleep(1)
                  print("We do that alot here, do not be ashamed.")
                  time.sleep(1)
                  breakout=True
                  break
                elif actions == "4":
                  print("You have consumed illegal drugs?")
                  time.sleep(1)
                  print("I guess it is okay, as long as you do not do it here.")
                  time.sleep(1)
                  breakout=True
                  break
                elif actions == "5":
                  print("Rape? uh. We will note that down.")
                  time.sleep(1)
                  print("Very well.")
                  time.sleep(1)
                  breakout=True
                  break
                elif actions == "6":
                  print("Very well.")
                  time.sleep(1)
                  breakout=True
                  break
                else:
                  print("Answer the question with (1,2,3,4,5,6)")
              except ValueError:
                print("Answer the question with (1,2,3,4,5,6)")
                continue
            if breakout:
              break 
          else:
            print("Answer with [Severe\Minor]")
        except ValueError:
          print("Answer with [Severe\Minor]")
          continue
        if breakout:
          break
    else:
      print("Answer with Y/N")
  except ValueError:
    print("Answer with Y/N")
    continue
  if breakout:
    break

os.system("clear")

time.sleep(1)
print ("Now.")
time.sleep(1)
print("%s" % name)
time.sleep(1)
print("Here is a summary of all your answers.")
time.sleep(1)
os.system("clear")
print("Name : %s" % name)
time.sleep(0.5)
print("Gender : %s" % gender)
time.sleep(0.5)
print("Age : %s" % age)
time.sleep(0.5)
print("Height : %s cm" % height)
time.sleep(0.5)
print("Experience with firearms? : %s" % experience)
time.sleep(0.5)
print("Alcohol before? : %s" % drunk)
time.sleep(0.5)
print("Crime before? : %s" % crime)
time.sleep(0.5)
if crimeseverity is True:
  print("Crime severity : %s" % severity)
time.sleep(0.5)
if crimesevereaction is True:
  if actions == "1":
    print("Type : Homicide")
    time.sleep(0.5)
  elif actions == "2":
    time.sleep(0.5)
    print("Type : Extortion")
  elif actions == "3":
    print("Type : Blackmail")
    time.sleep(0.5)
  elif actions == "4":
    print("Type : Illegal substances")
    time.sleep(0.5)
  elif actions == "5":
    print("Type : Rape")
    time.sleep(1)
  elif actions == "6":
    print("Type : Other")
    time.sleep(0.5)
print("Summary Evaluation")
time.sleep(1.5)
os.system("clear")

loop = 0

while loop <=2:
  loop = loop + 1
  print("Evaluating results")
  time.sleep(0.5)
  os.system("clear")
  print("Evaluating results.")
  time.sleep(0.5)
  os.system("clear")
  print("Evaluating results..")
  time.sleep(0.5)
  os.system("clear")
  print("Evaluating results...")
  time.sleep(0.5)
  os.system("clear")

score = 1
#EVALUATION
if height >170:
  score = score + 1
elif height <170:
  score = score - 1

if drunk == "Y":
  score = score - 1
elif drunk == "N":
  score = score + 1

if experience == "Y":
  score = score + 1
elif experience == "N":
  score = score + 0

if crime == "N":
  score = score + 1

elif crime == "Y":
  if severity == "Minor":
    score = score + 0
  elif severity == "Severe":
    score = score - 1
    if actions == "1":
      score = score + 1
    elif actions == "2":
      score = score + 1
    elif actions == "3":
      score = score + 1
    elif actions == "4":
      score = score + 0
    elif actions == "5":
      score = score + 0
    elif actions == "6":
      score = score + 0

if score >=3:   #pass
  print ('We have come back to tell you.')
  time.sleep(1)
  print ('That you have passed the test!')
  time.sleep(1)
  print ('Your final score was %d' % score)
  time.sleep(1)
  print ('For more info regarding this application')
  time.sleep(1)
  print ('Please visit bit.ly/agencysummary')


elif score <=2:   #nopass
  print ("We regret to inform you.")
  time.sleep(1)
  print("That you have failed the test.")
  time.sleep(1)
  print("Please re-evaluate your ways and try again.")
