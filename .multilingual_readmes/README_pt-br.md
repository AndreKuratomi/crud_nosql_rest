# crud_nosql_rest

- [Traduções](#traduções)
- [Sobre](#sobre)
- [Links](#links)
- [Instalação](#instalação)
- [Documentação](#documentação)
- [Referências](#referências)

<br>

## Traduções

- [English / Inglês](https://github.com/AndreKuratomi/crud_nosql_rest)
- [Português brasileiro](./README_pt-br.md)

<br>

## Sobre

<b>crud_nosql_rest</b> consiste numa aplicação que simula operações CRUD para publicações de um blog.

Esta aplicação utiliza a linguagem <strong>[Python](https://www.python.org/downloads/)</strong>, seu microframework <strong>[Flask](https://flask.palletsprojects.com/en/3.0.x/)</strong>, a biblioteca <strong>[PyMongo](https://pypi.org/project/pymongo/)</strong>, o banco de dados NoSQL<strong>[MongoDB](https://www.mongodb.com/)</strong>, e o software <strong>[Docker](https://docs.docker.com/)</strong> para fornecer tanto <b>Python</b> quanto <b>MongoDB</b>.

<br>

## Instalação

<h3>0. Primeiramente, é necessário já ter instalado na própria máquina:</h3>

- O versionador de codigo <b>[Git](https://git-scm.com/downloads)</b>,

- Um <b>editor de código</b>, conhecido também como <b>IDE</b>. Por exemplo, o <b>[Visual Studio Code (VSCode)](https://code.visualstudio.com/)</b>,

- O software <b>[Docker](https://docs.docker.com/)</b>,

- Uma <b>ferramenta cliente de API REST</b>. Por exemplo, o <b>[Insomnia](https://insomnia.rest/download)</b> ou o <b>[Postman](https://www.postman.com/product/rest-client/)</b>,

- <p> E versionar o diretório para receber o clone da aplicação:</p>

```
git init
```

<b>Obs:</b> Tanto <b>Python</b> quanto <b>MongoDb</b> não são exigidos para esta aplicação porque eles já são fornecidos pelo <b>Docker</b>.

<br>

<h3>1. Fazer o clone do reposítório <b>crud_nosql_rest</b> na sua máquina pelo terminal do computador ou pelo do IDE:</h3>

```
git clone https://github.com/AndreKuratomi/crud_nosql_rest.git
```

WINDOWS:

Obs: Caso apareca algum erro semelhante a este: 

```
unable to access 'https://github.com/AndreKuratomi/crud_nosql_rest.git': SSL certificate problem: self-signed certificate in certificate chain
```

Configure o git para desabilitar a certificação SSL:

```
git config --global http.sslVerify "false"
```


<p>Entrar na pasta criada:</p>

```
cd crud_nosql_rest
```
<br>

<h3>2. Após feito o clone do repositório, instalar:</h3>

<h4>O ambiente virtual* e atualizar suas dependências com o seguinte comando:</h4>

LINUX:
```
python3 -m venv venv --upgrade-deps
```

WINDOWS:
```
py -m venv venv --upgrade-deps
```

Caso seja retornado algum erro semelhante a este basta seguir as instruções:

```
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.
```

*É interessante seguir esta prática porque diferentes projetos exigem diferentes dependências. Um ambiente virtual nada mais é do que um ambiente separado da sua máquina. Caso contrário, a máquina do usuário pode se encher de dependências que serão utilizadas apenas em um único projeto.

<h4>Ative o seu ambiente virtual com o comando:</h4>

LINUX:
```
source/venv/bin/activate
```

WINDOWS:

No sistema operacional Windows é necessário antes configurar o Execution Policy do PowerShell:

```
Get-ExecutionPolicy # para verificar o tipo de política de execução
Set-ExecutionPolicy RemoteSigned # para alterar o tipo de política se o comando acima mostrar 'Restricted'
```
Obs: Eventualmente, pode ser necessário abrir o PowerShell como administrador.

```
.\venv\Scripts\activate
```


<h4>Instalar suas dependências:</h4>

```
pip install -r requirements.txt
```

WINDOWS:

Caso seja retornado algum erro semelhante a este:

```
ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\Users\\andre.kuratomi\\OneDrive - Company\\Área de Trabalho\\crud_nosql_rest\\crud_nosql_rest\\env\\Lib\\site-packages\\jedi\\third_party\\django-stubs\\django-stubs\\contrib\\contenttypes\\management\\commands\\remove_stale_contenttypes.pyi'
HINT: This error might have occurred since this system does not have Windows Long Path support enabled. You can find information on how to enable this at https://pip.pypa.io/warnings/enable-long-paths
```

Rode no cmd como adminstrador o seguinte comando:

```
reg.exe add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1 /f
```
<br>

<h3>3. Abrir a aplicação no IDE:</h3>

```
code .
```

<br>

<h3>4. Feitas as instalações precisamos criar nosso arquivo de variáveis de ambiente, o <b>.env</b>, no diretório raiz:</h3>

```
touch .env
```

Dentro dele precisamos definir nossas variáveis de ambiente tendo como base o arquivo <b>.env.example</b>:

```
FLASK_ENV=flask_env
MONGO_CLIENT=some_client
MONGO_URI=mongo_uri
```

<b>Obs:</b> as informações contidas no arquivo <b>.env</b> não devem ser compartilhadas. O arquivo já consta no <b>.gitignore</b> para não constar no repositório.

<h3>4. E executá-la:</h3>

LINUX e WINDOWS:
```
flask run
```

<br>

<h3>6. Executar dockerfile*:</h3>

LINUX e WINDOWS:
```
docker compose build
```

<br>

<h3>7. Executar docker compose*:</h3>

LINUX e WINDOWS:
```
docker compose up
```

<br>

*Para configurar docker com o usuário na máquina utilizar o seguinte comando:

```
sudo usermod -aG docker $USER
```

A variável $USER pode ser obtida com o seguinte comando (Linux):

```
whoami
```

<br>

## Documentação

Para ter acesso às descrições, detalhes das rotas e seus retornos, conferir documentação completa neste [link](https://insomnia-odwtdahxh-abkuras-projects.vercel.app/).

<br>

## Referências

- [Docker](https://docs.docker.com/)
- [Dotenv](https://www.npmjs.com/package/dotenv)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Insomnia-documenter](https://www.npmjs.com/package/insomnia-documenter)
- [Insomnia-documenter (quick tutorial)](https://www.youtube.com/watch?v=pq2u3FqVVy8)
- [MongoDB](https://www.mongodb.com/)
- [Python](https://www.python.org/downloads/)
- [PyMongo](https://pypi.org/project/pymongo/)
<!-- 
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

<p>Esta aplicação atende a fins exclusivamente didáticos e não possui qualquer intuito comercial.</p> -->
