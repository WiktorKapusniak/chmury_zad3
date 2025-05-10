FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install Flask pymongo
EXPOSE 5000
CMD ["python", "app.py"]