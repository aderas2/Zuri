class car:
  #pass
  """
  This is a Car class
  """
  def __init__(self,name,color):
    self.name = name
    self.color=color

  """
  This is a method for Car classs
  """
  def accel(self):
    print('%s accelerates at 100mph' %self.name)


#print(type(car))

car_1 = car('mercedes','black')
#print(type(car_1))
print(car_1.name)
print(car_1.color)
car_1.accel()

print(help(car))


#Error handling
def calc(num1,num2):
  return num1 / num2

try:
  num1 = int(input('Enter your first number: \n'))
  num2 = int(input('Enter your second number: \n'))

  Division = calc(num1,num2)

except ZeroDivisionError as err:
  #print("You can't divide a number by zero(0) ")
  print("Error:", err)
else:
  print('No Error')

finally:
  print('This would work irrespective of the error')