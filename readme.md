# 📚 API de Reserva de Salas

Este repositório contém a **API de Reserva de Salas**, desenvolvida com **Flask** e **SQLAlchemy**, como parte de uma arquitetura baseada em **microsserviços**.

## 🧩 Arquitetura

A API de Reserva de Salas é um **microsserviço** que faz parte de um sistema maior de [Gerenciamento Escolar](https://github.com/gabmacedo/schoolSystem_API.git)
, sendo responsável exclusivamente pelo gerenciamento das reservas de salas por turma.

⚠️ **Esta API depende de outra API de Gerenciamento Escolar (School System)**, que deve estar em execução e exposta localmente. A comunicação entre os serviços ocorre via **requisições HTTP REST**, para validar:

- Se a **Turma** existe (`GET /turmas/<id>`)

---

## 🚀 Tecnologias Utilizadas

- Python 3.x
- Flask
- SQLAlchemy
- SQLite (como banco de dados local)
- Requests (para consumo da API externa)

---

## ▶️ Como Executar a API

### 1. Clone o repositório

```bash
git clone https://github.com/gabmacedo/reserva-de-sala-api.git
cd reserva-api
```

### 2. Crie um ambiente virtual (opcional, mas recomendado)

```bash
python3 -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate     # Windows
```

### 3. Instale as dependências

```bash
pip install -r requirements.txt
```

### 4. Execute a API

```bash
python app.py
```

A aplicação estará disponível em:
📍 `http://localhost:5000`

📝 **Observação:** O banco de dados é criado automaticamente na primeira execução.

---

## 📡 Endpoints Principais

- `GET /reservas` – Lista todas as reservas
- `POST /reservas` – Cria uma nova reserva
- `GET /reservas/<id>` – Detalha uma reserva
- `DELETE /reservas/<id>` – Remove uma reserva

### Exemplo de corpo JSON para criação:

```json
{
  "turma_id": 1,
  "sala": "101",
  "data": "2025-05-06"
}
```

---

## 🔗 Dependência Externa

Certifique-se de que a **API de Gerenciamento Escolar** esteja rodando em:

```
http://localhost:5050
```

E que o endpoint de `GET /turmas/<id>` estejam funcionando corretamente para que a validação seja feita com sucesso.

---

## 📦 Estrutura do Projeto

```
reserva-api/
├── controller/
│   └──reserva_controller.py
├── instance/
│   └──reservas.db
├── models/
│   └──reserva_model.py
├── routes/
│   └──reserva_route.py
├── app.py
├── config.py
├── database.py
├── dockerfile
├── requirements.txt
└── README.md
```

---

## 🛠️ Futuras Melhorias

- Validação de conflito de horário na sala
- Integração via fila (RabbitMQ) com outros microsserviços
- Autenticação de usuários

---

## 🧑‍💻 Autores

- [Gabriel Aparecido de Macedo](https://github.com/gabmacedo) | RA: 2401541  
- [Guilherme Eduardo Moraes Pecorari](https://github.com/GuilhermePecorari) | RA: 2400086  
- [Davi de Moraes Bizerra](https://github.com/Davibizerra) | RA: 2401072
