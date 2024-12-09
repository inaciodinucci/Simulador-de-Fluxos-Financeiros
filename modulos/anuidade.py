def calcular_anuidade(pmt, taxa, periodos, tipo):
    """
    Calcula o valor presente de uma anuidade.
    
    Args:
        pmt (float): Valor do pagamento
        taxa (float): Taxa de juros (em decimal)
        periodos (int): Número de períodos
        tipo (str): 'ordinaria' ou 'vencida'
    
    Returns:
        float: Valor presente da anuidade
    """
    if tipo == "ordinaria":
        vp = pmt * ((1 - (1 / (1 + taxa)**periodos)) / taxa)
    else:  # vencida
        vp = pmt * ((1 - (1 / (1 + taxa)**periodos)) / taxa) * (1 + taxa)
    
    return vp