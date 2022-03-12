## CRUD_NoSQL_rest

- [Descrição](#descrição)
- [Instalação](#instalação)
- [Utilização](#utilização)
- [Termos de uso](#termos-de-uso)

<br>

# Descrição

<p><b>CRUD_NoSQL_rest</b> consiste numa aplicação que realiza operações CRUD para publicações de um blog.</p>
<p>Esta aplicação utiliza a linguagem Python, o microframework Flask e a biblioteca Pymongo e está organizada em arquitetura MVC utilizando o padrão de projeto Factory.</p>

<br>

# Instalação

<h5>0. Primeiramente, é necessário já ter instalado na própria máquina:</h5>

- <p> Um <b>editor de código</b>, conhecido também como <b>IDE</b>. Por exemplo, o <b>[Visual Studio Code (VSCode)](https://code.visualstudio.com/)</b>.</p>

- <p> Uma <b>ferramenta cliente de API REST</b>. Por exemplo, o <b>[Insomnia](https://insomnia.rest/download)</b> ou o <b>[Postman](https://www.postman.com/product/rest-client/)</b>.</p>

- <p> E versionar o diretório para receber o clone da aplicação:</p>

```
git init
```

<br>
<h5>1. Fazer o clone do reposítório <span style="text-decoration: underline">CRUD_NoSQL_rest</span> na sua máquina pelo terminal do computador ou pelo do IDE:</h5>

```
git clone git@gitlab.com:ABKURA/crud-nosql-rest.git
```

<p>Entrar na pasta criada:</p>

```
cd crud-nosql-rest
```

<h5>1. O arquivo oculto <b>.env</b> com o comando:</h5>

```
touch .env
```

dentro do arquivo .env configurar os seguintes comandos:

```
FLASK_ENV=development

```

<b>Obs:</b> as informações contidas no arquivo <b>.env</b> não devem ser compartilhadas. O arquivo já consta no <b>.gitignore</b> para não ser subido no repositório.


<h5>2. O ambiente virtual e atualizar suas dependências com o seguinte comando:</h5>

```
python -m venv venv --upgrade-deps
```

ative o seu ambiente virtual com o comando:

```
source/venv/bin/activate
```

<h5>3. recursivamente as dependências do projeto com o comando:</h5>

```
pip install -r requirements.txt
```


# Utilização

<p>Antes de passarmos para o API Client precisamos rodar o CLI</p>

```
flask run
```

<p>A aplicação rodará com o <b>http://127.0.0.1:5000/</b>. Adicionar depois deste as rotas e suas terminações, ou <b>endpoints</b>, que veremos a seguir.</p>

<p>Após o CLI rodar de modo bem sucedido com o API Client aberto vamos utilizar as seguintes rotas:</p>

<h3>Rotas</h3>

<h4>Cadastro</h4>

Cadastro de usuários (Método POST): <b>/post</b> (ou http://127.0.0.1:5000/post)

Exemplo a ser colocado no body da requisição:

```
{
	"title": "Something",
	"author": "Something's author",
	"content": "Something's content",
	"tags": "Something's tag"
}
```

E a resposta esperada:

```
Status: 201 CREATED
```

```
{
  "author": "Something's author",
  "content": "Something's content",
  "created_at": "12/03/2022 03:04:38 AM",
  "id": 1,
  "tags": "Something's tag",
  "title": "Something"
}
```

Caso falte algum item no body da requisição:

```
{
	"title": "Something",
	"author": "Something's author",
	"content": "Something's content"
}
```

A resposta esperada deverá ser:

```
Status: 400 BAD REQUEST
```

```
{
    "message": "JSON incompleto! Verifique se sua requisição está completa e se suas keys escritas corretamente."
}
```

<h4>Listagem de usuários</h4>

Listagem dos usuários cadastrados (Método GET): <b>/post</b> (ou http://127.0.0.1:5000/post)

Exemplo a ser colocado no body da requisição:

```
(Requisição feita sem body)
```

E a resposta esperada:

```
Status: 200 OK
```

```
[
  {
    "author": "Something's author",
    "content": "Something's content",
    "created_at": "12/03/2022 03:04:38 AM",
    "id": 1,
    "tags": "Something's tag",
    "title": "Something"
  }
]
```
  
<h4>Listagem de usuário por id</h4>

Listagem dos usuários cadastrados (Método GET): <b>/post/id**</b> (ou http://127.0.0.1:5000/post/id**)

\*\*preencher com o id do usuário anteriormente cadastrado.

Exemplo a ser colocado no body da requisição:

```
(Requisição feita sem body)
```

E a resposta esperada:

```
Status: 200 OK
```

```
{
  "author": "Something's author",
  "content": "Something's content",
  "created_at": "12/03/2022 03:04:38 AM",
  "id": 1,
  "tags": "Something's tag",
  "title": "Something"
}
```

  Caso o <b>id</b> no query não exista no banco de dados a resposta esperada deverá ser:

```
Status: 404 NOT FOUND
```

```
{
    "message": "Não encontrado ou inexistente!"
}
```

<h4>Atualização de usuário por id:</h4>

Atualização de dados do usuário cadastrado (Método PATCH): <b>/users/id**</b> (ou http://127.0.0.1:5000/users/id**)

\*\*preencher com o id do usuário anteriormente cadastrado.

Exemplo a ser colocado no body da requisição:

```
{
	"title": "Somesomething"
}
```

E a resposta esperada:

```
Status: 201 CREATED
```

```
{
  "author": "Something's author",
  "content": "Something's content",
  "created_at": "12/03/2022 03:04:38 AM",
  "id": 1,
  "tags": "Something's tag",
  "title": "Somesomething",
  "updated_at": "12/03/2022 03:17:08 AM"
}
```

<h4>Deleção de usuário por id:</h4>

Deleção de dados do usuário cadastrado (Método DELETE): <b>/users/id**</b> (ou http://127.0.0.1:5000/users/id**)

\*\*preencher com o id do usuário anteriormente cadastrado.

Exemplo a ser colocado no body da requisição:

```
(Requisição feita sem body)
```

E a resposta esperada:

```
Status: 200 OK
```

```
[
  {
    "author": "Something's author",
    "content": "Something's content",
    "created_at": "12/03/2022 03:04:38 AM",
    "id": 1,
    "tags": "Something's tag",
    "title": "Somesomething"
  }
]
```
  
# Termos de uso

<p>Esta aplicação atende a fins exclusivamente didáticos e não possui qualquer intuito comercial.</p>
