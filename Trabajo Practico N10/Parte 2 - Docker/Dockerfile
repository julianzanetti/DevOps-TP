# Usa una imagen base con Python y Django preinstalados
FROM python:3.11

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos de requerimientos
COPY requirements.txt /app/

# Instala las dependencias
RUN python -m pip install -r requirements.txt

# Copia el resto de la aplicación
COPY . /app/

# Expone el puerto en el que se ejecuta tu aplicación Django
EXPOSE 8000

# Comando para ejecutar la aplicación
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
