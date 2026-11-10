import pytest

from ia.analisador_requisitos import analisar_requisito


def test_identificar_termo_vago():
    resultado = analisar_requisito(
        "O sistema deve responder rapidamente às solicitações dos usuários."
    )
    assert resultado["status"] == "necessita_revisao"
    assert resultado["total_problemas"] > 0
    assert any("rapidamente" in problema for problema in resultado["problemas"])


def test_identificar_requisito_sem_acao():
    resultado = analisar_requisito("Tela de cadastro de clientes")
    assert resultado["status"] == "necessita_revisao"
    assert any("ação" in problema for problema in resultado["problemas"])


def test_identificar_requisito_curto():
    resultado = analisar_requisito("O sistema deve cadastrar.")
    assert resultado["status"] == "necessita_revisao"
    assert any("poucas informações" in problema for problema in resultado["problemas"])


def test_requisito_sem_problemas_identificados():
    resultado = analisar_requisito(
        "O sistema deve bloquear pedidos com carrinho vazio."
    )
    assert resultado["status"] == "sem_problemas_identificados"
    assert resultado["total_problemas"] == 0


def test_rejeitar_requisito_vazio():
    with pytest.raises(ValueError):
        analisar_requisito("")


def test_rejeitar_valor_que_nao_seja_texto():
    with pytest.raises(TypeError):
        analisar_requisito(123)


def test_nao_identificar_termo_vago_dentro_de_outra_palavra():
    resultado = analisar_requisito(
        "O sistema deve identificar usuários com acesso inseguro."
    )

    assert resultado["status"] == "sem_problemas_identificados"
    assert not any(
        "seguro" in problema
        for problema in resultado["problemas"]
    )


def test_identificar_expressao_vaga_com_mais_de_uma_palavra():
    resultado = analisar_requisito(
        "O sistema deve realizar a validação quando possível."
    )

    assert resultado["status"] == "necessita_revisao"
    assert any(
        "quando possível" in problema
        for problema in resultado["problemas"]
    )


def test_identificar_termo_vago_sem_diferenciar_maiusculas():
    resultado = analisar_requisito(
        "O sistema deve responder RAPIDAMENTE às solicitações."
    )

    assert resultado["status"] == "necessita_revisao"
    assert any(
        "rapidamente" in problema
        for problema in resultado["problemas"]
    )


def test_identificar_acao_com_pontuacao():
    resultado = analisar_requisito(
        "O sistema deve: validar o pagamento realizado pelo usuário."
    )

    assert resultado["status"] == "sem_problemas_identificados"


def test_reconhecer_verbo_permite_como_acao():
    resultado = analisar_requisito(
        "A funcionalidade permite acesso ao cadastro de clientes."
    )

    assert not any(
        "ação" in problema
        for problema in resultado["problemas"]
    )


def test_identificar_requisito_sem_criterios_verificaveis():
    resultado = analisar_requisito(
        "O sistema deve permitir realizar pedidos."
    )

    assert resultado["status"] == "necessita_revisao"
    assert any(
        "critérios" in problema.lower()
        for problema in resultado["problemas"]
    )
