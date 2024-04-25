#area de imports

#area de variaveis fixas

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
        print('isso nao é um numero')
        
    
#area do codigo

print('qual seu investimento inicial ?')
inv = input()

verificar_v(inv)
verifcar_n(inv)

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
    

print('a taxa de juros e ao mes ou ao ano ? A ou M')
taxa = input().upper()

if taxa == 'A':
    print('qual a taxa de juros ao ano ?')
    jurosx = input()
    verificar_v(jurosx)
    verifcar_n(jurosx)
    jurosx = int(jurosx)
    juros = jurosx / 12
elif taxa == 'M':
    print('qual a taxa de juros ao mes ?')
    jurosx = input()
    verificar_v(jurosx)
    verifcar_n(jurosx)
    juros = int(jurosx)



inv = int(inv)
tempo = int(tempo)
juros = juros / 100

montante = inv * juros * tempo

print(montante)