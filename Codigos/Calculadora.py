#area de imports

# area de variaveis fixas

#area de funçoes

def verificar(valor):
    return valor.isdigit()
    
# area de codigo

print('qual o valor inicial de investimento ?')
inv = input()

if verificar(inv) == True:
    print(f'ok seu investimento é de {inv}')
    inv = float(inv)    
    print(inv)
else:
    print('valor errado, recarrangando o programa')

