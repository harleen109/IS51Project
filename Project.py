"""
This program will determine if the user is meets the minimum physical and education requirments of their preferred US military Branch.

First we ask the user's preferred US military Branch
Question = What US Military branch would you like to enlist in? Options include Army, Marines, Air Force, Navy and Coast Guard.

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

With the previous collected physical information regarding the user we calculate their BMI.
Then based on their respective chosen branch's requirement
the program will output if they meet the physical requirments of their preferred military branch.
If they do meet the physical requirments, the program will print ("You have met the physical requirements for US", [preferred branch]) 

"""