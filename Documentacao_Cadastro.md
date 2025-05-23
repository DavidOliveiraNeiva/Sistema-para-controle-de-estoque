# Projeto: Sistema para controle de estoque

## Visão Geral
o Projeto visa criar um softwa\re capaz de armazenas dados do estoque e manipular os valores atraves de entrada e saida de produtos.

## Tecnologias
- Frontend: QT Designer
- Backend: Python
- Banco de Dados: SQLiteStudeo
- Controle de Versão: Git + GitHub

### REQUISITOS FUNCIONAIS
    RF-01 – Cadastro de Produtos
    Descrição: o sistema deve permitir que o usuário cadastre novos produtos no estoque, informando nome, código do Produto, categoria, valor de custo
    (oculos Rayban, OC01, Oculos Premium, R$15,30)

    RF-02 – Entrada de Produtos
    Descrição: o sistema deve permitir que o usuário Registre as entradas de novos produtos no estoque, informando código do Produto, categoria, quantidade
    (OC01, Oculos Premium, 20)

    RF-03 – Saida de Produtos
    Descrição: o sistema deve permitir que o usuário  Registre as saidas de produtos no estoque, informando código do produto, quantidade

    RF-04 – Controle de Estoque Mínimo
    Descrição: o sistema deve gerar um alerta quando o estoque esta abaixo do limite minimo estipulado.

    RF-05 – Gerar relatório
    Descrição: o sistema deve gerar relatórios com as informações Estoque atual, Produtos que mais vendem, Historico de movimentações e exportar para PDF

    RF-06 – Busca e Filtros de Produtos
    Descrição: O sistema deve permitir filtrar as informações por código, categoria

### REQUISITOS NÃO FUNCIONAIS (qualidade do sistema)
    RNF01 – Interface simples e intuitiva.
    RNF02 – Responsividade (acesso em computador, tablet, celular).
    RNF03 – Segurança de dados (login, criptografia de senha).
    RNF04 – Boa performance mesmo com grande volume de dados.

### Diagrama de Casos de Uso
    Mostra os atores (usuários) e o que eles podem fazer no sistema.
    Feito em UML ou com ferramentas visuais como Draw.io, Lucidchart, etc.

### Modelagem de Dados (Banco de Dados)
    DER (Diagrama Entidade-Relacionamento): Representa tabelas, chaves, relacionamentos.
    Dicionário de dados: Define cada campo, tipo, tamanho, se é obrigatório, etc.

### Protótipo das Telas
    Simulações visuais da interface do sistema.
    Pode ser feito com Figma, Adobe XD, Balsamiq, ou até desenhado à mão.

### Fluxo de Navegação ou Fluxograma de Processos
    Mostra como o usuário vai navegar entre telas ou como os processos internos funcionam.
    Útil para validar se a lógica do sistema está clara e eficiente.

### Plano de Testes (opcional, mas recomendado)
    Descreve como você vai validar se o sistema funciona corretamente.
    Ex: Teste de cadastro de produto → Entrada: nome, preço, categoria → Esperado: produto salvo.

### Cronograma (se for projeto em equipe ou TCC)
    Datas previstas para cada fase: levantamento, modelagem, desenvolvimento, testes, entrega.

---

## Conexões/Funções
- **função `valor_produto_total()`** – chamada ao adionar o valor unitário
- **função `cadastrar_produto()`** – envia dados para o banco de dados
- **API_URL:** ``

## Tarefas da Sprint
 - [ ] Criar Banco de dados `Estoque.db`
    - [ ] Inserir campos de nome `text`, cod_produto `text`, categoria `text`, valor_custo `int` ao criar o banco de dados
        - Responsável: nenhum
        - Data Prazo: 26/05
        - Data Conclusão: -
        - Status: a fazer
 - [ ] Implantar Botão Salvar
    - [ ] salvar informações no banco dados
        - Responsável: nenhum
        - Data Prazo: 26/05
        - Data Conclusão: -
        - Status: a fazer
    - [ ] Implantar Botão Limpar (limpar campos na tela)
        - Responsável: nenhum
        - Data Prazo: 26/05
        - Data Conclusão: -
        - Status: a fazer

### Regras de Commit (Git)
- Commits claros: `adiciona botão de login`
- Um commit por funcionalidade
- Sempre descrever o que foi feito no Pull Request

### Como contribuir
1. Puxe a branch `Main`
2. Crie uma nova branch com seu nome e tarefa: `feature/tela-login`
3. Faça push e envie o Pull Request
