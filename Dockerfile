FROM python:3.12-slim

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
copy requirements.txt /app

# run sed -i 's/http:\/\/[a-zA-Z0-9]*.[a-zA-Z0-9]*.*.com/http:\/\/ir.ubuntu.sindad.cloud/g' /etc/apt/sources.list

# run pip install --upgrade pip https://mirror-pypi.runflare.com/simple\
#     && pip install -r requirements.txt https://mirror-pypi.runflare.com/simple

run pip install --upgrade pip 
run pip install -r requirements.txt

copy ./core /app

# cmd ["python","manage.py","runserver","0.0.0.0:8000"]