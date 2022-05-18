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
    print_hi('Tete')

    #chamar a função do calculo da area do retangulo
    resultado = calcular_area_do_retangulo(3,4)
    print(f'Area do rentângulo: {resultado} metros quadrados')

    #chamar a função de calculo do quadrado
    resultado = calcular_area_do_quadrado(5)
    print(f'Area do quadrado: {resultado} metros quadrados')

    #chamar a função do triangulo
    resultado = calcular_area_do_triangulo(6, 7)
    print(f'Area do triangulo: {resultado} metros quadrados')

    #executar a contagem progressiva
    contagem_progressiva(11)

    #mostrando o nome do candidato varias vezes
    candidato('Faker', 100)

    #brincar de plim
    brincar_de_plim(100)

