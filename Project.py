"""
This program will determine if the user is meets the minimum physical and education requirments of their preferred US military Branch.

First we ask the user's preferred US military Branch
Question = "What US Military branch would you like to enlist in? Options include Army, Marines, Air Force, Navy and Coast Guard."

We ask if the user has graduated highschool or GED equivalent
Question = Have you graduated Highscool with atleast a 2.5 GPA or it's equivalent in GED. 
Then based on the answer 
we check to see if the user input is Yes, print "You meet the education minimum requirements for all the US military branches" 

if the user gives the wrong answer,
then print "You do not meet the education requirments for the US military, please seek a recruiter for further information"
then the loop will be termintated with a break statement. 

Second we ask the user's weight 
Question = "How many pounds do you weight (Weight in lbs)"

Thirdly we ask the user's height
question = "How tall are you (Height in inches - 12 inches = 1 foot)

Fourthly we ask the user's age
question = "What is your age?"

With the previous collected physical information regarding the user we calculate their BMI.
Then based on their respective chosen branch's requirement
the program will output if they meet the physical requirments of their preferred military branch.
If they do meet the physical requirments, the program will print ("You have met the physical requirements for US", [preferred branch]) 

"""

"""
Mbranch = " What US Military branch would you like to enlist in? Options include Army, Marines, Air Force, Navy and Coast Guard."

main
  education = " Have you graduated Highscool with atleast a 2.5 GPA or it's equivalent in GED. "
  answer = "Yes" 
  ask(education, answer)

ask
  tries = 0
  loop 1 time
     increment tries
     ask user input()
     check to see if user input is equal to yes
       if so, print "You meet the education minimum requirements for all the US military branches"
    elif if your branch is marines
      print "You meet the education requirement for the Marines"   
    elif not yes
      print to the user "You do not meet the education requirments for the US military, please seek a recruiter for further information"
      print to the user some clarfication  " Although you do not meet the education requirements, there are ways to enlist in which the enlisted branch of your choice will pay for your GED"
         break

weight = input("How many pounds do you weight (Weight in lbs): ")
height = input("How tall are you (Height in inches - 12 inches = 1 foot)")
age = input("What is your age?)
bmi = weight*703/(height*height)

if user meets physical requirements based on their height and weight
    print to the user " You meet the education minimum requirements for the United States" , [Selected Branch]
if not
    print "you don't meet the cut"


"""

