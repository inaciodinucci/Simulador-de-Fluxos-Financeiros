def calcular_amortizacao(valor, taxa, periodos, parcela):
    """
    Calcula a tabela de amortização de um empréstimo.
    
    Args:
        valor (float): Valor do empréstimo
        taxa (float): Taxa de juros (em decimal)
        periodos (int): Número de períodos
        parcela (float): Valor da parcela
    
    Returns:
        list: Lista de tuplas com os valores da tabela de amortização
    """
    tabela = []
    saldo = valor
    
    for periodo in range(1, periodos + 1):
        juros = saldo * taxa
        amortizacao = parcela - juros
        saldo = saldo - amortizacao
        
        if saldo < 0.01:  # Evitar problemas de arredondamento
            saldo = 0
            
        linha = (
            periodo,
            round(parcela, 2),
            round(juros, 2),
            round(amortizacao, 2),
            round(saldo, 2)
        )
        tabela.append(linha)
        
        if saldo == 0:
            break
            
    return tabela