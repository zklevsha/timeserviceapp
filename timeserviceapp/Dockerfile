FROM python:3.8-alpine
WORKDIR /app
ENV PYTHONUNBUFFERED=1
COPY ./requirements.txt .
RUN pip install -r ./requirements.txt
COPY ./timeserviceapp.py .
CMD ["python", "./timeserviceapp.py"]