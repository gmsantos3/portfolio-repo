FROM python:3.8

RUN useradd -m fastapi

WORKDIR /app

COPY app /app/

RUN chown -R fastapi:fastapi /app

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

USER fastapi

CMD ["python", "main.py"]
