FROM python:3.15.0rc2-slim-trixie

WORKDIR /app

COPY . /app

CMD ["python", "-c", "import time; print('Aplicação rodando com sucesso no Docker!'); time.sleep(3600)"]