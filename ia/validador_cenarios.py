def validar_cenarios(resultado: dict) -> dict:
    """
    Valida a estrutura e a consistência de um conjunto de cenários.
    """

    if not isinstance(resultado, dict):
        raise TypeError("O resultado deve ser um dicionário.")

    erros = []

    if not isinstance(resultado.get("requisito"), str) or not resultado["requisito"].strip():
        erros.append("O requisito deve ser um texto preenchido.")

    if not isinstance(resultado.get("prompt"), str) or not resultado["prompt"].strip():
        erros.append("O prompt deve ser um texto preenchido.")

    cenarios = resultado.get("cenarios")

    if not isinstance(cenarios, list):
        erros.append("A lista de cenários está ausente ou possui formato inválido.")
        cenarios = []

    total_informado = resultado.get("total_cenarios")

    if (
        not isinstance(total_informado, int)
        or isinstance(total_informado, bool)
    ):
        erros.append("O total de cenários deve ser um número inteiro.")
    elif total_informado != len(cenarios):
        erros.append("O total informado não corresponde à quantidade de cenários.")

    if not cenarios:
        erros.append("É necessário informar pelo menos um cenário.")

    campos_obrigatorios = [
        "id",
        "titulo",
        "categoria",
        "pre_condicoes",
        "passos",
        "resultado_esperado",
        "prioridade"
    ]

    categorias_validas = ["positivo", "negativo", "limite"]
    prioridades_validas = ["Alta", "Média", "Baixa"]
    ids_encontrados = set()

    for indice, cenario in enumerate(cenarios, start=1):
        identificacao = f"Cenário {indice}"

        if not isinstance(cenario, dict):
            erros.append(f"{identificacao}: deve ser um dicionário.")
            continue

        for campo in campos_obrigatorios:
            if campo not in cenario:
                erros.append(f"{identificacao}: campo obrigatório ausente: {campo}.")

        identificador = cenario.get("id")

        if not isinstance(identificador, str) or not identificador.strip():
            erros.append(f"{identificacao}: ID inválido.")
        elif identificador in ids_encontrados:
            erros.append(f"{identificacao}: ID duplicado: {identificador}.")
        else:
            ids_encontrados.add(identificador)

        for campo in ["titulo", "resultado_esperado"]:
            valor = cenario.get(campo)

            if not isinstance(valor, str) or not valor.strip():
                erros.append(f"{identificacao}: {campo} deve ser um texto preenchido.")

        categoria = cenario.get("categoria")

        if categoria not in categorias_validas:
            erros.append(f"{identificacao}: categoria inválida.")

        prioridade = cenario.get("prioridade")

        if prioridade not in prioridades_validas:
            erros.append(f"{identificacao}: prioridade inválida.")

        for campo in ["pre_condicoes", "passos"]:
            valores = cenario.get(campo)

            if (
                not isinstance(valores, list)
                or not valores
                or any(
                    not isinstance(valor, str) or not valor.strip()
                    for valor in valores
                )
            ):
                erros.append(
                    f"{identificacao}: {campo} deve conter uma lista "
                    "com textos preenchidos."
                )

    return {
        "valido": len(erros) == 0,
        "total_erros": len(erros),
        "erros": erros
    }
