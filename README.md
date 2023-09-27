## Backend - Django



Entrar no venv Python.
```shell
source backend/bin/activate
```
Sair
```shell
deactivate
```
----------

Cria arquivos de migração com base nas alterações feitas nos modelos do Django, registrando as alterações que devem ser aplicadas ao banco de dados.
```shell
python manage.py makemigrations
```

Aplica as migrações ao banco de dados, atualizando-o para refletir as alterações definidas nos modelos, garantindo que o banco de dados esteja em sincronia com a estrutura de dados do projeto Django.
```shell
python manage.py migrate
```
----------

Inicia a aplicação.
```shell
python manage.py runserver
```

----------

## MySql

Iniciar o MySQL Server:
```shell
sudo service mysql start
```

Parar o MySQL Server:
```shell
sudo service mysql stop
```

Reiniciar o MySQL Server:
```shell
sudo service mysql restart
```

Verificar o status do MySQL Server:
```shell
sudo service mysql status
```

Entrar no MySQL Server: 
```shell
sudo mysql -u root -p
```

