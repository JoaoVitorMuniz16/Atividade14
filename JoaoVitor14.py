Salário = float(input("insira o salário"))

if Salário > float('1250.00'):
    print ("seu salário é", Salário + (Salário/100))
else:
    print ("seu salário é", Salário + (Salário/150))