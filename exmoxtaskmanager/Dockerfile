FROM python:3.8.0-alpine

WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies
RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt


# copy app
COPY . /app/

#copy entrypoint.sh
#COPY ./entrypoint.sh /app/entrypoint.sh

#RUN chmod +x /app/entrypoint.sh
#RUN chmod 777 /app/entrypoint.sh \
#    && ln -s /app/entrypoint.sh /



# run entrypoint.sh
#ENTRYPOINT ["/app/entrypoint.sh"]


# CMD ["gunicorn", "--bind", ":8000", "--chdir", "ELearning", "ELearning.wsgi:application"]


