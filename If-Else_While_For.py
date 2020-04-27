#using turtle functions for example
import turtle
anushka_turtle=turtle.Turtle()
#for changing speed of turtle
anushka_turtle.speed(10)

def square():
  anushka_turtle.forward(100)
  anushka_turtle.right(90)
  anushka_turtle.forward(100)
  anushka_turtle.right(90)
  anushka_turtle.forward(100)
  anushka_turtle.right(90)
  anushka_turtle.forward(100)
  #full square

#IF- ELSE STATEMENTS
elephant_weight= 3000
ant_weight=0.1

if(elephant_weight>ant_weight):
   square()
else:
   anushka_turtle.forward(100)
   
   
# WHILE LOOP   
anushka="happy"

while anushka=="happy":
  anushka_turtle.forward(10)
   

#FOR LOOP    
for count in range(4):
  square()
#4 squares  
  
