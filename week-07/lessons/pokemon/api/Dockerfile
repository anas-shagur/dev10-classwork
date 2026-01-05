FROM python:alpine

WORKDIR /home/app

COPY . .

RUN apk update \
    && apk add make make gcc g++ mariadb-connector-c mariadb-dev

RUN pip install -r ./requirements.txt

EXPOSE 5000

CMD ["python", "main.py"]