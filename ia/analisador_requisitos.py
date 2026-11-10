import re


def analisar_requisito(requisito: str) -> dict:
    """
    Analisa um requisito e identifica possíveis ambiguidades
    ou informações que precisam ser esclarecidas.
    """

    if not isinstance(requisito, str):
        raise TypeError("O requisito deve ser um texto.")

    requisito = requisito.strip()

    if not requisito:
        raise ValueError("O requisito não pode estar vazio.")

    termos_vagos = [
        "rápido",
        "rapidamente",
        "fácil",
        "facilmente",
        "adequado",
        "intuitivo",
        "melhor",
        "muitos",
        "poucos",
        "alguns",
        "etc",
        "quando possível",
        "seguro"
    ]

    problemas = []
    recomendacoes = []

    requisito_minusculo = requisito.lower()

    termos_encontrados = []

    for termo in termos_vagos:
        partes = termo.split()
        padrao = r"(?<!\w)" + r"\s+".join(
            re.escape(parte) for parte in partes
        ) + r"(?!\w)"

        if re.search(padrao, requisito_minusculo):
            termos_encontrados.append(termo)

    if termos_encontrados:
        problemas.append(
            "O requisito contém termos vagos ou subjetivos: "
            + ", ".join(termos_encontrados)
        )
        recomendacoes.append(
            "Substituir os termos vagos por critérios objetivos e mensuráveis."
        )

    palavras_de_acao = [
        "deve",
        "deverá",
        "precisa",
        "permitir",
        "permite",
        "permitem",
        "impedir",
        "possibilitar"
    ]

    possui_acao = any(
        re.search(
            r"(?<!\w)" + re.escape(palavra) + r"(?!\w)",
            requisito_minusculo
        )
        for palavra in palavras_de_acao
    )

    if not possui_acao:
        problemas.append(
            "Não foi identificada uma ação ou obrigação claramente definida."
        )
        recomendacoes.append(
            "Descrever claramente o que o sistema deve fazer."
        )

    if len(requisito.split()) < 5:
        problemas.append(
            "O requisito apresenta poucas informações para uma análise completa."
        )
        recomendacoes.append(
            "Adicionar contexto, condições e resultados esperados."
        )

    expressoes_genericas = [
        "realizar pedidos",
        "efetuar operações",
        "processar solicitações",
        "gerenciar cadastros"
    ]

    possui_expressao_generica = any(
        expressao in requisito_minusculo
        for expressao in expressoes_genericas
    )

    possui_criterios = any(
        termo in requisito_minusculo
        for termo in [
            "quando",
            "desde que",
            "somente se",
            "com ",
            "sem ",
            "maior que",
            "menor que",
            "igual a",
            "mínimo",
            "máximo",
            "obrigatório"
        ]
    )

    if possui_expressao_generica and not possui_criterios:
        problemas.append(
            "O requisito não apresenta critérios verificáveis para orientar os testes."
        )
        recomendacoes.append(
            "Definir condições, dados obrigatórios, regras de negócio e resultados esperados."
        )

    if problemas:
        status = "necessita_revisao"
    else:
        status = "sem_problemas_identificados"

    return {
        "requisito": requisito,
        "status": status,
        "total_problemas": len(problemas),
        "problemas": problemas,
        "recomendacoes": recomendacoes
    }
