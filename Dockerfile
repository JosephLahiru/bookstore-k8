FROM python:3.7
WORKDIR /app
COPY . /app
RUN pip install -r python/requirements.txt
EXPOSE 5000
CMD ["python", "python/app.py"]
