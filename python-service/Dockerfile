FROM python:slim

COPY app/*.py ./app
COPY requirements.txt ./

RUN pip install -r requirements.txt

RUN adduser --system --group app-user

EXPOSE 8000
USER app-user

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
