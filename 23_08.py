'''
Exercício 1
---
Crie uma calculadora onde o usuário final irá entrar com 2 números
inteiros, depois iremos exibir um menu com as seguintes opções:
• Somar
• Subtrair
• Multiplicar
• Dividir
• Raiz quadrada
• Digitar outros números
• Sair
Ele irá selecionar a opção desejada e o  Python irá realizar
a operação matemática. Então o resultado será exibido na tela.
Depois de visualizar o resultado, o usuário retorna para o menu.
O teste se o número digitado é um inteiro deve ser realizado como
apresentado nas aulas anteriores.
Você deve também tratar os erros na divisão e no cálculo das
raízes quadradas.

'''

# ******************** RESOLUÇÃO DO EXERCÍCIO *************************

import math

''' ****  ESPAÇO RESERVADO PARA AS FUNÇÕES ****'''

def calculadora ():
    print('\n' + '-' * 40)
    print('{}'.format('                CALCULADORA'))
    print('-'*40)

def menu ():
    calculadora()
    print('1. Somar')
    print('2. Subtração')
    print('3. Multiplicação')
    print('4. Dividir')
    print('5. Rais Quadrada')
    print('6. Digitar outros números')
    print('7. Sair')


def somar(n1=0, n2=0):
    r =  n1+ n2
    return r

def subtracao(n1=0, n2=0):
    r = n1 - n2
    return r

def multiplicacao(n1=0, n2=0):
    r = n1 * n2
    return r

def dividir(n1=0, n2=0):
    try:
        r = n1 / n2
    except ZeroDivisionError:
        print('NÕ PODE REALIZAR UMA DIVISÃO POR ZERO')
        print('O N2 FOI ALTERADO PARA 1 DURANTE A DIVISÃO')
        n2 =1
        r = n1 / n2     
    print('\n {} / {} = {:.2f}'.format(n1,n2,r))

def raiz(n1=0, n2=0):
    try:
        raiz1 = math.sqrt(n1)
    except ValueError as Argument:
        print('NÃO É POSSÍVEL CALCULAR RAIZ DE UM NÚMERO NEGATIVO') 
    except Exception:
        print('NÃO É POSS[IVEL OBTER A RAIZ QUADRADA')
    else:
        print('A RAIZ QUADRADA DE {} É {:.2F}'.format(n1, raiz1))

    try:
        raiz2 = math.sqrt(n2)
    except ValueError as Argument:
        print('NÃO É POSSÍVEL CALCULAR RAIZ DE UM NÚMERO NEGATIVO') 
    except Exception:
        print('NÃO É POSS[IVEL OBTER A RAIZ QUADRADA')
    else:
        print('A RAIZ QUADRADA DE {} É {:.2F}'.FORMAT(n2, raiz2))
    r = raiz1 * raiz2
    print('O RESULTADO DAS RAIZES {} *{} É {:.2f}'.format(raiz1, raiz2,r))

''' **** FINAL DO ESPAÇO RESERVADO PARA AS FUNÇÕES **** '''
num1 = 0
num2 = 0

''' *** VALIDANDO NUMEROS DIGITADOS *** '''

while True:
    try:
        num1 = int(input('NUMERO 1: '))
        break
    except ValueError:
        print('NÃO É UM NÚMERO VÁLIDO. TENTE NOVAMENTE.')
    
while True:    
    try:
        num2 = int(input('NUMERO 2: '))
        break
    except ValueError:
        print('NÃO É UM NÚMERO VÁLIDO. TENTE NOVAMENTE.')

''' *** CHAMANDO O MENU DA CALCULADORA *** '''

while num1 > 0 and num2 >= 0:
    menu()
    opcao =  int(input('QUAL A SUA OPÇÃO[1,2,3,4,5,6,7]? '))

    ''' *** VERIFICANDO AS OPÇÕES DE MENU *** '''

    if opcao < 1 or opcao > 7:
        print('\n Opção inválida')
        input('\n Precione <ENTER>\n')
        continue
    
    elif (opcao ==1):
        res =  somar(num1, num2)
        print('\n {} + {} = {}'.format(num1, num2, res))
        input('\n Pressione <ENTER>\n')

    elif (opcao == 2):
        res =  subtracao(num1, num2)
        print('\n {} - {} = {}'.format(num1, num2, res))
        input('\n Pressione <ENTER>\n')
    
    elif (opcao == 3):
        res =  multiplicacao(num1, num2)
        print('\n {} * {} = {}'.format(num1, num2, res))
        input('\n Pressione <ENTER>\n')

    elif (opcao ==4):
        res =  dividir(num1, num2)
        #print('\n {} / {} = {}'.format(num1, num2, res))
        input('\n Pressione <ENTER>\n')
    
    elif (opcao ==5):
        res =  raiz(num1, num2)
        input('\n Pressione <ENTER>\n')

#''' *** SOLICITANDO OUTROS NUMEROS *** '''
    elif (opcao == 6):
        while True:
            try:
                num1 = int(input('NUMERO 1: '))
                break
            except ValueError:
                print('NÃO FOI UM NÚMERO VÁLIDO. TENTE NIVAMENTE')
        while True:
            try:
                num2 = int(input('NUMERO 2: '))
                break
            except ValueError:
                print('NÃO FOI UM NÚMERO VÁLIDO. TENTE NIVAMENTE')
        input('\n Pressione <ENTER>')
    elif (opcao == 7):
        break

