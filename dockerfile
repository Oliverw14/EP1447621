
FROM python:alpine3.7
COPY . /EP1447621
WORKDIR /EP1447621
RUN apk add build-base
RUN pip install -r requirements.txt
EXPOSE 8080
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
