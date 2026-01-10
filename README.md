# 🚀 Django Sales CRM

Um sistema de Gestão de Relacionamento com o Cliente (CRM) desenvolvido para organizar leads, histórico de interações e pipeline de vendas.

![Status do Projeto](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow)
![Python](https://img.shields.io/badge/Python-3.13%2B-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon-336791)

## 📋 Sobre o Projeto

Este projeto faz parte do meu portfólio de desenvolvimento Backend. O objetivo é criar uma solução robusta utilizando a arquitetura **MVT (Model-View-Template)** do Django, demonstrando boas práticas de engenharia de software, segurança e modelagem de dados.

O sistema permite que vendedores cadastrem potenciais clientes (Leads), registrem interações (ligações, emails) e movam o cliente através de um funil de vendas.

## 🛠 Tecnologias Utilizadas

* **Backend:** Python 3, Django Framework
* **Banco de Dados:** PostgreSQL (Hospedado na nuvem via **Neon Tech**)
* **Gerenciamento de Dependências:** Pip / Virtualenv
* **Variáveis de Ambiente:** Python-dotenv
* **Driver de Banco:** Psycopg2

## ⚙️ Arquitetura e Modelagem

O projeto segue o padrão MVC (MVT no Django):
* **Models:** Definição rigorosa de tipos de dados, chaves estrangeiras (`ForeignKey`) e integridade referencial.
* **Views (Controller):** (Em desenvolvimento) Lógica de negócios e controle de fluxo.
* **Templates (View):** (Em desenvolvimento) Interface do usuário.

### Estrutura do Banco de Dados Principal
* **Lead:** Armazena dados do cliente, status do funil (`choices`) e prioridade.
* **Interaction:** Tabela relacionada (1:N) que mantém o histórico de contatos com cada cliente.

## 🚀 Como rodar o projeto localmente

### Pré-requisitos
* Python instalado
* Conta no Neon (ou PostgreSQL local)

### Passo a Passo

1.  **Clone o repositório**
    ```bash
    git clone https://github.com/EnioJr18/CRM-Customer-Relationship-Management-.git
    cd crm-portfolio
    ```

2.  **Crie e ative o ambiente virtual**
    ```bash
    # Windows
    python -m venv venv
    venv\Scripts\activate

    # Linux/Mac
    source venv/bin/activate
    ```

3.  **Instale as dependências**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Configure as Variáveis de Ambiente**
    Crie um arquivo `.env` na raiz do projeto e adicione a URL do seu banco de dados:
    ```env
    DATABASE_URL=postgres://usuario:senha@host-neon.tech/neondb?sslmode=require #(Exemplo)
    ```

5.  **Execute as Migrations**
    ```bash
    python manage.py migrate
    ```

6.  **Crie um Superusuário (para acessar o Admin)**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Inicie o servidor**
    ```bash
    python manage.py runserver
    ```

## 🔜 Próximos Passos (Roadmap)

- [x] Configuração do Ambiente e Banco de Dados (Neon)
- [x] Modelagem de Dados (Leads e Interações)
- [x] Customização do Django Admin
- [ ] Criação das Views (Dashboard e Listagem)
- [ ] Implementação de Templates com Bootstrap/Tailwind
- [ ] Exportação de Relatórios (CSV/PDF)

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
Desenvolvido por **Enio Jr** 💻

📧 Entre em contato: eniojr100@gmail.com <br>
🔗 LinkedIn: https://www.linkedin.com/in/enioeduardojr/ <br>
📷 Instagram: https://www.instagram.com/enio_juniorrr/ <br>