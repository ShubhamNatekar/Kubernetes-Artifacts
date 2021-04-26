FROM python:3.8
MAINTAINER shubham natekar <shubhamnatekar9221@gmail.com>

WORKDIR /app

COPY ./app .
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
