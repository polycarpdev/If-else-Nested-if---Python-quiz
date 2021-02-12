#print(9%2)

#operators
#

conversion = int(input('Choose to convert from which unit: \n 1. Celcius to Fahrenheit\n 2. Fahrenheit to Celcius\n\n Enter 1 or 2 :'))
if (conversion == 1):
    c = int(input('Enter Temperature in celcius: '))
    f = int((9*c/5)+32)
    print( str(c) + ' degrees celcius = ' + str(f) + ' fahrenheight')
elif (conversion == 2):
    f = int(input('Enter Temperature in fahrenheight: '))
    c = int((f-32)*(5/9))
    print( str(f) + ' degrees fahrenheight = ' + str(c) + ' celcius')
else:
    print('Your selection is out of range! Please run the program to start over again.')
