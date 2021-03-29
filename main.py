import turtle

#Ask the user how many sides they want for the polygon
#Create the polygon based on the userinput

userShape = int(input("How many sides do you want for your shape? "))

while(userShape > 10 or userShape < 3):
  print("Sorry! Invalid input. Try again")
  userShape = int(input("Please choose sides for a shape between 3 and 10."))
  break

turtle.shape("turtle")

for i in range (userShape):
  if(userShape != 99):
    turtle.forward(100)
    turtle.right(360/userShape)
