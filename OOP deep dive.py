class Animal:
  animal_type = 'Mammal'
  counter = 0

  def __init__(self,name,number_of_legs):
    self.name=name
    self.number_of_legs =number_of_legs
    Animal.counter +=1

  def can_run(self):
    print('Animal %s runs with %s' %(self.name,self.number_of_legs))

  @classmethod #class mwthod comes with all the declarations
  def can_see(cls):
    print('Animal can see')

  @staticmethod
  def tail_wiggle():
    print('Animal can wiggle it"s tail')



animal_1 = Animal('rat', 4)
animal_2 = Animal('cat', 4)

animal_1.can_run()
animal_2.can_run()

print('='*40)

print(animal_1.animal_type)
print(animal_2.animal_type)

print('='*60)
animal_1.can_see()
animal_2.can_see()


print(Animal.counter)
#types of method in classes: instance method, class method and static method

print('\n')

#inheritance and composition

# 1. Inheritance is a relationship
#class BaseClass:
#class SubClass(BaseClass):

print('='*60)
class food:
  def solid_food(self):
    return 'hard foods'

class water(food):
  pass

food_1 = water().solid_food()

print(food_1)

print('\n')
print('\n')


print('='*60)
class CustomException(Exception):
  pass

#raise CustomException('An error occurred')

class ValueTooSmallException(CustomException):
  pass
class ValueTooBigException(CustomException):
  pass

number_value = 20

while True:
  try:
    input_number = int(input('Enter a number \n'))
    if input_number < number_value:
      raise ValueTooSmallException
    elif input_number > number_value:
      raise ValueTooBigException

    break

  except ValueTooSmallException as _:
    print('Value too small')
  except ValueTooBigException as _:
    print('Value too big')
  except Exception as _:
    print(_.__str__())

print('Hey you got it correctly')

print('='*60)
print('\n')
#2. Composition shows has a relationship

class Employee:
  def __init__(self,name,department,salary):
    self.name = name
    self.department = department
    self.salary = salary

  def check_salary(self):
    return self.salary.check_salary()


class Salary:
  def __init__(self,amount,bonus):
    self.amount = amount
    self.bonus = bonus

  def check_salary(self):
    return ('Marketer"s salary is %d+ (%d*%d) with bonus of %d' %(self.amount,self.amount,self.bonus,self.bonus) )

marketer_salary = Salary(400000,5)
marketer_employee = Employee("Jones",'MArketing',marketer_salary)
print(marketer_employee.check_salary())



