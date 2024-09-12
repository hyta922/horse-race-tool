FROM public.ecr.aws/docker/library/python:3.9-buster
ENV PYTHONUNBUFFERED=1

WORKDIR /src
COPY api ./
RUN pip3 install --upgrade pip
RUN pip3 install -r /src/requirements.txt
RUN mkdir -p /var/log/my-racing-tool

EXPOSE 80
ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port","80","--reload"]
