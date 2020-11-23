# I've tidied up the indents - they're really important to watch!

def main():
    #write your code below this line
  while True:
    try:
      number_one = int(input('please  choose a number: '))
      break
    except:
        print("Please enter an integer!")

  # watch indents...
  while True:
    try:
      number_two = int(input('please choose a number: '))
      break
    except:
        print("Please enter an integer!")
             
         
  # The only thing you need to do now is fix this print statement so it matches the README. Something like this:
  # print(str(number_one) + " + " + str(number_two) " = " number_one + number_two)
  print(str(number_one) + ' + ' + str(number_two) + ' = ' +  str(number_one + number_two))
  
    
if __name__ == '__main__':
    main() #this needs an indent
