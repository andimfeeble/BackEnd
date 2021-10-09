#Exercicio89
opcao = ''
lista = []
print('-------CADASTRO DE ALUNO--------')
while opcao != 'N':
    nome = str(input('Digite o nome do aluno: ')).strip().capitalize()
    nota1 = float(input('Digite a primeira nota: '))
    nota2 = float(input('Digite a segunda nota: '))
    media = (nota1 + nota2) / 2
    lista.append([nome, nota1, nota2, media])
    print('-------Cadastro Realizado-------')
    print()
    opcao = str(input('Deseja cadastrar outro aluno? [S/N] ')).strip().upper()
print()
print('--------BOLETIM DA TURMA---------')
print(f'{"Cod.":<5} {"NOME":<10} {"MEDIA":>10}')
print('-' * 32)
for indice, aluno in enumerate(lista):
    print(f'{indice + 1:<5} {aluno[0]:<10} {aluno[3]:>10.1f}')
opcao = ''
print('-' * 32)
print()
while opcao != 'N':
    codigo = int(input('Digite o cod. do Aluno para consulta: '))
    print(f'{"Cod.":<5} {"NOME":<10} {"1ª NOTA":>10} {"2ª NOTA":>10}')
    if codigo >= 1 and codigo <= len(lista):
        for indice, aluno in enumerate(lista):
            if (codigo - 1) == indice:
                print('-' *38)
                print(f'{indice + 1:<5} {aluno[0]:<10} {aluno[1]:>10.1f} {aluno[2]:>10.1f}')
                print('-' *38)
            else:
                pass
    else:
        print('Codigo digitado inexistente!')
    print()
    opcao = str(input('Deseja consultar outro aluno? [S/N] ')).strip().upper()
print('-' * 32)
print('-------Sistema Finalizado!------')
print('-' * 32)