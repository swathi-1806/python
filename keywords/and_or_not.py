x=int(input("enter the x value:"))
y=int(input("enter the y value:"))
if x<30 and y<30:
  print("both conditions true")
if x>30 and y<30:
  print("one condition is true")
if not x %2==0:
  print("x is odd")
else:
  print("x is even")

  """
  output
  enter the x value: 25 
  enter the y value: 20
  both conditions true
  x is odd
  -----------------------
  enter the x value: 31
  enter the y value: 20 
  one conditions true
  x is even   

  """
