"""Calculos estatisticos introdutorios."""


def calcular_media(valores: list[int | float]) -> float:
    """Calcula a media aritmetica de uma lista nao vazia.

    Args:
        valores: Lista com pelo menos um numero.

    Returns:
        A media aritmetica dos valores.

    Raises:
        ValueError: Quando a lista esta vazia.

    Exemplos:
        >>> calcular_media([2, 4, 6])
        4.0
        >>> calcular_media([1, 2])
        1.5
        >>> calcular_media([5])
        5.0
        >>> calcular_media([])
        Traceback (most recent call last):
        ...
        ValueError: a lista nao pode estar vazia
    """
    if len(valores) == 0:
        raise ValueError("a lista nao pode estar vazia")

    total = 0
    for valor in valores:
        total = total + valor

    resultado = total / len(valores)
    return float(resultado)
