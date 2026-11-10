# Documentação do Uso de Inteligência Artificial no Projeto QA Inteligente

## 1. Introdução

Este documento apresenta a aplicação da Inteligência Artificial como ferramenta de apoio ao desenvolvimento do projeto QA Inteligente — Automação de Testes com IA.

O projeto tem como objetivo explorar recursos de Quality Assurance (QA), incluindo testes funcionais, automação de interfaces, análise de requisitos, elaboração de prompts e geração estruturada de cenários de testes.

A aplicação utilizada como base é uma simulação web de delivery, desenvolvida em HTML e JavaScript.

## 2. Aplicação da Inteligência Artificial

O ChatGPT foi utilizado como ferramenta de apoio ao processo de aprendizagem e desenvolvimento do projeto.

Sua utilização envolveu:

- Apoio na elaboração de cenários de testes.
- Sugestões para organização dos casos de teste.
- Auxílio na estruturação dos scripts em Python.
- Orientação sobre utilização do Pytest.
- Apoio na implementação dos testes de interface com Playwright.
- Estruturação de prompts para atividades de QA.
- Desenvolvimento de regras para análise de requisitos.
- Apoio na geração estruturada de cenários de testes.
- Análise dos resultados das execuções.
- Organização e elaboração da documentação técnica.

A implementação, execução e conferência dos testes foram realizadas no ambiente de desenvolvimento.

Nesta versão, os módulos de análise e geração utilizam lógica e regras implementadas em Python. A integração com um modelo de IA generativa por API está prevista para uma etapa posterior.

## 3. Módulos desenvolvidos

### 3.1 Testes funcionais do carrinho

Arquivo: tests/test_carrinho.py

Foram implementados cinco testes:

1. Verificar se o carrinho inicia vazio.
2. Validar a adição de produtos.
3. Verificar o cálculo do total de dois produtos.
4. Impedir pedidos com o carrinho vazio.
5. Validar a finalização de pedidos com produtos.

### 3.2 Testes de interface

Arquivo: tests/test_interface_delivery.py

Foram implementados cinco testes:

1. Verificar se a página Delivery abre corretamente.
2. Validar se o carrinho inicia vazio na interface.
3. Verificar se a adição de produtos atualiza quantidade e total.
4. Validar a mensagem apresentada ao tentar finalizar um carrinho vazio.
5. Verificar a finalização de pedidos com produtos.

Os testes utilizam Playwright e Chromium para simular interações de usuários com a aplicação web.

### 3.3 Módulo de criação de prompts

Arquivo: ia/prompts.py

Responsável por estruturar instruções utilizadas como base para atividades de QA.

O módulo contempla:

- Recebimento e validação de requisitos.
- Organização das categorias de testes.
- Estruturação dos elementos necessários aos casos de teste.
- Preparação de instruções para apoiar a geração de cenários.

### 3.4 Módulo de geração de cenários

Arquivo: ia/gerador_cenarios.py

Responsável pela geração estruturada de três categorias de cenários:

- Positivo.
- Negativo.
- Limite.

Os cenários possuem campos como:

- Identificador.
- Título.
- Categoria.
- Pré-condições.
- Passos.
- Resultado esperado.
- Prioridade.

Nesta versão, a geração utiliza regras implementadas em Python.

### 3.5 Módulo de análise de requisitos

Arquivo: ia/analisador_requisitos.py

Responsável pela análise inicial de requisitos, identificando possíveis problemas de clareza e especificação.

O módulo verifica:

- Presença de termos vagos ou subjetivos.
- Ausência de ação claramente definida.
- Requisitos com poucas informações.
- Necessidade de recomendações para melhorar a objetividade.

O resultado apresenta o requisito analisado, seu status, a quantidade de problemas encontrados, os problemas identificados e as recomendações correspondentes.

A análise é baseada em regras programadas em Python, não em interpretação realizada por um modelo generativo.

## 4. Testes automatizados e resultados

Os testes foram implementados com Pytest e organizados em cinco arquivos.

### 4.1 Distribuição dos testes

| Arquivo | Quantidade |
|---|---:|
| tests/test_carrinho.py | 5 |
| tests/test_interface_delivery.py | 5 |
| tests/test_prompts.py | 5 |
| tests/test_gerador_cenarios.py | 6 |
| tests/test_analisador_requisitos.py | 6 |
| Total | 27 |

### 4.2 Resultado da execução completa

Na execução realizada em 10/11/2026, foram obtidos os seguintes resultados:

- Total de testes executados: 27.
- Testes aprovados: 27.
- Testes reprovados: 0.
- Resultado apresentado pelo Pytest: 27 passed.
- Tempo de execução: 7,35 segundos.

O resultado demonstra que os 27 testes implementados foram aprovados na execução registrada.

A evidência completa está armazenada em:

evidencias/execucao_completa_pytest.txt

## 5. Ferramentas e tecnologias utilizadas

- ChatGPT: apoio à elaboração, revisão e análise dos testes.
- Python: linguagem utilizada nos módulos e scripts.
- Pytest: execução e validação dos testes automatizados.
- Playwright: automação de interações com a interface web.
- Chromium: navegador utilizado nos testes de interface.
- HTML5 e JavaScript: tecnologias da aplicação simulada.
- GitHub Codespaces: ambiente de desenvolvimento em nuvem.
- Git e GitHub: controle de versão e armazenamento do projeto.

## 6. Considerações sobre o uso da IA

A utilização da Inteligência Artificial contribuiu para a organização e o desenvolvimento das atividades de Quality Assurance.

O projeto permitiu explorar como ferramentas de IA podem apoiar a elaboração de cenários, a estruturação de prompts, a análise de requisitos e a documentação técnica.

Entretanto, é importante diferenciar os recursos já implementados das funcionalidades planejadas. Os módulos atuais de análise e geração utilizam regras em Python, enquanto a integração com IA generativa ainda não foi implementada.

A execução dos testes automatizados permanece fundamental para verificar os comportamentos implementados e identificar possíveis falhas.

## 7. Próximas etapas de evolução

### Nível 2 — Inteligência aplicada ao QA

- Ampliar a análise de requisitos.
- Melhorar a identificação de ambiguidades.
- Evoluir a estruturação de prompts.
- Ampliar a geração de cenários.
- Aumentar a cobertura dos testes automatizados.

### Nível 3 — Integração com IA generativa

- Integrar um modelo de IA por meio de API.
- Enviar requisitos para análise pelo modelo.
- Gerar casos de teste dinamicamente.
- Validar e revisar os cenários produzidos.
- Desenvolver relatórios automatizados com apoio da IA.

## 8. Status do projeto

Em desenvolvimento.

Projeto desenvolvido para fins de estudo, prática profissional e construção de portfólio em Quality Assurance.
