FROM python:3.9

ENV PYTHONUNBUFFERED=1

WORKDIR /MyPipelines
COPY requirements.txt ./
RUN pip install -r requirements.txt
CMD ["python", "./pipeline.py"]