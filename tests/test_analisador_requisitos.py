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
