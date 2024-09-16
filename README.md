

# CRUD DJANGO


## Instruções de Instalação

Siga os passos abaixo para clonar o projeto e configurá-lo em sua máquina local.

### 1. Clonar o Repositório

Execute o comando abaixo para clonar o repositório do GitHub:

```bash
git clone https://github.com/JefersonQueiroga/projeto-django-crud
```

### 2. Criar e Ativar o Ambiente Virtual

Navegue até o diretório do projeto e crie um ambiente virtual:

```bash
cd seu-projeto
python -m venv venv
```

Ative o ambiente virtual:

- **No Windows:**

  ```bash
  venv\Scripts\activate
  ```

- **No Linux/macOS:**

  ```bash
  source venv/bin/activate
  ```

### 3. Instalar Dependências

Com o ambiente virtual ativado, instale as dependências do projeto utilizando o arquivo `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 4. Rodar Migrações

Aplique as migrações para configurar o banco de dados:

```bash
python manage.py migrate
```

### 5. Executar o Servidor

Agora você pode rodar a aplicação:

```bash
python manage.py runserver
```

### 6. Acessar a Aplicação

Abra o navegador e acesse:

```
http://localhost:8000
