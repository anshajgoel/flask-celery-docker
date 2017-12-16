FROM python:3.5.0
WORKDIR /usr/src/app

# install supervisord
RUN apt-get update && apt-get install -y supervisor

# copy requirements and install (so that changes to files do not mean rebuild cannot be cached)
COPY . /www
WORKDIR /www
RUN pip install -r requirements.txt


# expose port 80 of the container (HTTP port, change to 443 for HTTPS)
EXPOSE 80

COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

# needs to be set else Celery gives an error (because docker runs commands inside container as root)
ENV C_FORCE_ROOT=1
# run supervisord
CMD ["/usr/bin/supervisord"]