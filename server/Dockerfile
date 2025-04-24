

FROM python:3.12

WORKDIR /server
# Копируем зависимости и устанавливаем их
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Копируем оставшиеся файлы проекта
COPY . .

# Открываем порт 8000
EXPOSE 8000
# Команда по умолчанию (запуск FastAPI через uvicorn)
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]