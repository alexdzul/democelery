# socialtenant
Example of using tenant schemas within a Django project.

## Instalación: 

* Paso 1. Crear archivo .env con base al archivo ejemplo .env.example para poder cargar la configuración de la base de datos.
    ```bash
    $ cp .env.example .env
    ```
* Paso 2. Instalar dependencias. 
    ```bash
    $ pip install -r requirements.txt
    ```
* Paso 3. Aplicar migraciones.
    ```bash
    $ python manage.py migrate
    ```
* Paso 4. Crear super usuario.
    ```bash
    $ python manage.py createsuperuser
    ```
 