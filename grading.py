enterMarks = 'Enter the marks for '

math = float(input( enterMarks + 'maths: '))
sci = float(input( enterMarks + 'sci: '))
eng = float(input( enterMarks + 'eng: '))
pe = float(input( enterMarks + 'pe: '))
gsc = float(input( enterMarks + 'gsc: '))

sum = math + sci + eng + pe + gsc
print ('The sum is ' + str(sum))

avr = sum/5
print('The average is ' + str(avr))
grade="Your grade is: "
if (avr >=70 and avr<=100):
    print(grade + 'A')
elif (avr>= 60 and avr<=69):
    print(grade + 'B')
elif (avr>= 50 and avr<=59):
    print(grade + 'C')
elif (avr>= 40 and avr<=49):
    print(grade + 'D')
elif (avr>= 0 and avr<=39):
    print(grade + 'E')
