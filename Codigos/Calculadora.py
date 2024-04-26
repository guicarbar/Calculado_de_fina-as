#area de imports

#area de funçoes


def verificar_v(n):
    atualizado = ''
    for virgula in n:
        if virgula == ',':
            atualizado += '.'
        else:
            atualizado += virgula
    return atualizado

def inteiro(p):
    try:
        int(p)
        return True
    except ValueError:
        return False
    
def decimal(p):
    try:
        float(p)
        return True
    except ValueError:
        return False


def verifcar_n(p):
    if inteiro(p) == True or decimal(p) == True:
        print('tudo certo')
    else:
        print('isso nao é um numero adcionar um reset no codigo depois')
        
def simple():
    rendimento = inv * juros * tempo
    print(f'{inv}apos {tempo} meses rendendo a uma taxa de {juros} seu rendimento foi de {rendimento}')
    rendimento += inv
    print(f'somando um total de {rendimento}')

def composto():
    
    

#investimento inicial

print('qual seu investimento inicial ?')
inv = input()

inv = verificar_v(inv)
verifcar_n(inv)

#quanto tempo

print('quanto meses vai deixar rendendendo ?')
print('nn sabe exatamente ? digite N, vamos calcular para vc ?')
tempox = input()

if tempox.upper() == 'N':
    print('qunatos anos vai deixar rendendendo ?')
    tempo_ano = int(input()) * 12
    print(f'voce vai deixar rendendo por {tempo_ano} meses rendendo')
    print('deseja adcionar mais quantos meses ? se ja esta satifesito coloque 0')
    tempo_meses = int(input())
    tempo = tempo_ano + tempo_meses
else:
    verifcar_n(tempox)
    tempo = tempox

#juros simples ou composto

print('vc gostaria de adcionar mensalmente um valor no seu investimento ? S ou N')
y = str(input()).upper()

if y == 'S':
    calc = True
elif y == 'N':
    calc = False
    print('ok vamos continuar')
else:
    print('isso nn e um valor valido, adcionar o reset')
    
#taxa de juros

print('a taxa de juros e ao mes ou ao ano ? A ou M')
taxa = input().upper()

if taxa == 'A':
    print('qual a taxa de juros ao ano ?')
    jurosx = input()
    jurosx = verificar_v(jurosx)
    verifcar_n(jurosx)
    jurosx = int(jurosx)
    juros = jurosx / 12
elif taxa == 'M':
    print('qual a taxa de juros ao mes ?')
    jurosx = input()
    jurosx = verificar_v(jurosx)
    verifcar_n(jurosx)
    juros = int(jurosx)
else:
    print('isso nn e um numero, adcionar o reset no codigo')

#corrigindo as varivaeis

inv = int(inv)
tempo = int(tempo)
juros = juros / 100

#escolhendo formula

if calc == True:
    simple()
else:
    composto()