"""Verificacao de propriedades simples de numeros inteiros."""


def eh_par(numero: int) -> bool:
    """Informa se um numero inteiro e par.

    Args:
        numero: Inteiro a ser analisado.

    Returns:
        True para numeros pares, False para numeros impares.

    Exemplos:
        >>> eh_par(4)
        True
        >>> eh_par(7)
        False
        >>> eh_par(0)
        True
        >>> eh_par(-2)
        True
    """
    return numero % 2 == 0


resposta = eh_par(5)
resposta2 = eh_par(4)
print(resposta, resposta2)