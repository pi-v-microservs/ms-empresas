# MS-Empresas 
## Microserviço de gerenciamento de empresas da plataforma BAE Brasil

## 1. Instalação e Execução do Servidor Flask:
Importante: pressupõe-se o uso de gerenciadores de pacote e de ambientes virtuais como ```pip``` 
e ```venv```, respectivamente ou ```pipenv```.

### 1.1. Instalação das dependências:
```shell
pip install -r requirements.txt
```

### 1.2. Inicialização do banco de dados:
No diretório ```/src/api``` executar o comando:
```shell
flask init_db
```

### 1.3. Inicialização da aplicação:
No diretório ```/src/api``` executar o comando:
```shell
flask run
```

## 2. Endpoints Disponíveis:
### 2.1. Empresas:

> **GET** <br>
> **Listar** todas as empresas: ```/empresas/list``` <br>
> **Buscar** por id_empresa: ```/empresas/get``` <br>

> **POST** <br>
> **Criar** novo: ```/empresas/create``` <br>

> **PUT** <br>
> **Atualizar** existente por id_empresa: ```/empresas/update``` <br>

> **DELETE** <br>
> **Deletar** existente por id_empresa: ```/empresas/delete```

### 2.2. Vagas:
> **GET** <br>
> **Listar** todas as vagas de um empresa por id_empresa: ```/vagas/list``` <br>
> **Buscar** por id_vaga: ```/vagas/get``` <br>

> **POST** <br>
> **Criar** novo: ```/vagas/create``` <br>

> **PUT** <br>
> **Atualizar** existente por id_vaga: ```/vagas/update``` <br>

> **DELETE** <br>
> **Deletar** existente por id_vaga: ```/vagas/delete```

### 2.3. Vagas Candidatos:

> **GET** <br>
> **Listar** todas vagas candidatos de um empresa por id_vaga: ```/vagas_candidatos/list``` <br>
> **Buscar** por id_vaga_candidato: ```/vagas_candidatos/get``` <br>

> **POST** <br>
> **Criar** novo: ```/vagas_candidatos/create``` <br>

> **PUT** <br>
> **Atualizar** existente por id_vaga_candidato: ```/vagas_candidatos/update``` <br>

> **DELETE** <br>
> **Deletar** existente por id_vaga_candidato: ```/vagas_candidatos/delete```
