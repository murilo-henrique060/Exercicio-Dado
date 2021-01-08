def leiaint(mensagem='Digite Um Número Inteiro: ',erro='Erro! Por Favor, Digite um Número Inteiro Válido.',cor=False):
    """[Funciona como um input, Mas só retorna números inteiros.]

    Args:
        mensagem (str, optional): [mensagem do input]. Defaults to 'Digite Um Número Inteiro: '.
        erro (str, optional): [mensagem de erro]. Defaults to 'Erro! Por Favor, Digite um Número Inteiro Válido.'.
        cor (bool, optional): [opção de adicionar cor ao texto.]. Defaults to False.

    Returns:
        [int]: [Número Inteiro digitado.]

    Criado por:
        Murilo_Henrique060.
    """
    if cor:
        from colorama import init
        init()
    while True:
        número = input(mensagem)
        try:
            int(número)
        except:
            print(erro)
            continue
        return número
        break


def leiaInRange(numero=0,n1=0,n2=1,outRange='ERRO! Número Fora Do Alcance.',cor=False):
    """[Verifica se Um Número Está Dentro de um Range.]

    Args:
        numero (int, optional): [Númaero à Ser Verificado.]. Defaults to 0.
        n1 (int, optional): [começo do range]. Defaults to 0.
        n2 (int, optional): [final do range]. Defaults to 1.
        outRange (str, optional): [Mensagem se o número Estiver Fora do Range]. Defaults to 'ERRO! Número Fora Do Alcance.'.
        cor (bool, optional): [Adicionar ou Não Cores]. Defaults to False.

    Returns:
        [bool]: [retorna True ou False]
    Criado por:
        Murilo_Henrique060
    """
    if cor:
        from colorama import init
        init()
    v = 0
    for n in range(n1,n2+1):
        if n == numero:
            v += 1
    if v != 1:
        print(outRange)
        return False
    else:
        return True