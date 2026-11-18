"""Comparacao de valores numericos."""


def maior_de_tres(primeiro: int, segundo: int, terceiro: int) -> int:
    """Retorna o maior entre tres numeros inteiros.

    Args:
        primeiro: Primeiro valor.
        segundo: Segundo valor.
        terceiro: Terceiro valor.

    Returns:
        Maior valor entre os tres argumentos.

    Exemplos:
        >>> maior_de_tres(8, 5, 3)
        8
        >>> maior_de_tres(1, 2, 9)
        9
        >>> maior_de_tres(-4, -2, -7)
        -2
        >>> maior_de_tres(5, 5, 5)
        5
    """
    if primeiro > segundo:
        return primeiro
    return segundo
