# Meu Imóvel

<p align="center">
  <img src="https://www.televendasecobranca.com.br/wp-content/uploads/2015/02/Tenho-uma-divida-enorme-devo-refinanciar-meu-imovel-televendas-cobranca.jpg" width="300" height="200"/>
</p>

## Sistema de aluguel de imóveis proximos a você!


Este projeto foi gerado com [Django](https://github.com/django/django) version 2.0.

## Requirements

 - Python 3.5 ou posterior.
 - Django 2.x
 - A Google Maps API key.


#### Set Up
Clone esse projeto:

`$ https://github.com/I-am-Miguel/meu-imovel.git`

`$ cd meu-imovel`

Crie um ambiente virtual e instale as dependências:
~~~~bash
$ virtualenv venv
(venv)$ source /venv/bin/activate
(venv)$ pip install -r requeriments.txt
~~~~

Antes de iniciar o servidor, será necessário coletar
os arquivos estáticos da aplicação:
~~~~
(venv)$ python manage.py collectstatic
~~~~

## Servidor de desenvolvimento
Setup banco de dados:

1) Limpe o histórico para todas as apps, o exemplo abaixo limpa o histórico da app de nome core.
~~~~
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate --fake core zero
~~~~

2) Remova os arquivos de migração:

~~~~
(venv)$ find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
(venv)$ find . -path "*/migrations/*.pyc"  -delete
~~~~
3) Crie as migrações iniciais:

~~~~bash
(venv)$ python manage.py makemigrations
(venv)$ python manage.py migrate --fake-initial
~~~~
Rodando a aplicação
~~~~bash
$ python manage.py runserver
~~~~
Agora você pode ir até [http://localhost:8000](http://localhost:8000).

<span class="warning">(Fonte imagem: www.televendasecobranca.com.br)</span>