FROM python:3.9
WORKDIR .
ENV PYTHONUNBUFFERED=1
COPY requirements.txt .
COPY amanpandey.sh .
RUN bash amanpandey.sh
COPY . .
CMD ["python3", "-m", "main_startup"]
