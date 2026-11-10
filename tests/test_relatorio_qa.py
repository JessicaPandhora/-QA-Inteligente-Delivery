import pytest

from ia.relatorio_qa import gerar_relatorio_qa


def test_relatorio_retorna_estrutura_esperada():
    relatorio = gerar_relatorio_qa(
        "O sistema deve permitir realizar pedidos."
    )

    assert "requisito" in relatorio
    assert "analise" in relatorio
    assert "geracao" in relatorio
    assert "resumo" in relatorio
    assert "texto" in relatorio


def test_relatorio_apresenta_resumo_correto():
    relatorio = gerar_relatorio_qa(
        "O sistema deve permitir realizar pedidos."
    )

    resumo = relatorio["resumo"]

    assert resumo["total_problemas"] == 1
    assert resumo["total_cenarios"] == 3
    assert resumo["total_erros_validacao"] == 0
    assert resumo["status_validacao"] == "VALIDO"


def test_texto_contem_cenarios_e_status_da_validacao():
    relatorio = gerar_relatorio_qa(
        "O sistema deve permitir realizar pedidos."
    )

    texto = relatorio["texto"]

    assert "RELATORIO DE QUALIDADE DE SOFTWARE" in texto
    assert "O sistema deve permitir realizar pedidos." in texto
    assert "CT001" in texto
    assert "CT002" in texto
    assert "CT003" in texto
    assert "Status: VALIDO" in texto


def test_relatorio_identifica_requisito_vago():
    relatorio = gerar_relatorio_qa(
        "O sistema deve funcionar rapidamente."
    )

    assert relatorio["analise"]["total_problemas"] > 0
    assert relatorio["analise"]["recomendacoes"]


def test_rejeitar_requisito_vazio():
    with pytest.raises(ValueError):
        gerar_relatorio_qa("   ")


def test_rejeitar_requisito_que_nao_seja_texto():
    with pytest.raises(TypeError):
        gerar_relatorio_qa(123)


def test_exportar_relatorio_txt(tmp_path):
    from ia.relatorio_qa import (
        gerar_relatorio_qa,
        salvar_relatorio_txt
    )

    relatorio = gerar_relatorio_qa(
        "O sistema deve permitir realizar pedidos."
    )

    caminho = tmp_path / "evidencias" / "relatorio.txt"

    arquivo = salvar_relatorio_txt(relatorio, str(caminho))

    assert caminho.exists()
    assert arquivo == str(caminho)
    assert "RELATORIO DE QUALIDADE DE SOFTWARE" in caminho.read_text(
        encoding="utf-8"
    )


def test_exportar_relatorio_json(tmp_path):
    import json

    from ia.relatorio_qa import (
        gerar_relatorio_qa,
        salvar_relatorio_json
    )

    relatorio = gerar_relatorio_qa(
        "O sistema deve permitir realizar pedidos."
    )

    caminho = tmp_path / "evidencias" / "relatorio.json"

    arquivo = salvar_relatorio_json(relatorio, str(caminho))

    dados = json.loads(caminho.read_text(encoding="utf-8"))

    assert caminho.exists()
    assert arquivo == str(caminho)
    assert dados["resumo"]["total_cenarios"] == 3
    assert dados["resumo"]["status_validacao"] == "VALIDO"


def test_exportacao_txt_rejeita_relatorio_invalido():
    from ia.relatorio_qa import salvar_relatorio_txt

    with pytest.raises(TypeError):
        salvar_relatorio_txt("relatorio inválido")


def test_exportacao_json_rejeita_relatorio_invalido():
    from ia.relatorio_qa import salvar_relatorio_json

    with pytest.raises(TypeError):
        salvar_relatorio_json("relatorio inválido")
