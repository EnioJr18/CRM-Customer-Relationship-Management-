# 🚀 CRM Portfolio - Sistema de Gestão de Clientes

Um sistema de Gestão de Relacionamento com o Cliente (CRM), o projeto simula uma aplicação real para gestão de leads, permitindo cadastro, acompanhamento de histórico e análise de métricas.

![Status do Projeto](https://shields.io/badge/Status-Active-success?logo=checkmarx&style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.13%2B-blue)
![Django](https://img.shields.io/badge/Django-5.x-green)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon-336791)

## 📋 Sobre o Projeto

Um sistema completo de **CRM (Customer Relationship Management)** desenvolvido para gerenciar o ciclo de vida de clientes, desde a captação (Lead) até o relacionamento contínuo. O sistema permite que vendedores cadastrem potenciais clientes (Leads), registrem interações (ligações, emails) e movam o cliente através de um funil de vendas.

Este projeto demonstra uma aplicação **Fullstack Python** robusta, saindo do ambiente de desenvolvimento local e indo para a produção na nuvem com banco de dados real.

---

### 🌐 Demo Online
Você pode testar o sistema funcionando em tempo real clicando no link abaixo:

👉 **[Acessar CRM Online (Render)](https://gestor-de-relacionamento-crm.onrender.com)**

*(Nota: Como o servidor é gratuito, pode levar alguns segundos para "acordar" no primeiro acesso).*

---

## 📸 Screenshots

<img width="640" height="610" alt="Image" src="https://github.com/user-attachments/assets/b3d6aac8-9bdb-4d24-a33a-8284ebed4fdf" /> 
<img width="640" height="610" alt="Image" src="https://github.com/user-attachments/assets/8759207a-b8a4-4eba-ab84-5126790135f1" />

---

## ⚡ Funcionalidades Principais

### 1. Gestão de Leads (CRUD)
- Cadastro completo de clientes com validação.
- Listagem inteligente com **paginação** e indicadores visuais de status.
- Edição e Exclusão segura (com confirmação).

### 2. Ferramentas de Negócio
- **Dashboard Gerencial:** Métricas em tempo real (Total de leads, distribuição por status e prioridade).
- **Timeline de Interações:** Histórico cronológico de conversas e notas para cada cliente.
- **Busca e Filtros:** Pesquisa por nome e filtros rápidos (Alta Prioridade, Recentes, Sem Interação).
- **Exportação:** Geração de relatórios em **CSV** para Excel.

### 3. Segurança e Infraestrutura
- **Autenticação:** Sistema de Login/Logout (acesso restrito).
- **Proteção:** CSRF Tokens e SQL Injection prevention (ORM Django).
- **Deploy:** Configurado com Gunicorn e WhiteNoise para alta performance de arquivos estáticos.

---

## 🛠️ Tech Stack

**Backend & Core**
- Python 3.11+
- Django 5 (MVT Architecture)
- Gunicorn (WSGI Server)

**Banco de Dados**
- PostgreSQL (Produção - Neon Tech)
- SQLite (Desenvolvimento Local)

**Frontend**
- HTML5 / CSS3
- Bootstrap 5 (Responsividade)
- Django Template Engine

**DevOps & Deploy**
- Render (Hospedagem)
- WhiteNoise (Gestão de arquivos estáticos)
- Git & GitHub

---

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
    SECRET_KEY=sua_chave_secreta
    DEBUG=True
    DATABASE_URL=postgres://usuario:senha@host-neon.tech/neondb?sslmode=require ou sqlite
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

8. **Acesse**
```bash
http://127.0.0.1:8000/
```

🗺️ Roadmap:

[ ]**Cadastro e Gestão de Usuários** <br>
[ ]**Melhoria na UI Design** <br>
[ ]**Interatividade** <br>
[ ]**Reestruturação do Código (Clean Code)** <br>

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
Desenvolvido por **Enio Jr** para fins de estudo e portfólio 💻

📧 Entre em contato: eniojr100@gmail.com <br>
🔗 LinkedIn: https://www.linkedin.com/in/enioeduardojr/ <br>
📷 Instagram: https://www.instagram.com/enio_juniorrr/ <br>
