# Utilizar una imagen base de Python
FROM python:3.9

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /code

# Copiar los archivos de la aplicación en el contenedor
COPY . /code/

# Instalar las dependencias
RUN pip install -r requirements.txt

# Ejecutar los comandos de migraciones de Django
RUN python manage.py makemigrations
RUN python manage.py migrate

# Exponer el puerto que usará el servidor Django (por ejemplo, 8000)
EXPOSE 8000

# Iniciar el servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
