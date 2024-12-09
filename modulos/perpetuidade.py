def calcular_perpetuidade(pmt, taxa):
    """
    Calcula o valor presente de uma perpetuidade.
    
    Args:
        pmt (float): Valor do pagamento
        taxa (float): Taxa de juros (em decimal)
    
    Returns:
        float: Valor presente da perpetuidade
    """
    return pmt / taxa