# Urban Routes Automation Suite

Este projeto implementa uma suíte completa de **testes automatizados** para a aplicação web [Urban Routes](https://urbanroutes.com), utilizando **Python**, **Selenium WebDriver** e **Pytest**. O objetivo é simular e validar a experiência do usuário ao utilizar o serviço de transporte da plataforma.

---

## 📁 Estrutura de Arquivos

```
.
├── data.py               # Dados de entrada e configurações
├── helpers.py            # Funções auxiliares
├── main.py               # Casos de teste automatizados
├── pages.py              # Page Object Model (POM)
└── README.md             # Documentação do projeto
```

---

## 🚗 Funcionalidades Testadas

Cada teste automatiza uma ação que um usuário real faria no site:

| Teste                              | Descrição                                                                 |
|-----------------------------------|---------------------------------------------------------------------------|
| `test_define_route`               | Define endereço de origem e destino no campo de busca                     |
| `test_choose_support_plan`        | Seleciona o plano de tarifa "Suporte"                                     |
| `test_register_phone`             | Insere o número de telefone e confirma com o código recebido              |
| `test_fill_card_details`          | Preenche e valida os dados de um cartão de crédito                        |
| `test_write_driver_message`       | Escreve uma mensagem personalizada para o motorista                       |
| `test_toggle_blanket`             | Ativa a opção de conforto (ex: cobertores e lençóis)                      |
| `test_add_ice_creams`             | Adiciona potes de sorvete ao pedido (quantidade enumerável)              |
| `test_place_order`                | Solicita o táxi e verifica se o pop-up de confirmação é exibido          |

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.9+**
- **Selenium WebDriver**
- **Pytest**
- **ChromeDriver**

---

## ▶️ Como Executar os Testes

1. Clone o repositório:
   ```bash
   git clone https://github.com/seuusuario/urban-routes-automation-suite.git
   cd urban-routes-automation-suite
   ```

2. Instale as dependências (recomenda-se o uso de `venv`):
   ```bash
   pip install -r requirements.txt
   ```

3. Execute os testes:
   ```bash
   pytest main.py -s
   ```

---

## 🧪 Observações

- Os testes estão configurados para rodar em **modo headless** (sem abrir o navegador).
- O código de verificação do telefone está **mockado** via função auxiliar `retrieve_phone_code()`.
- Você pode modificar os dados em `data.py` para testar diferentes cenários.
