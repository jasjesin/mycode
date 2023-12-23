# Pull the minimal Ubuntu image
FROM ubuntu:latest

# Install Nginx
RUN apt-get -y update && apt-get -y install apache2
RUN service apache2 start

# Copy the Apache2 config
COPY docker_compose/app/index.html /var/www/html/

# Expose the port for access
EXPOSE 85/tcp

