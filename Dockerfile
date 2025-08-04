FROM python:3.10-slim

WORKDIR /app

COPY ./board/ .
COPY ./.env .
COPY ./requirements.txt .

RUN pip3 install -r requirements.txt --no-cache-dir
RUN pip3 install gunicorn

RUN python manage.py collectstatic --noinput

RUN python manage.py makemigrations
RUN python manage.py migrate

CMD ["gunicorn", "board.wsgi:application", "--bind", "0:8000"]