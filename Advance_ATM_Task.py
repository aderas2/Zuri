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
  
  database[accountNumber] = [first_name,last_name,email,password,100]

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
  
  print("Welcome to withdrawal service")
  print('How much would you like to withdraw')
  WithdrawALAmount = int(input('Please input amount \n'))
  if WithdrawALAmount<=accountBalance:
    print('Take your cash')
    print ("Your account balance is: $ ", accountBalance - WithdrawALAmount)
  else:
    print("Insufficient Fund, TRY AGAIN!!!")
    withdrawalOperation()
  

def depositOperation():
  print('How much do you like to deposit')
  
  amountDeposited = int(input('Please input amount \n'))
  print('You have successfully deposited $%s:' % amountDeposited)
  print('Your current balance is $', amountDeposited + accountBalance)
  print('Thank you for banking with us')


def accountBalance(user):
  return user[-1]


def logout():
  login()



def generateAccountNumber():
    return random.randrange(1111111111,9999999999)





### Actual Banking system ###
#print(generateAccountNumber())
init()