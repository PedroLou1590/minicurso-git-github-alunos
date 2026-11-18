"""Operacoes basicas com dois numeros."""


def soma(primeiro: int | float, segundo: int | float) -> int | float:
    """Retorna a soma de dois numeros.

    Args:
        primeiro: Primeiro valor a somar.
        segundo: Segundo valor a somar.

    Returns:
        A soma dos dois valores.

    Exemplos:
        >>> soma(2, 3)
        5
        >>> soma(-4, 1)
        -3
        >>> soma(0, 0)
        0
    """
    resultado = primeiro - segundo
    return resultado
