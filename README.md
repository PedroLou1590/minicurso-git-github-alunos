# Git e GitHub — Oficina de contribuição (UEM)

**Minicurso:** Git e GitHub  
**Apresentadores:** Pedro Vitor da Costa Lourenço e Gabriel Gongora — UEM  
**Pré-requisitos:** Git, Python 3.10+ e uma conta GitHub.  
**Dependências externas:** nenhuma.

## Sua missão

Este repositório contém funções Python simples com **erros intencionais na implementação**. As **docstrings e seus exemplos (doctests) descrevem o comportamento esperado**. Por isso, alguns testes falham antes da correção. Isso é normal!

Você vai: **clonar → criar branch → investigar → corrigir/refatorar → testar → commitar → enviar → abrir Pull Request**.

> **Atenção:** cada pessoa ou dupla deve trabalhar em **um arquivo designado pelo instrutor**, mantendo o restante do projeto inalterado. Não corrija todos os erros em uma única Pull Request.

## Arquivos para escolher

| Arquivo | Função | Objetivo |
|---|---|---|
| `soma.py` | `soma` | Somar dois números |
| `concatenacao.py` | `concatenar` | Juntar textos na ordem correta |
| `paridade.py` | `eh_par` | Reconhecer números pares |
| `media.py` | `calcular_media` | Calcular média aritmética |
| `vogais.py` | `contar_vogais` | Contar vogais maiúsculas e minúsculas |
| `maior.py` | `maior_de_tres` | Escolher o maior entre três inteiros |

Leia os detalhes em [TAREFAS.md](TAREFAS.md).

## Testes com doctest

Para testar **somente seu arquivo**, execute no terminal dentro da pasta do projeto:

```bash
python verificar.py soma
```

Substitua `soma` por `concatenacao`, `paridade`, `media`, `vogais` ou `maior`.

Você também pode usar o doctest diretamente:

```bash
python -m doctest -v soma.py
```

Para testar todos os módulos:

```bash
python verificar.py
```

**Importante:** o teste completo pode continuar mostrando falhas enquanto os exercícios de outras pessoas não forem corrigidos. **O que precisa passar antes de sua PR é o teste do módulo que você alterou.**

Se o Windows não reconhecer `python`, tente `py` nos comandos acima.

## Passo a passo: quem tem permissão de escrita no repositório

A pessoa responsável pelo minicurso informará a URL do repositório.

```bash
git clone URL_DO_REPOSITORIO
cd NOME_DA_PASTA
git switch -c fix/nome-sobrenome-soma
python verificar.py soma
```

Agora corrija e organize o código do **arquivo designado** e repita o teste até ele passar.

```bash
git status
git diff
git add soma.py
git commit -m "fix(soma): corrige a adicao de dois numeros"
git push -u origin fix/nome-sobrenome-soma
```

No GitHub, use **Compare & pull request**, selecione `main` como base, preencha o modelo e abra a Pull Request.

Substitua os nomes e o módulo dos comandos pelo seu nome e pela sua tarefa. **Não execute `git push origin main`.**

## Sem permissão de escrita? Utilize um fork

1. Abra o repositório original no GitHub e clique em **Fork**.
2. Faça `git clone URL_DO_SEU_FORK`, não a URL do original.
3. Dentro da pasta clonada, crie a branch com `git switch -c fix/nome-sobrenome-soma`.
4. Corrija, teste, faça `git add`, `git commit` e `git push -u origin NOME_DA_BRANCH`.
5. No GitHub, abra uma Pull Request **do seu fork/branch para o repositório original/main**.

## Regras da entrega

Consulte o arquivo [CONTRIBUINDO.md](CONTRIBUINDO.md) para os nomes de branches, commits e Pull Requests. Todo aluno ou dupla deve seguir o mesmo padrão.

## Dúvida frequente

**Por que o teste está falhando?** Porque o código precisa ser corrigido. **Por que o `git commit` não aparece no GitHub?** Porque o commit é local até você executar o `git push` para o remoto correspondente.
