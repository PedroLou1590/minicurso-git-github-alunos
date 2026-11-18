"""Funcoes para manipulacao simples de textos."""


def concatenar(primeiro: str, segundo: str) -> str:
    """Junta dois textos preservando a ordem recebida.

    Args:
        primeiro: Texto que deve aparecer no inicio.
        segundo: Texto que deve aparecer no final.

    Returns:
        Uma nova string com os dois textos em sequencia.

    Exemplos:
        >>> concatenar("Git", "Hub")
        'GitHub'
        >>> concatenar("Ola", "!")
        'Ola!'
        >>> concatenar("", "Python")
        'Python'
    """
    resultado = primeiro + segundo
    return resultado
