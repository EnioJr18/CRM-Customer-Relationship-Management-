# 🚀 CRM.Pro - Sistema de Gestão de Clientes

![Python](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-5.0-092E20?style=for-the-badge&logo=django&logoColor=white)
![Bootstrap](https://img.shields.io/badge/Bootstrap-5-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![Status](https://img.shields.io/badge/Status-Em_Desenvolvimento-yellow?style=for-the-badge)

Um sistema de CRM (Customer Relationship Management) moderno e seguro, desenvolvido com **Django**. O projeto foca em oferecer uma interface elegante (Dark Mode) e isolamento de dados por usuário, funcionando como um SaaS (Software as a Service).

---

## 📸 Screenshots
<img width="520" height="500" alt="Image" src="https://github.com/user-attachments/assets/a907f830-2330-45ff-a3a9-9c33509efaf3" /> 
<img width="520" height="500" alt="Image" src="https://github.com/user-attachments/assets/65099e52-2fae-49d9-9268-e5cc5d0b9f87" />
<img width="520" height="500" alt="Image" src="https://github.com/user-attachments/assets/c050143b-c194-4e3f-b905-1f8a4d7c6625" />

## ✨ Funcionalidades Principais

- **🔐 Autenticação Segura:** Sistema completo de Login, Cadastro e Recuperação de Senha.
- **🛡️ Multi-Tenant (Isolamento de Dados):** Cada usuário vê apenas os seus próprios leads. Acesso cruzado é bloqueado.
- **🌑 UI/UX Moderna:** Interface responsiva com tema **Dark/Cyberpunk**, Sidebar fixa e componentes Bootstrap customizados.
- **📊 Dashboard Interativo:** Visão geral com KPIs (Total de Vendas, Novos Clientes, Pedidos do Dia).
- **📝 Gestão de Leads (CRUD):**
  - Cadastro detalhado (Nome, Contato, Status, Prioridade).
  - Histórico de interações (Timeline de anotações).
  - Edição e Exclusão segura.
  - Busca e Filtros: Pesquisa por nome e filtros rápidos (Alta Prioridade, Recentes, Sem Interação).
  - Listagem inteligente com **paginação** e indicadores visuais de status.
- **⚙️ Perfil de Usuário:** Área para atualização de dados cadastrais.
- **Exportação:** Geração de relatórios em **CSV** para Excel.
- **Deploy:** Configurado com Gunicorn e WhiteNoise para alta performance de arquivos estáticos.

## 🛠️ Tecnologias Utilizadas

- **Back-end e Core:** Python, Django Framework.
- **Front-end:** HTML5, CSS3, Bootstrap 5 (com customização CSS via Variáveis).
- **Banco de Dados:** SQLite (Desenvolvimento) / PostgreSQL (Planejado para Produção).
- **Ícones:** Bootstrap Icons.
- **DevOps & Deploy:** Render (Hospedagem), WhiteNoise (Gestão de arquivos estáticos) e Git & GitHub.

### 🌐 Demo Online
Você pode testar o sistema funcionando em tempo real clicando no link abaixo:

👉 **[Acessar CRM Online (Render)](https://gestor-de-relacionamento-crm.onrender.com)**

*(Nota: Como o servidor é gratuito, pode levar alguns segundos para "acordar" no primeiro acesso).*

---

## 🚀 Como rodar o projeto localmente

### Pré-requisitos
* Python instalado
* Conta no Neon (ou PostgreSQL local)

### Passo a Passo

1.  **Clone o repositório**
    ```bash
    git clone https://github.com/EnioJr18/Gestor-de-Clientes-CRM.git
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
    python manage.py makemigrations
    python manage.py migrate
    ```

6.  **Crie um Superusuário (para acessar o Admin, opcional)**
    ```bash
    python manage.py createsuperuser
    ```

7.  **Inicie o servidor**
    ```bash
    python manage.py runserver
    ```

8. **Acesse**
http://127.0.0.1:8000/


🗺️ Roadmap:

* [ ] Visualização de Dados: Implementar gráficos com Chart.js.
* [ ] Automação: Envio de e-mails automáticos para novos leads.7

## 🤝 Contribuição
Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.

---
Desenvolvido por **Enio Jr** para fins de estudo e portfólio 💻

📧 Entre em contato: eniojr100@gmail.com <br>
🔗 LinkedIn: https://www.linkedin.com/in/enioeduardojr/ <br>
📷 Instagram: https://www.instagram.com/enio_juniorrr/ <br>
