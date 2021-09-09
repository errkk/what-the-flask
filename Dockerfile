# syntax=docker/dockerfile:1
FROM python:3.7-alpine
WORKDIR /code
RUN apk add --no-cache gcc musl-dev linux-headers bash
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
EXPOSE 5000
COPY src src
WORKDIR /code/src
RUN python3 setup.py develop
CMD ["python", "beryl/app.py"]
