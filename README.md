# crud_nosql_rest

- [Translations](#translations)
- [About](#about)
- [Instalation](#instalation)
- [Documentation](#documentation)
- [References](#references)

<br>

## Translations

- [Português brasileiro](./.multilingual_readmes/README_pt-br.md)
- [English / Inglês](https://github.com/AndreKuratomi/crud_nosql_rest)

<br>

## About

<b>crud_nosql_rest</b> is a simple API for blog posts simulation with NoSQL databasen and CRUD operations.

This API uses the language <strong>[Python](https://www.python.org/downloads/)</strong>, its framework <strong>[Flask](https://flask.palletsprojects.com/en/3.0.x/)</strong>, its lib <strong>[PyMongo](https://pypi.org/project/pymongo/)</strong>, the database <strong>[MongoDB](https://www.mongodb.com/)</strong>, and the software <strong>[Docker](https://docs.docker.com/)</strong> for running both <b>Python</b> and <b>MongoDB</b>.

<br>

## Instalation

<h3>0. It is first necessary to have instaled the following devices:</h3>

- The code versioning <b>[Git](https://git-scm.com/downloads)</b>,

- The software <b>[Docker](https://docs.docker.com/)</b>,

- A <b>code editor</b>, also known as <b>IDE</b>. For instance, <strong>[Visual Studio Code (VSCode)](https://code.visualstudio.com/)</strong>,

- <p> And versioning your directory to receive the aplication clone:</p>

```
git init
```

Obs: both <b>Python</b> and <b>MongoDb</b> are not required for this app since they are already provided by <b>Docker</b>.

<br>
<h3>1. Clone the repository <b>crud_nosql_rest</b> by your machine terminal or by the IDE:</h3>

```
git clone https://github.com/AndreKuratomi/crud_nosql_rest.git
```

WINDOWS:

Obs: In case of any mistake similar to this one: 

```
unable to access 'https://github.com/AndreKuratomi/crud_nosql_rest.git': SSL certificate problem: self-signed certificate in certificate chain
```

Configure git to disable SSL certification:

```
git config --global http.sslVerify "false"
```

<p>Enter the directory:</p>

```
cd crud_nosql_rest
```
<br>

<h3>2. After cloning the repository install:</h3>

<h4>Virtual enviroment* and update its dependencies with the following command:</h4>


LINUX:
```
python3 -m venv venv --upgrade-deps
```

WINDOWS:
```
py -m venv venv --upgrade-deps
```

In case an error like this one is returned just follow the command displayed:

```
The virtual environment was not created successfully because ensurepip is not
available.  On Debian/Ubuntu systems, you need to install the python3-venv
package using the following command.

    apt install python3.10-venv

You may need to use sudo with that command.  After installing the python3-venv
package, recreate your virtual environment.
```

*It is a good practice to work with virtual enviroments because different projects may need different dependencies. A virtual enviroment is only a separated enviroment from the user machine. If not used, the user's machine may have lots of dependencies intalled that may only be used in a single project.

<br>

<h4>Ativate your virtual enviroment with the command:</h4>

LINUX:
```
source/venv/bin/activate
```

WINDOWS:

On Windows operational system it is necessary to configure the Execution Policy at PowerShell:

```
Get-ExecutionPolicy # to check the Execution policy type
Set-ExecutionPolicy RemoteSigned # to change the type of policy if the command above shows 'Restricted'
```
Obs: It may often be necessary to open PowerShell as administrador for that.

```
.\env\Scripts\activate
```

<br>

<h4>Install its dependencies:</h4>

```
pip install -r requirements.txt
```
<br>

WINDOWS:

In case any error similar to the one bellow be returned:

```
ERROR: Could not install packages due to an OSError: [Errno 2] No such file or directory: 'C:\\Users\\andre.kuratomi\\OneDrive - Company\\Área de Trabalho\\tables_to_db_mail_for_finances\\tables_to_db_and_mail_finances\\env\\Lib\\site-packages\\jedi\\third_party\\django-stubs\\django-stubs\\contrib\\contenttypes\\management\\commands\\remove_stale_contenttypes.pyi'
HINT: This error might have occurred since this system does not have Windows Long Path support enabled. You can find information on how to enable this at https://pip.pypa.io/warnings/enable-long-paths
```

Run cmd as adminstrador with the following command:

```
reg.exe add HKLM\SYSTEM\CurrentControlSet\Control\FileSystem /v LongPathsEnabled /t REG_DWORD /d 1 /f
```

<br>

<h3>3. Open the application on your IDE:</h3>

```
code .
```
<br>


<h3>4. Create <b>.env</b> file at the root directory:</h3>

```
touch .env
```

Inside it we need to put our enviroment variables taking as reference the given file <b>.env.example</b>:

```
FLASK_ENV=flask_env
MONGO_CLIENT=some_client
MONGO_URI=mongo_uri
```

<b>Obs:</b> Do not share info from <b>.env</b> file. It is already mentioned in <b>.gitignore</b> for not being pushed to the repo.

<h3>5. And run Flask:</h3>

LINUX and WINDOWS:
```
flask run
```

<br>

<h3>6. Run dockerfile*:</h3>

LINUX and WINDOWS:
```
docker compose build
```

<br>

<h3>7. Run docker compose*:</h3>

LINUX and WINDOWS:
```
docker compose up
```

<br>

*It may be required to set docker with the user with the following command:

```
sudo usermod -aG docker $USER
```

This $USER can be obtained by the following command (Linux):

```
whoami
```

<br>

## Documentation

For full description of endpoints and its responses check the insomnia documentation on the link bellow (necessary free login account) click [here](https://insomnia-odwtdahxh-abkuras-projects.vercel.app/).

<br>

## References

- [Docker](https://docs.docker.com/)
- [Dotenv](https://www.npmjs.com/package/dotenv)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Insomnia-documenter](https://www.npmjs.com/package/insomnia-documenter)
- [Insomnia-documenter (quick tutorial)](https://www.youtube.com/watch?v=pq2u3FqVVy8)
- [MongoDB](https://www.mongodb.com/)
- [Python](https://www.python.org/downloads/)
- [PyMongo](https://pypi.org/project/pymongo/)
