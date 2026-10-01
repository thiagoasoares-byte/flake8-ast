# Desafio Flake8 e Qualidade de Código

Este projeto demonstra a refatoração de um teste legado com foco em qualidade de código, regras do Flake8 e uso do plugin `flake8-pytest-style`.

## Arquivos principais

- `test_login.py`: script refatorado para seguir boas práticas do Python e passar no lint.
- `.flake8`: configuração do Flake8 com `max-line-length = 100`, `max-complexity = 3` e exclusão de diretórios de cache e ambientes virtuais.
- `explicacao.md`: resumo curto sobre os erros E711, E712 e o plugin de Pytest.

## Como executar

1. Instale as dependências:

```powershell
python -m pip install flake8 flake8-pytest-style
```

2. Rode a validação na raiz do projeto:

```powershell
python -m flake8 .
```

## Resultado esperado

O comando acima deve executar sem retornar mensagens de erro.

## Observações

- A variável `token_sessao` foi mantida com `# noqa: F841` apenas na linha em que aparece.
- O teste foi ajustado para evitar uma asserção composta apontada pelo `flake8-pytest-style`.