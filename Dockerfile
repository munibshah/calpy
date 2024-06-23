FROM tiangolo/uvicorn-gunicorn-fastapi

COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

COPY ./app /app

RUN cat /app/main.py 

CMD ["fastapi", "run", "/app/main.py", "--port", "8080"]
