
# Documentação do Uso de Inteligência Artificial no Projeto QA Inteligente

## 1. Introdução

Este documento apresenta como a Inteligência Artificial foi utilizada como ferramenta de apoio durante o desenvolvimento do projeto QA Inteligente — Automação de Testes com IA.

O objetivo é explorar a aplicação da IA nas atividades de Quality Assurance (QA), especialmente na elaboração de cenários de testes, estruturação de scripts, revisão de validações, automação de interfaces e documentação técnica.

## 2. Aplicação da Inteligência Artificial

O ChatGPT foi utilizado como ferramenta de apoio ao processo de aprendizagem e desenvolvimento do projeto.

Sua utilização envolveu:

- Apoio na elaboração dos cenários de testes.
- Sugestões para organização dos casos de teste.
- Auxílio na estruturação dos scripts em Python.
- Orientação sobre utilização do Pytest.
- Apoio na implementação dos testes de interface com Playwright.
- Análise dos resultados apresentados durante as execuções.
- Revisão e aprimoramento das validações.
- Organização e elaboração da documentação técnica.

A Inteligência Artificial foi utilizada como recurso de apoio, enquanto a implementação, execução e conferência dos resultados foram realizadas no ambiente de desenvolvimento.

## 3. Cenários de testes desenvolvidos

O projeto utiliza uma aplicação web simulada de delivery, desenvolvida em HTML e JavaScript, para validar funcionalidades de um carrinho de compras.

Foram implementados dez testes automatizados, divididos em duas categorias.

### 3.1 Testes de lógica com Pytest

Arquivo: tests/test_carrinho.py

1. Verificar se o carrinho inicia vazio.
2. Validar a adição de produtos.
3. Verificar o cálculo do total de dois produtos.
4. Verificar se o sistema impede pedidos com o carrinho vazio.
5. Validar a finalização de pedidos com produtos.

### 3.2 Testes de interface com Playwright

Arquivo: tests/test_interface_delivery.py

1. Verificar se a página Delivery abre corretamente.
2. Validar se o carrinho inicia vazio na interface.
3. Verificar se a adição de produtos atualiza a quantidade e o total.
4. Validar a mensagem apresentada ao tentar finalizar um carrinho vazio.
5. Verificar a finalização de pedidos com produtos.

Os testes de interface utilizam o navegador Chromium para simular interações de usuários com a aplicação web.

## 4. Validação e resultados

Após a implementação dos scripts, os testes foram executados utilizando Pytest no ambiente GitHub Codespaces.

Na última execução registrada, foram obtidos os seguintes resultados:

- Total de testes executados: 10.
- Testes aprovados: 10.
- Testes reprovados: 0.
- Tempo de execução: 8,02 segundos.
- Resultado apresentado pelo Pytest: 10 passed.

Os resultados demonstram que todos os cenários implementados foram aprovados na execução registrada.

A saída completa foi armazenada no arquivo:

evidencias/execucao_completa_pytest.txt

## 5. Ferramentas utilizadas

- ChatGPT: apoio na elaboração, revisão e análise dos testes.
- Python: linguagem utilizada nos scripts.
- Pytest: execução e validação dos testes automatizados.
- Playwright: automação de interações com a interface web.
- Chromium: navegador utilizado na execução dos testes de interface.
- HTML5 e JavaScript: tecnologias utilizadas na aplicação simulada.
- GitHub Codespaces: ambiente de desenvolvimento em nuvem.
- Git e GitHub: controle de versão e armazenamento do projeto.

## 6. Considerações finais

O desenvolvimento do projeto permitiu explorar a aplicação da Inteligência Artificial como ferramenta de apoio às atividades de Quality Assurance.

A experiência envolveu a elaboração de cenários de testes, implementação de scripts automatizados, validação de funcionalidades e automação de interações com uma aplicação web.

A combinação de Python, Pytest e Playwright possibilitou trabalhar com diferentes níveis de validação, abrangendo tanto a lógica das funcionalidades quanto o comportamento da interface.

O projeto permanece em desenvolvimento e poderá receber novos cenários, melhorias, funcionalidades e experimentos relacionados à automação de testes e à aplicação da Inteligência Artificial em QA.
