from ia.validador_cenarios import validar_cenarios
import re

from ia.prompts import montar_prompt


def identificar_contexto(requisito: str) -> str:
    """Identifica o contexto principal do requisito."""

    texto = requisito.lower()

    contextos = {
        "login": [
            "login", "autenticação", "autenticar",
            "senha", "credencial", "usuário"
        ],
        "pagamento": [
            "pagamento", "pagar", "pagamento",
            "transação", "cartão", "cobrança"
        ],
        "carrinho": [
            "carrinho", "produto", "quantidade",
            "adicionar ao carrinho", "remover do carrinho"
        ],
        "pedido": [
            "pedido", "pedidos", "encomenda"
        ]
    }

    for contexto, palavras in contextos.items():
        for palavra in palavras:
            if re.search(
                r"(?<!\w)" + re.escape(palavra) + r"(?!\w)",
                texto
            ):
                return contexto

    return "geral"


def gerar_cenarios(requisito: str) -> dict:
    """
    Gera três cenários de teste adaptados ao contexto do requisito.
    A geração utiliza regras locais, sem API externa.
    """

    prompt = montar_prompt(requisito)
    contexto = identificar_contexto(requisito)

    modelos = {
        "login": [
            (
                "Validar autenticação com credenciais válidas",
                [
                    "Acessar a tela de login.",
                    "Informar credenciais válidas.",
                    "Solicitar autenticação."
                ],
                "O sistema deve processar a autenticação conforme o requisito.",
                "Alta"
            ),
            (
                "Validar autenticação com credenciais inválidas",
                [
                    "Acessar a tela de login.",
                    "Informar credenciais inválidas.",
                    "Solicitar autenticação."
                ],
                "O sistema deve tratar a tentativa inválida sem conceder acesso indevido.",
                "Alta"
            ),
            (
                "Validar campos de autenticação vazios",
                [
                    "Acessar a tela de login.",
                    "Deixar os campos de autenticação vazios.",
                    "Tentar realizar o login."
                ],
                "O sistema deve tratar corretamente o envio de campos vazios.",
                "Média"
            )
        ],
        "pagamento": [
            (
                "Validar processamento de pagamento",
                [
                    "Acessar a funcionalidade de pagamento.",
                    "Informar os dados necessários.",
                    "Solicitar o processamento."
                ],
                "O sistema deve processar o pagamento conforme as regras do requisito.",
                "Alta"
            ),
            (
                "Validar tentativa de pagamento inválida",
                [
                    "Acessar a funcionalidade de pagamento.",
                    "Informar dados inválidos.",
                    "Tentar processar o pagamento."
                ],
                "O sistema deve impedir ou tratar adequadamente a operação inválida.",
                "Alta"
            ),
            (
                "Validar valores nos limites do pagamento",
                [
                    "Acessar a funcionalidade de pagamento.",
                    "Informar valores nos limites permitidos.",
                    "Solicitar o processamento."
                ],
                "O sistema deve respeitar os limites de valores definidos.",
                "Média"
            )
        ],
        "carrinho": [
            (
                "Validar inclusão de produto no carrinho",
                [
                    "Acessar a lista de produtos.",
                    "Selecionar um produto.",
                    "Adicionar o produto ao carrinho."
                ],
                "O sistema deve incluir o produto no carrinho conforme o requisito.",
                "Alta"
            ),
            (
                "Validar operação inválida no carrinho",
                [
                    "Acessar o carrinho.",
                    "Tentar realizar uma operação com dados inválidos.",
                    "Verificar o comportamento apresentado."
                ],
                "O sistema deve tratar a operação inválida sem comprometer o carrinho.",
                "Alta"
            ),
            (
                "Validar limites de quantidade no carrinho",
                [
                    "Acessar o carrinho.",
                    "Informar quantidades nos limites permitidos.",
                    "Verificar o resultado da operação."
                ],
                "O sistema deve respeitar os limites de quantidade definidos.",
                "Média"
            )
        ],
        "pedido": [
            (
                "Validar realização de pedido",
                [
                    "Acessar a funcionalidade de pedidos.",
                    "Informar os dados necessários.",
                    "Solicitar a realização do pedido."
                ],
                "O sistema deve processar o pedido conforme o requisito.",
                "Alta"
            ),
            (
                "Validar tentativa de pedido inválido",
                [
                    "Acessar a funcionalidade de pedidos.",
                    "Informar dados inválidos ou incompletos.",
                    "Tentar realizar o pedido."
                ],
                "O sistema deve tratar adequadamente os dados inválidos.",
                "Alta"
            ),
            (
                "Validar limites na realização de pedidos",
                [
                    "Acessar a funcionalidade de pedidos.",
                    "Utilizar valores nos limites permitidos.",
                    "Verificar o resultado da operação."
                ],
                "O sistema deve respeitar os limites definidos para o pedido.",
                "Média"
            )
        ],
        "geral": [
            (
                "Validar comportamento esperado do requisito",
                [
                    "Acessar o sistema.",
                    "Executar a funcionalidade descrita no requisito."
                ],
                "O sistema deve atender ao comportamento descrito no requisito.",
                "Alta"
            ),
            (
                "Validar comportamento diante de entrada inválida",
                [
                    "Acessar o sistema.",
                    "Informar um dado inválido.",
                    "Tentar executar a funcionalidade."
                ],
                "O sistema deve impedir ou tratar a operação inválida.",
                "Alta"
            ),
            (
                "Validar limites da funcionalidade",
                [
                    "Acessar o sistema.",
                    "Executar a funcionalidade utilizando valores nos limites permitidos."
                ],
                "O sistema deve respeitar os limites definidos.",
                "Média"
            )
        ]
    }

    modelos_selecionados = modelos[contexto]

    categorias = ["positivo", "negativo", "limite"]
    cenarios = []

    for indice, modelo in enumerate(modelos_selecionados):
        titulo, passos, resultado_esperado, prioridade = modelo

        cenarios.append({
            "id": f"CT00{indice + 1}",
            "titulo": titulo,
            "categoria": categorias[indice],
            "pre_condicoes": ["Sistema disponível."],
            "passos": passos,
            "resultado_esperado": resultado_esperado,
            "prioridade": prioridade
        })

    resultado = {
        "requisito": requisito.strip(),
        "prompt": prompt,
        "total_cenarios": len(cenarios),
        "cenarios": cenarios
    }

    resultado["validacao"] = validar_cenarios(resultado)

    return resultado
