# Psicodoc API

## Configuración

Clonando el repositorio
```
$ git clone https://github.com/Dev-Mw/psicodoc-api.git
$ cd psicodoc-api/app/
```

Creando y activando el entorno virtual
```
$ virtualenv -p python3.9 venv
$ source venv/bin/activate
```

Instalando dependencias y el paquete *app/*
```
(venv)$ pip install -r requirements.txt
(venv)$ python setup.py install
```

# Empezando

Construir las migraciones
```
(venv)$ python manage.py makemigrations
```

Corriendo las migraciones
```
(venv)$ python manage.py migrate
```

Corriendo el servicio web
```
(venv)$ python manage.py runserver
```

# API
Probando el API
```
$ curl http://127.0.0.1:8000/api/v1/users/

# Output
{"message": "anonymous user"}
```