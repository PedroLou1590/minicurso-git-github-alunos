# Guia de contribuição — regras do minicurso

Nosso objetivo é simular uma contribuição profissional, mas em um projeto pequeno e acessível.

## 1. Branch

Formato obrigatório:

```text
fix/nome-sobrenome-modulo
```

Exemplos:

```text
fix/ana-silva-soma
fix/joao-souza-paridade
```

Regras: letras minúsculas, sem acentos, palavras separadas por hífen. Cada aluno deve usar seu próprio nome para evitar colisões. Se o trabalho for em dupla, use o nome de um responsável.

## 2. Commit — Conventional Commits simplificado

Formato obrigatório:

```text
fix(modulo): descricao curta da correcao
```

Exemplos:

```text
fix(soma): corrige a adicao de dois numeros
fix(concatenacao): preserva a ordem dos textos
fix(paridade): corrige a verificacao de pares
```

`fix` identifica uma correção de erro; `modulo` indica o arquivo da tarefa; a descrição resume **o que mudou**. Evite mensagens como `arrumei`, `teste`, `final` ou `alteracoes`.

> O projeto usa uma adaptação didática de Conventional Commits: https://www.conventionalcommits.org/pt-br/v1.0.0/

## 3. Título da Pull Request

Formato obrigatório:

```text
fix(modulo): descricao curta — Nome Sobrenome
```

Exemplo:

```text
fix(soma): corrige a adicao de dois numeros — Ana Silva
```

## 4. Corpo da Pull Request

Preencha o modelo automático do GitHub: problema encontrado, como resolveu, comando de teste e checklist.

## 5. Regras de escopo

- Modifique apenas o arquivo designado (inclusive o novo doctest).
- Não apague os doctests existentes para fazer os testes passarem.
- Não force um `push` para `main`.
- Faça `git status` e `git diff` antes do commit.
- Não inclua arquivos temporários, `__pycache__` ou informações pessoais/senhas.
- Não faça merge da própria PR sem autorização dos instrutores.

## 6. Checklist para revisão

- A solução corrige o comportamento descrito?
- O doctest do arquivo passa integralmente?
- Há um novo caso de teste útil?
- A branch, o commit e a PR seguem os formatos obrigatórios?
- A descrição da PR deixa claro o que foi corrigido?
