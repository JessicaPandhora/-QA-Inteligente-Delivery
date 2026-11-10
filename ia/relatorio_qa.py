from ia.analisador_requisitos import analisar_requisito
from ia.gerador_cenarios import gerar_cenarios


def gerar_relatorio_qa(requisito: str) -> dict:
    """
    Gera um relatório de QA com análise, cenários e validação.
    """

    analise = analisar_requisito(requisito)
    geracao = gerar_cenarios(requisito)

    validacao = geracao["validacao"]

    status_validacao = (
        "VALIDO" if validacao["valido"] else "INVALIDO"
    )

    resumo = {
        "status_requisito": analise["status"],
        "total_problemas": analise["total_problemas"],
        "total_cenarios": geracao["total_cenarios"],
        "total_erros_validacao": validacao["total_erros"],
        "status_validacao": status_validacao
    }

    linhas = [
        "RELATORIO DE QUALIDADE DE SOFTWARE",
        "=" * 40,
        "",
        "REQUISITO ANALISADO:",
        analise["requisito"],
        "",
        "ANALISE DO REQUISITO:",
        f"Status: {analise['status']}",
        f"Total de problemas: {analise['total_problemas']}",
        "",
        "PROBLEMAS IDENTIFICADOS:"
    ]

    if analise["problemas"]:
        for problema in analise["problemas"]:
            linhas.append(f"- {problema}")
    else:
        linhas.append("- Nenhum problema identificado.")

    linhas.extend([
        "",
        "RECOMENDACOES:"
    ])

    if analise["recomendacoes"]:
        for recomendacao in analise["recomendacoes"]:
            linhas.append(f"- {recomendacao}")
    else:
        linhas.append("- Nenhuma recomendacao necessária.")

    linhas.extend([
        "",
        "CENARIOS DE TESTE:"
    ])

    for cenario in geracao["cenarios"]:
        linhas.extend([
            "",
            f"ID: {cenario['id']}",
            f"Titulo: {cenario['titulo']}",
            f"Categoria: {cenario['categoria']}",
            f"Prioridade: {cenario['prioridade']}",
            f"Pre-condicoes: {', '.join(cenario['pre_condicoes'])}",
            f"Passos: {'; '.join(cenario['passos'])}",
            f"Resultado esperado: {cenario['resultado_esperado']}"
        ])

    linhas.extend([
        "",
        "VALIDACAO DOS CENARIOS:",
        f"Status: {status_validacao}",
        f"Total de erros: {validacao['total_erros']}"
    ])

    if validacao["erros"]:
        for erro in validacao["erros"]:
            linhas.append(f"- {erro}")
    else:
        linhas.append("- Nenhum erro encontrado.")

    linhas.extend([
        "",
        "RESUMO:",
        f"Problemas no requisito: {resumo['total_problemas']}",
        f"Cenarios gerados: {resumo['total_cenarios']}",
        f"Erros de validacao: {resumo['total_erros_validacao']}",
        f"Status da validacao: {resumo['status_validacao']}"
    ])

    return {
        "requisito": analise["requisito"],
        "analise": analise,
        "geracao": geracao,
        "resumo": resumo,
        "texto": "\n".join(linhas)
    }


def salvar_relatorio_txt(
    relatorio: dict,
    caminho: str = "relatorios/relatorio_qa.txt"
) -> str:
    """
    Salva o relatório de QA em um arquivo TXT.
    """

    from pathlib import Path

    if not isinstance(relatorio, dict):
        raise TypeError("O relatório deve ser um dicionário.")

    if not isinstance(relatorio.get("texto"), str):
        raise ValueError("O relatório não possui texto válido.")

    arquivo = Path(caminho)
    arquivo.parent.mkdir(parents=True, exist_ok=True)

    arquivo.write_text(relatorio["texto"], encoding="utf-8")

    return str(arquivo)


def salvar_relatorio_json(
    relatorio: dict,
    caminho: str = "relatorios/relatorio_qa.json"
) -> str:
    """
    Salva os dados estruturados do relatório em JSON.
    """

    import json
    from pathlib import Path

    if not isinstance(relatorio, dict):
        raise TypeError("O relatório deve ser um dicionário.")

    arquivo = Path(caminho)
    arquivo.parent.mkdir(parents=True, exist_ok=True)

    with arquivo.open("w", encoding="utf-8") as destino:
        json.dump(
            relatorio,
            destino,
            ensure_ascii=False,
            indent=4
        )

    return str(arquivo)
