from ia.prompts import montar_prompt


def test_gerar_prompt_com_requisito_valido():
    requisito = "O sistema deve impedir pedidos com carrinho vazio."

    resultado = montar_prompt(requisito)

    assert isinstance(resultado, str)
    assert requisito in resultado


def test_prompt_contem_categorias_de_testes():
    resultado = montar_prompt("O usuário deve conseguir realizar um pedido.")

    assert "Testes positivos" in resultado
    assert "Testes negativos" in resultado
    assert "Testes de limite" in resultado


def test_prompt_contem_estrutura_dos_casos_de_teste():
    resultado = montar_prompt("O sistema deve calcular o valor do pedido.")

    assert "ID do teste" in resultado
    assert "Pré-condições" in resultado
    assert "Resultado esperado" in resultado
    assert "Prioridade" in resultado


def test_rejeitar_requisito_vazio():
    try:
        montar_prompt("")
        assert False, "Deveria rejeitar requisito vazio."
    except ValueError:
        pass


def test_rejeitar_valor_que_nao_seja_texto():
    try:
        montar_prompt(123)
        assert False, "Deveria rejeitar valores que não sejam texto."
    except TypeError:
        pass
