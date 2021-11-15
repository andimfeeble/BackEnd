#Folha de Pagamento
salario_bruto = float(input(f'Digite o valor do salário para o calculo da folha: R$'))
if salario_bruto >= 1100:
    #Calculo do valor do IR
    def calculo_ir():
        if salario_bruto <= 1903.98:
            valor_ir = salario_bruto * 0 / 100
        elif salario_bruto <= 2826.65:
            valor_ir = salario_bruto * 7.5 / 100
        elif salario_bruto <= 3751.05:
            valor_ir = salario_bruto * 15 / 100
        else:
            valor_ir = salario_bruto * 27.5 / 100
        return valor_ir


    #Calculo do valor do INSS
    def calculo_inss():
        if salario_bruto <= 1100:
            valor_inss = salario_bruto * 7.5 / 100
        elif salario_bruto <= 2203.49:
            valor_inss = salario_bruto * 9 / 100
        elif salario_bruto <= 3305.22:
            valor_inss = salario_bruto * 12 / 100
        else:
            valor_inss = salario_bruto * 14 / 100
        return valor_inss


    ir = calculo_ir()
    inss = calculo_inss()
    #Calculo do valor do Sindicato
    sindicato = salario_bruto * 3 / 100
    #Calculo do Salario Liquido
    salario_liquido = salario_bruto - (ir + inss + sindicato)
    
    
    #Impressão Demonstrativo
    print(f'''
-------Demonstrativo-------

Salario Bruto:    R${salario_bruto:.2f}
Desconto IR:      R${ir:.2f}
Desconto INSS:    R${inss:.2f}
Contrib. Sind:    R${sindicato:.2f}
Salario Liquido:  R${salario_liquido:.2f}
''')
else:
    print('O salário digitado nao pode ser menor que o salário mínimo atual!')