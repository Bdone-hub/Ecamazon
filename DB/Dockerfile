# Utilisez l'image MySQL officielle de Docker Hub
FROM mysql:latest

# Définissez les variables d'environnement pour le mot de passe de la base de données
ENV MYSQL_ROOT_PASSWORD=password
ENV MYSQL_DATABASE=mydatabase
ENV MYSQL_USER=myuser
ENV MYSQL_PASSWORD=mypassword

# Copiez le script SQL d'initialisation dans le conteneur
COPY init.sql /docker-entrypoint-initdb.d/

# Exposez le port MySQL
EXPOSE 3306
