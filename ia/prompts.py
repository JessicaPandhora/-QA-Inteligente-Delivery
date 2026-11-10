def montar_prompt(requisito: str) -> str:
    """
    Prepara uma instrução estruturada para a IA gerar casos de teste.
    """

    if not isinstance(requisito, str):
        raise TypeError("O requisito deve ser um texto.")

    requisito = requisito.strip()

    if not requisito:
        raise ValueError("O requisito não pode estar vazio.")

    return f"""
Você é um profissional especialista em Quality Assurance (QA).

Analise cuidadosamente o requisito informado e elabore casos
de teste completos e objetivos.

REQUISITO:
{requisito}

Gere cenários das seguintes categorias:

1. Testes positivos: verificam comportamentos esperados.
2. Testes negativos: verificam situações inválidas ou erros.
3. Testes de limite: verificam valores mínimos, máximos e extremos.

Para cada caso de teste, informe:

- ID do teste
- Título
- Categoria
- Pré-condições
- Passos para execução
- Resultado esperado
- Prioridade (Alta, Média ou Baixa)

Não invente funcionalidades que não estejam fundamentadas
no requisito. Quando faltar informação, indique a dúvida.

Apresente o resultado de forma organizada e estruturada.
"""
