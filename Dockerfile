FROM python:3.14.0a2-alpine3.19
WORKDIR /app
COPY requirements.txt ./
COPY main-flask.py .
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 80
CMD [ "python", "main.py" ]