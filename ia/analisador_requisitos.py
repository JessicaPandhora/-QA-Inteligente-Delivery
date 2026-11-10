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

    termos_encontrados = [
        termo for termo in termos_vagos
        if termo in requisito_minusculo
    ]

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
        "impedir",
        "possibilitar"
    ]

    possui_acao = any(
        palavra in requisito_minusculo.split()
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
