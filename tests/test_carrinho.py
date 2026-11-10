import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture
def pagina():
    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=True)
        pagina = navegador.new_page()

        pagina.set_content("""
        <!DOCTYPE html>
        <html lang="pt-BR">
        <body>
            <h1>Delivery QA</h1>

            <h2>Hambúrguer - R$ 29,90</h2>
            <button onclick="adicionar()">Adicionar ao carrinho</button>

            <p>Quantidade: <span id="quantidade">0</span></p>
            <p>Total: <span id="total">R$ 0,00</span></p>

            <button onclick="finalizar()">Finalizar pedido</button>
            <p id="mensagem"></p>

            <script>
                let quantidade = 0;

                function adicionar() {
                    quantidade++;
                    document.getElementById("quantidade").textContent = quantidade;

                    let valor = quantidade * 2990;
                    document.getElementById("total").textContent =
                        "R$ " + (valor / 100).toFixed(2).replace(".", ",");
                }

                function finalizar() {
                    if (quantidade === 0) {
                        document.getElementById("mensagem").textContent =
                            "Adicione um produto antes de finalizar.";
                    } else {
                        document.getElementById("mensagem").textContent =
                            "Pedido realizado com sucesso!";
                    }
                }
            </script>
        </body>
        </html>
        """)

        yield pagina
        navegador.close()


def test_carrinho_inicia_vazio(pagina):
    assert pagina.locator("#quantidade").inner_text() == "0"
    assert pagina.locator("#total").inner_text() == "R$ 0,00"


def test_adicionar_produto(pagina):
    pagina.get_by_role("button", name="Adicionar ao carrinho").click()

    assert pagina.locator("#quantidade").inner_text() == "1"
    assert pagina.locator("#total").inner_text() == "R$ 29,90"


def test_calcular_total_de_dois_produtos(pagina):
    botao = pagina.get_by_role("button", name="Adicionar ao carrinho")

    botao.click()
    botao.click()

    assert pagina.locator("#quantidade").inner_text() == "2"
    assert pagina.locator("#total").inner_text() == "R$ 59,80"


def test_impedir_pedido_com_carrinho_vazio(pagina):
    pagina.get_by_role("button", name="Finalizar pedido").click()

    assert pagina.locator("#mensagem").inner_text() == (
        "Adicione um produto antes de finalizar."
    )


def test_finalizar_pedido_com_produto(pagina):
    pagina.get_by_role("button", name="Adicionar ao carrinho").click()
    pagina.get_by_role("button", name="Finalizar pedido").click()

    assert pagina.locator("#mensagem").inner_text() == (
        "Pedido realizado com sucesso!"
    )
