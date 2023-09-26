## Backend - Django


----------
Entrar / Sair do venv Python.

`$ source backend/bin/activate` `$ deactivate`

Cria arquivos de migração com base nas alterações feitas nos modelos do Django, registrando as alterações que devem ser aplicadas ao banco de dados.

`$ python manage.py makemigrations`

Aplica as migrações ao banco de dados, atualizando-o para refletir as alterações definidas nos modelos, garantindo que o banco de dados esteja em sincronia com a estrutura de dados do projeto Django.

`$ python manage.py migrate`

Inicia a aplicação.

`$ python manage.py runserver`

----------