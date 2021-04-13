#register
#log-in


#initializing the system
import random

database = {}
def init():

    
    print('Welcome to bank php')
  
    haveAccount = int(input('Do you have account with us : 1 (yes) 2 (No) \n'))
    if (haveAccount == 1):
      login()

    elif (haveAccount == 2):        
      register()

    else:
      print('You have selected invalid option')
      init()


def login():
    print('********* login ******')
   
    accountNumberFromeUser = int(input('What is your account Number? \n'))
    password = input('What is your password? \n')

    for accountNumber,userDetails in database.items():
      if (accountNumber==accountNumberFromeUser):
        if(userDetails[3]==password):
          bankOperation(userDetails)
          
      else:
        print('Invalid account or password')
        login()


    


def register():
  print('******** Register ********')
  email = input('What is your email address? \n')
  first_name = input('What is your first name? \n')
  last_name = input('What is your last name? \n')
  password = input('please create a password. \n')

  accountNumber = generateAccountNumber()

  database[accountNumber] = [first_name,last_name,email,password]

  print('Your account has been created')
  print('==== ======= ====== ======= =====')
  print('Your account number is: %d' %accountNumber)
  print('Make sure you keep it safe')
  print('==== ======= ====== ======= =====')

  login()

 

def bankOperation(user):
    print('Welcome %s %s' %(user[0],user[1]))    

    selectedOption = int(input('What would you like to do? (1) deposit (2) Withdrawal (3) Logout (4) exit'))

    if (selectedOption == 1):      
      depositOperation()

    elif (selectedOption == 2):      
      withdrawalOperation()

    elif (selectedOption == 3):
      logout()

    elif (selectedOption == 4):
      exit()

    else:
      print('Invalid option selected')
      bankOperation(user)

def withdrawalOperation():
  print('Withdrawal')

def depositOperation():
  print('Deposit')

def logout():
  login()



def generateAccountNumber():
    return random.randrange(1111111111,9999999999)





### Actual Banking system ###
#print(generateAccountNumber())
init()