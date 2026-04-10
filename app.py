#FROM python:3.9.7-slim-bullseye
FROM devilbox/python-flask:3.8-dev

WORKDIR /app


COPY ./ /app/

#RUN apt-get update
#RUN apt-get install -y python-is-python3

EXPOSE 8000

CMD ["python3", "app.py"] 

