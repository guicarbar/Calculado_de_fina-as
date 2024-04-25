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
    
#area do codigo

print('qual seu investimento inicial ?')
inv = verificar_v(input())

print('quanto meses vai deixar rendendendo ?')
print('nn sabe exatamente ? digite N, vamos calcular para vc ?')
tempox = input()

if tempox.upper() == 'N':
    print('qunatos anos vai deixar rendendendo ?')
    tempo_ano = int(input()) * 12
    print(f'voce vai deixar rendendo por {tempo_ano} rendendo')
    print('deseja adcionar mais quantos meses ? se ja esta satifesito coloque 0')
    tempo_meses = int(input())
    tempo = tempo_ano + tempo_meses
else:
    print(f'Vc vai deixar rendendo por {tempox} meses')
    tempo = tempox

