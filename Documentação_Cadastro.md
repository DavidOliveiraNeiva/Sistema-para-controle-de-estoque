# Projeto: Sistema para controle de estoque

## Visão Geral
o Projeto visa criar um softwa\re capaz de armazenas dados do estoque e manipular os valores atraves de entrada e saida de produtos.

## Tecnologias
- Frontend: QT Designer
- Backend: Python
- Banco de Dados: SQLiteStudeo
- Controle de Versão: Git + GitHub




## Telas


### Tela Inicial
-Campos
    - Nome
    - Quantidade
    - Valor Unitário
    - Tipo Unitário
    - 

- Botões:
    - Cadastrar
    - Limpar

## Funcionalidades
| Item          | Descrição                                   | Status       |
|---------------|---------------------------------------------|--------------|
| Tela inicial  | Criação da UI com botões e layout base      | Pronto |
| Cadastro      | Formulário de novo Produto                  | A fazer      |
| Integração    | Conexão com API ou banco de dados           | A fazer      |

---

## Conexões/Funções
- **função `valor_produto_total()`** – chamada ao adionar o valor unitário
- **função `cadastrar_produto()`** – envia dados para o banco de dados
- **API_URL:** ``

---

## Tarefas da Sprint (Semana 1)
| Tarefa                            | Responsável | Prazo     | Data Conclusão | Status       |
|-----------------------------------|-------------|-----------|----------------|--------------|
| Montar tela inicial (sem lógica)  | David       | 20/05     | 20/05          | Feito        |
| Criar função valor_produto_total  | David       | 26/05     | ---            | Em andamento |
| Documentar API                    | Você        | 25/05     | ---            | A fazer      |
| Integrar botão "Entrar"           | Fulano      | 26/05     | ---            | A fazer      |

---

## Regras de Commit (Git)
- Commits claros: `feat: adiciona botão de login`
- Um commit por funcionalidade
- Sempre descrever o que foi feito no PR

---

## Como contribuir
1. Puxe a branch `develop`
2. Crie uma nova branch com seu nome e tarefa: `feature/tela-login`
3. Faça push e envie o PR



---

## Telas

### Tela Inicial (`UI_ProjSysCtrlEstoque.ui`)
- Botões:
  - [ ] Cadastrar
  - [ ] Limpar

---

## Funcionalidades

| ID  | Funcionalidade             | Descrição                                               | Status     |
|-----|----------------------------|----------------------------------------------------------|------------|
| F01 | Conectar botão "Entrar"    | Chamar função `fazer_login()` no backend                | A fazer    |
| F02 | Conectar botão "Cadastrar" | Chamar função `cadastrar_usuario()`                     | A fazer    |
| F03 | Esqueci senha              | Abrir nova janela de recuperação                        | A fazer    |
| F04 | Sair                       | Fechar o programa                                       | A fazer    |

---

## Backend - Conexões e Lógica

### `login.py`
```python
def fazer_login(usuario: str, senha: str) -> bool:
    """
    Valida login do usuário.
    Retorna True se o login for válido, False caso contrário.
    """





