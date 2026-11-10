import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def pagina():
    with sync_playwright() as playwright:
        navegador = playwright.chromium.launch(headless=True)
        pagina = navegador.new_page()
        pagina.goto("http://127.0.0.1:8000")

        yield pagina

        navegador.close()


def test_pagina_delivery_abre_corretamente(pagina):
    assert pagina.locator("h1").inner_text() == "Delivery - QA Inteligente"


def test_carrinho_inicia_vazio_na_interface(pagina):
    assert pagina.locator("#quantidade").inner_text() == "0"
    assert pagina.locator("#total").inner_text() == "0.00"


def test_adicionar_produto_atualiza_carrinho(pagina):
    pagina.locator("#adicionar").click()

    assert pagina.locator("#quantidade").inner_text() == "1"
    assert pagina.locator("#total").inner_text() == "25.00"


def test_impedir_finalizacao_com_carrinho_vazio(pagina):
    pagina.locator("#finalizar").click()

    mensagem = pagina.locator("#mensagem").inner_text()

    assert mensagem == "Adicione um produto antes de finalizar."


def test_finalizar_pedido_com_produto(pagina):
    pagina.locator("#adicionar").click()
    pagina.locator("#finalizar").click()

    assert pagina.locator("#mensagem").inner_text() == "Pedido realizado com sucesso!"