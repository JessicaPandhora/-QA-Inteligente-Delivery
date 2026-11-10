import pytest

from ia.gerador_cenarios import gerar_cenarios
from ia.validador_cenarios import validar_cenarios


def test_validar_cenarios_gerados_corretamente():
    resultado = gerar_cenarios(
        "O sistema deve permitir realizar pedidos."
    )

    validacao = validar_cenarios(resultado)

    assert validacao["valido"] is True
    assert validacao["total_erros"] == 0
    assert validacao["erros"] == []


def test_rejeitar_resultado_que_nao_seja_dicionario():
    with pytest.raises(TypeError):
        validar_cenarios("resultado inválido")


def test_identificar_campo_obrigatorio_ausente():
    resultado = gerar_cenarios(
        "O sistema deve validar o pagamento."
    )

    del resultado["cenarios"][0]["titulo"]

    validacao = validar_cenarios(resultado)

    assert validacao["valido"] is False
    assert any("titulo" in erro for erro in validacao["erros"])


def test_identificar_ids_duplicados():
    resultado = gerar_cenarios(
        "O sistema deve permitir realizar pedidos."
    )

    resultado["cenarios"][1]["id"] = resultado["cenarios"][0]["id"]

    validacao = validar_cenarios(resultado)

    assert validacao["valido"] is False
    assert any("ID duplicado" in erro for erro in validacao["erros"])


def test_identificar_categoria_invalida():
    resultado = gerar_cenarios(
        "O sistema deve permitir realizar pedidos."
    )

    resultado["cenarios"][0]["categoria"] = "inexistente"

    validacao = validar_cenarios(resultado)

    assert validacao["valido"] is False
    assert any("categoria inválida" in erro for erro in validacao["erros"])


def test_identificar_prioridade_invalida():
    resultado = gerar_cenarios(
        "O sistema deve permitir realizar pedidos."
    )

    resultado["cenarios"][0]["prioridade"] = "Urgente"

    validacao = validar_cenarios(resultado)

    assert validacao["valido"] is False
    assert any("prioridade inválida" in erro for erro in validacao["erros"])


def test_identificar_total_de_cenarios_incorreto():
    resultado = gerar_cenarios(
        "O sistema deve permitir realizar pedidos."
    )

    resultado["total_cenarios"] = 10

    validacao = validar_cenarios(resultado)

    assert validacao["valido"] is False
    assert any("total informado" in erro for erro in validacao["erros"])
