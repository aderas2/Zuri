from time import gmtime, strftime

name = input('What is your Name? \n')
allowedUsers = ['Rasaq','Ade','Bola']
allowedPassword = ['passwordRasaq','passwordAde','passwordBola']


dt_string = strftime("%Y-%m-%d %H:%M:%S +1", gmtime())

if (name in allowedUsers):
  password = input('Your password? \n')
  userID = allowedUsers.index(name)

  if(password == allowedPassword[userID]):

    print('Welcome %s, you have successfull log in at %s' %(name,dt_string))

    print('These are the available options:')
    print('1. withdrawal')
    print('2. cash deposit')
    print('3. compliant')

    selectedOption = int(input('Please select an option \n'))

    if(selectedOption ==1):
      print('You selected %s ' %selectedOption)
      print('How much would you like to withdraw')
      
      Amount = int(input('Please input amount \n'))
      print('Take your cash')

    elif(selectedOption ==2):
      print('You selected %s ' %selectedOption)
      print('How much do you like to deposit')
      
      amountDeposited = int(input('Please input amount \n'))
      print('Your current balance is $%s ' %amountDeposited )
      print('Thank you for banking with us')

    elif(selectedOption == 3):
      print('You selected %s ' %selectedOption)
      print('What are complaints')
      complaint = input('Please input complaints \n')
      print('Thank your for contacting us')

    else:
      print('Invalid Option selected, please try again')

  else:
    print('password Incorrect, please try again')

else:
  print('Name not found, please try again')