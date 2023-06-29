FROM python:3.9

WORKDIR /app/NeximoChallenge

COPY requirements.txt .

RUN pip install --upgrade pip

RUN pip install --no-cache-dir -r requirements.txt

COPY NeximoChallenge/ .

CMD [ "python","manage.py", "runserver", "0.0.0.0:8080" ]