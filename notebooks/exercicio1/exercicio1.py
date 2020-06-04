
#Autor: Mariana Soeiro
#About: Exercicio 1 - Lista 4 (Python)

#       -  Given a range of first 10 numbers [x]
#       -  Iterate from start number to the end number [x]
#       -  Print the sum of the current number and previous number


#Range of first 10 numbers
num = list(range(10))
pn = 0
for i in num:
    sum = pn + i
    print('Current Number =  '+ str(i) + ', Previous Number = ' + str(pn) + ' and Sum =  ' + str(sum)) # <- This is the issue.
    pn=i


