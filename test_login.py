def _motivo_falha(usuario, senha, forcar_erro):
    verificacoes = [
        (not usuario, "Usuario invalido"),
        (senha is None, "Senha vazia"),
        (forcar_erro, "Erro forcado"),
    ]
    for falhou, mensagem in verificacoes:
        if falhou:
            return mensagem
    return None


def realizar_login(usuario, senha, forcar_erro):
    motivo = _motivo_falha(usuario, senha, forcar_erro)
    if motivo:
        print(motivo)
        return False

    print(
        "Iniciando o processo de login no sistema com credenciais validas "
        "e aguardando o tempo de resposta do servidor..."
    )
    return True


def test_verificar_login_valido():
    token_sessao = "abc123xyz"  # noqa: F841
    assert realizar_login(True, "123456", False)
