def calcule(num1, operator, num2):
    if operator == '+':
      résultat = num1+num2
      print(résultat)
    elif operator == '-':
        résultat = num1-num2
        print(résultat)
    elif operator == '*':
        résultat = num1*num2
        print(résultat)
    elif operator == '/':
        résultat = num1/num2
        print(résultat)
    elif operator == '%':
        résultat = num1%num2
        print(résultat)

calcule(num1=5, operator='+', num2=3)
calcule(num1=5, operator='*', num2=3)