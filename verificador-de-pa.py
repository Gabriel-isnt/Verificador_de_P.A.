# desafio final do chatgpt

def erro(palavra) -> None:  # deixa qualquer texto em vermelho
    """
    Essa função retorna a palavra ou frase em vermelho

    É usada para quando vou mostrar uma mensagem de erro qualquer
    """
    print(f'\033[91m{palavra}\033[0m' if isinstance(palavra, (str, int)) else palavra)



def tratando_sequencia() -> int:  # para não tratar no programa principal eu faço uma função
    """
    Essa função verifica e garante que o usuário digite um número positivo maior que 2 e retorna esse número
    """
    while True:
        try:
            numero = int(input('>> ').strip())
            if numero > 2:
                return a  # retornará o número se ele for maior que 2

            else:
                erro('Por favor, coloque números positivos maiores que 2')

        except ValueError:
            erro('Por favor, escreva somente números inteiros')


def tratando_numero() -> int:
    """
    Essa função retorna o número colocado pelo usuário
    """

    while True:
        try:
            return int(input('>> ').strip())

        except ValueError:
            erro('Por favor, escreva somente números inteiros')


def verifica_pa(sequencia) -> str:
    """
    Essa função recebe uma lista e fala se os números dela são uma P.A.
    """

    if isinstance(sequencia, list):

        razao = sequencia[1] - sequencia[0]  # verifico a razão inicial da sequência

        for index in range(len(sequencia) - 1):
            if (sequencia[index + 1]  - sequencia[index]) != razao:
                # razão inicial difere da nova razão não é uma P.A.
                return 'não é uma P.A.'

        return 'é uma P.A.'

    else:
        return 'só posso analisar listas'


# programa rodando
while True:
    numeros_usuario = []  # cria no início para não dar erro de escopo

    print('O número que você digitar, será o tamanho da sequência.')
    print('Qual tamanho você quer ?')
    quantidade_sequencia = tratando_sequencia()  # pega o tamanho desejado da sequência

    print('digite um número para a sequência,  ele não pode ser repetido')
    termina = 0
    while quantidade_sequencia != termina:  # garante que o usuário coloque todos os números na lista
        sequencia_usuario = tratando_numero()

        if sequencia_usuario not in numeros_usuario:

            numeros_usuario.append(sequencia_usuario)  # adiciona o número se ele não for repetido
            numeros_usuario.sort()  # ordena a lista

            print(numeros_usuario)

            termina += 1

        else:  # se colocar um número repetido
            erro('Não coloque números repetidos')


    # verificação de P.A.
    epa = verifica_pa(numeros_usuario)
    print(epa)

    continuar = str(input('você quer fazer outra sequência? [S / N]\n: ').strip().upper())
    if continuar not in ('S', 'SIM'):
        break
