# Definição / Definition
def print_hi(name):

    print(f'Hi, {name}') # esse f é de format, sem ele o python entende que tudo dentro do parenteses é texto
    print('Oi,' + name) # jeito antigo

def calcular_area_do_retangulo(largura, comprimento):
    return largura * comprimento

def calcular_area_do_quadrado(lado):
    return lado ** 2 #elevado ao quadrado

def calcular_area_do_triangulo(largura, comprimento):
    return largura * comprimento /2

def contagem_progressiva(fim):
    for numero in range(fim): #repetir o bloco de zero até o fim
        print(numero)

def candidato(nome, votos):
    for numero in range(votos):
        #cont = numero+1
        #print(f'{cont} - {nome}')

        if numero < 9:
            print(f'00{numero+1} - {nome}')
        elif numero < 99:
            print(f'0{numero+1} - {nome}')
        else:
            print(numero+1, '-', nome)

def brincar_de_plim(fim):
    for numero in range(fim):
        if numero % 4 == 0:
            print('PLIM!')
        else:
            print('{:0>3}'.format(numero))

# estrutura de identificação / execução do script
if __name__ == '__main__':
    resposta = 'C'

    while resposta.upper() != 'Z':
        print('==================================')
        print('#                               #')
        print('   M E N U   D E   O P Ç Õ E S  #')
        print('#                               #')
        print('#    [1] - Olá Mundo            #')
        print('#    [2] - Áre do Retângulo     #')
        print('#    [3] - Áre do Quadrado      #')
        print('#    [4] - Áre do Triângulo     #')
        print('#    [5] - Contagem Progressiva #')
        print('#    [6] - Candidato            #')
        print('#    [7] - Brincar de PLIM      #')
        print('#                               #')
        print('#    [Z] - Sair                 #')
        print('#                               #')
        print('==================================')

        resposta = input('Escolha sua opção: ')
        print(f'Opção escolhida: {resposta}')

        if resposta.upper() != 'Z':
            if resposta == '1':
                print_hi('Tete')
            elif resposta == '2':
                resultado = calcular_area_do_retangulo(4, 8)
                print(f'Resultado: {resultado}')
            elif resposta == '3':
                resultado = calcular_area_do_quadrado(4)
                print(f'Resultado: {resultado}')
            elif resposta == '4':
                resultado = calcular_area_do_triangulo(3, 5)
                print(f'Resultado: {resultado}')
            elif resposta == '5':
                contagem_progressiva(10)
            elif resposta == '6':
                candidato('Fake', 8)
            elif resposta == '7':
                brincar_de_plim(12)
            else:
                print('Escolha inválida!!!')
        else:
            print('Você escolheu sair.')






