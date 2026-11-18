"""Contagem de caracteres em textos."""


def contar_vogais(texto: str) -> int:
    """Conta vogais sem diferenciar letras maiusculas de minusculas.

    Args:
        texto: Texto a ser analisado.

    Returns:
        Quantidade de ocorrencias de a, e, i, o e u.

    Exemplos:
        >>> contar_vogais("banana")
        3
        >>> contar_vogais("AEIOU")
        5
        >>> contar_vogais("GitHub")
        2
        >>> contar_vogais("")
        0
    """
    quantidade = 0
    for letra in texto:
        if letra.lower() in "aeiou":
            quantidade = quantidade + 1
    return quantidade
