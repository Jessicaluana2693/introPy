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

def exibir_dia_da_semana(numero):
    print('Exemplo do If - Elif - Else:')
    if numero == 1:
        print('O dia é segunda')
    elif numero == 2:
        print('O dia é terça')
    elif numero == 3:
        print('O dia é quarta')
    elif numero == 4:
        print('O dia é quinta')
    elif numero == 5:
        print('O dia é sexta')
    elif numero == 6:
        print('O dia é sábado')
    elif numero == 7:
        print('O dia é domingo')
    else:
        print('Opção inválida')

def exibir_dia_da_semana_match(numero):
    print('Exemplo do Match:')
    match numero:
        case 1:
            print('O dia é segunda')
        case 2:
            print('O dia é terça')
        case 3:
            print('O dia é quarta')
        case 4:
            print('O dia é quinta')
        case 5:
            print('O dia é sexta')
        case 6:
            print('O dia é sábado')
        case 7:
            print('O dia é domingo')
        case _:
            print("Valor {} é inválido".format(numero)) #wild card - caso genérico

def fim_de_semana(dia):
    print('Match usando operador lógico OU')
    match dia:
        case 'Domingo' | 'Sábado':
            return 'É Fim de semana'
        case 'Segunda' | 'Terça' | 'Quarta' | 'Quinta' | 'Sexta':
            return 'É dia útil'
        case _:
            return 'valor desconhecido'

def contas(centros):
    print('Match usando listas:')
    match centros:
        case [area, centros]: # Apenas 1 centro de custo
            print('A área {} possui o centro de custo {}'.format(area, centros))
        case [area, *centros]: # 2 centros ou mais
            print('A área {} possui os centros de custo abaixo:'.format(area))
            for centro in centros:
                print(centro)



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

    # exemplo de dia da semana com if estrutura
    exibir_dia_da_semana(11)

    #exemplo dia da semana com match - case
    exibir_dia_da_semana_match(0)

    #exemplo de fim de semana usando match case
    print(fim_de_semana('batata'))

    #exemplo de match case usando listas
    contas(['Financeiro', 'ABC'])
    contas(['Marketing', 'XYZ', 'JKL', 'XUXU'])
