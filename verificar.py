"""Executa os doctests dos modulos deste minicurso, sem dependencias externas.

Uso:
    python verificar.py soma
    python verificar.py
"""

import doctest
import importlib
import sys


MODULOS = ("soma", "concatenacao", "paridade", "media", "vogais", "maior")


def main() -> int:
    if len(sys.argv) > 2 or (len(sys.argv) == 2 and sys.argv[1] not in MODULOS):
        print("Uso: python verificar.py [nome_do_modulo]")
        print("Modulos:", ", ".join(MODULOS))
        return 2

    selecionados = MODULOS if len(sys.argv) == 1 else (sys.argv[1],)
    falhas_totais = 0
    exemplos_totais = 0

    for nome in selecionados:
        print("\n" + "=" * 60)
        print("VERIFICANDO:", nome)
        print("=" * 60)
        modulo = importlib.import_module(nome)
        falhas, exemplos = doctest.testmod(modulo, verbose=True)
        falhas_totais = falhas_totais + falhas
        exemplos_totais = exemplos_totais + exemplos

    print("\nRESUMO:", exemplos_totais, "exemplos;", falhas_totais, "falhas")
    if falhas_totais > 0:
        print("Ha casos que ainda precisam de correcao.")
        return 1
    print("Todos os exemplos selecionados passaram!")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
