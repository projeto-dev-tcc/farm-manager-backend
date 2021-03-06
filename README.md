<h1 align="center"></h1>

<p align="center">
	<a href="#sobre">Sobre</a> &nbsp;|&nbsp;
	<a href="#instalando">Instalando</a> &nbsp;|&nbsp;
	<a href="#rodando">Rodando</a> &nbsp;|&nbsp;
	<a href="#autor">Autores</a> 
</p>

<h3 id="sobre">:information_source: Sobre</h3>

> Este projeto foi desenvolvido utilizando o Django como framework back-end e bootstrap como framework front-end. 

A ideia é:

_"Criar um Prototipo de Sistema para gerenciamento de uma propriedade rural."_

--------------------------------------------------------------------------------------

<h3 id="instalando">:computer: Instalando o Projeto</h3>

**Clonando o Repositório**

```
git clone git@github.com:projeto-dev-tcc/farm-manager-backend.git

cd farm-manager-backend
```

#### Rodando o Projeto

#### Windows

> **Observação:** Foi utilizado o Windows(versão 10), caso ocorra algum problema na instalação, pesquise por conta própria a resolução do mesmo!

```
python -m venv env

env\Scripts\activate

python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py makemigrations home

python manage.py makemigrations usuarios

python manage.py makemigrations manager

python manage.py migrate

python manage.py shell

exec(open('scripts/grupos.py').read())

exit()

python manage.py runserver
```

#### Linux

> **Observação:** Foi utilizado a distro Linux Mint(versão 20.1), caso ocorra algum problema na instalação, pesquise por conta própria a resolução do mesmo!

Caso não tenha um ambiente virtual instalado, digite no terminal:

```
sudo apt-get install python3-venv
```

**Preparando Ambiente Virtual**

Com o terminal aberto, digite no terminal:

```
python3 -m venv env

source env/bin/activate

python -m pip install --upgrade pip

pip install -r requirements.txt

python manage.py makemigrations home

python manage.py makemigrations usuarios

python manage.py makemigrations manager

python manage.py migrate

python manage.py shell

exec(open('scripts/grupos.py').read())

exit()

python manage.py runserver
```

**Criando Super Usuário**

```
python manage.py createsuperuser
```
**Acessando o Projeto**

para visualizar o projeto: http://127.0.0.1:8000/

**Acessando o Painel Administrativo do Django**

Com o projeto rodando, adicione o 'admin/' dps da URL:

http://127.0.0.1:8000/admin/

--------------------------------------------------------------------------------------

<h3 id="autor">:bust_in_silhouette: Autores</h3>

- **Lucas Santos:** [GitHub](https://github.com/LucasSantus)
- **Albert Ramos:** [GitHub](https://github.com/albertallan-rar)
- **Fernanda Thomaz:** [GitHub](https://github.com/FernandaThomaz)
