import pytest

from ia.gerador_cenarios import gerar_cenarios


def test_gerar_tres_cenarios():
    resultado = gerar_cenarios(
        "O sistema deve impedir pedidos com carrinho vazio."
    )

    assert resultado["total_cenarios"] == 3
    assert len(resultado["cenarios"]) == 3


def test_cenarios_contem_categorias_esperadas():
    resultado = gerar_cenarios(
        "O sistema deve permitir realizar pedidos."
    )

    categorias = [
        cenario["categoria"]
        for cenario in resultado["cenarios"]
    ]

    assert categorias == ["positivo", "negativo", "limite"]


def test_cenarios_contem_campos_obrigatorios():
    resultado = gerar_cenarios(
        "O sistema deve calcular o valor do pedido."
    )

    campos = [
        "id",
        "titulo",
        "categoria",
        "pre_condicoes",
        "passos",
        "resultado_esperado",
        "prioridade"
    ]

    for cenario in resultado["cenarios"]:
        for campo in campos:
            assert campo in cenario


def test_requisito_e_preservado():
    requisito = "O sistema deve validar o pagamento."

    resultado = gerar_cenarios(requisito)

    assert resultado["requisito"] == requisito
    assert requisito in resultado["prompt"]


def test_rejeitar_requisito_vazio():
    with pytest.raises(ValueError):
        gerar_cenarios("")


def test_rejeitar_valor_que_nao_seja_texto():
    with pytest.raises(TypeError):
        gerar_cenarios(123)
