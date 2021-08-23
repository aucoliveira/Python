#Arquivos e Diretórios - Funções do sistema Operacinal

import os
from time import localtime
'''
print(os.system('ls -l'))
print(os.system('clear'))
print(os.cpu_count())
print(os.sep)
print(os.extsep)
tamanho = os.get_terminal_size()
print(tamanho)
'''
# Faça um script que crie um novo diretório com o nome "novo", depois
# mostre todos os arquivos e subpastas do local de execução do script
# altere o nome desse diretorio criado para backup, depois
# mostre novamente todos os arquivos e subpastas do local para execução
# Remova o diretorio backup

'''REsolução do problema'''
'''
os.mkdir('Novo')
print(os.system('ls -l '))
os.system('mv Novo Backup')
print(os.system('ls -l'))
os.system('rm -rf Backup')
print(os.system('ls -l'))
'''
#import datetime as dt
'''
#Informando uma hora exata
hora = datetime.time(2,30,23,34)
horas = datetime.time(2,30,23)
print(hora)
print("hora {}".format(hora.hour))
print('minutos {}'.format(hora.minute))
print('segundos {}'.format(hora.second))
print('Microsegundo {}'.format(hora.microsecond))

hora2 = hora.replace(6,25)
print(hora2.isoformat())

import datetime as dt

t1 = str(dt.time(9,35,23))
t2 = str(dt.time(10,23,00))

inicio = dt.datetime.strptime(t1, '%H:%M:%S')
fim = dt.datetime.strptime(t2, '%H:%M:%S')
diferenca = (fim - inicio)
print(diferenca)
'''

# Crie um script que mostre a hora 19h30,25. depois adicione 35m, depois mostra a nova hora, no formado iso
# alterea hora para 15h e mostre na tela no formato HH:MM:SS
'''
import datetime 

hora = datetime.time(19,30,25)
print(hora)

minutosTotais = hora.hour * 60 + hora.minute
minutosTotais += 35 # Somando os 35 min
novaHora = minutosTotais //60
novosMinutos = minutosTotais % 60
novosSegundos = hora.second
hora2 = datetime.time(novaHora, novosMinutos, novosSegundos)
print(hora2)

hora3 = hora2.replace(15)
print(hora3.strftime('%Hh %Min %Sseg' ))

import datetime,time
hora4 = time.localtime()
print(hora4.tm_hour,':', hora4.tm_min, ':',hora4.tm_sec)

print(time.ctime())
print(time.gmtime())

d1 = datetime.date.today()
print(d1)
d2 = datetime.date.today() + datetime.timedelta(days=159)
print(d2)
'''

import datetime
hoje = datetime.datetime.now()
print('Data atual: {}')