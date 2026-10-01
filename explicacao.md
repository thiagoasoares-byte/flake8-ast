E711 e E712 mostram que o Python prefere `is None`, `is True` e `is False` ou, na maioria dos casos, avaliar a expressão diretamente.
Isso evita comparações desnecessárias e deixa o código mais legível e idiomático.
O comentário `# noqa: F841` silencia apenas a variável temporária daquela linha, sem alterar a configuração global do projeto.
No plugin `flake8-pytest-style`, o erro PT018 indica uma asserção composta; por isso o teste foi simplificado para `assert realizar_login(...)`.