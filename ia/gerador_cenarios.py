from ia.prompts import montar_prompt


def gerar_cenarios(requisito: str) -> dict:
    """
    Gera cenários estruturados a partir de um requisito.
    """

    prompt = montar_prompt(requisito)

    cenarios = [
        {
            "id": "CT001",
            "titulo": "Validar comportamento esperado do requisito",
            "categoria": "positivo",
            "pre_condicoes": ["Sistema disponível."],
            "passos": [
                "Acessar o sistema.",
                "Executar a funcionalidade descrita no requisito."
            ],
            "resultado_esperado": (
                "O sistema deve atender ao comportamento "
                "descrito no requisito."
            ),
            "prioridade": "Alta"
        },
        {
            "id": "CT002",
            "titulo": "Validar comportamento diante de entrada inválida",
            "categoria": "negativo",
            "pre_condicoes": ["Sistema disponível."],
            "passos": [
                "Acessar o sistema.",
                "Informar um dado inválido.",
                "Tentar executar a funcionalidade."
            ],
            "resultado_esperado": (
                "O sistema deve impedir a operação inválida."
            ),
            "prioridade": "Alta"
        },
        {
            "id": "CT003",
            "titulo": "Validar limites da funcionalidade",
            "categoria": "limite",
            "pre_condicoes": ["Sistema disponível."],
            "passos": [
                "Acessar o sistema.",
                "Executar a funcionalidade utilizando valores "
                "nos limites permitidos."
            ],
            "resultado_esperado": (
                "O sistema deve respeitar os limites definidos."
            ),
            "prioridade": "Média"
        }
    ]

    return {
        "requisito": requisito.strip(),
        "prompt": prompt,
        "total_cenarios": len(cenarios),
        "cenarios": cenarios
    }
