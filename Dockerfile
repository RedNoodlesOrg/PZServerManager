
FROM python:3.12
WORKDIR /usr/src/app
COPY ./ /usr/src/app/
RUN pip install --upgrade pip
RUN pip install poetry
RUN poetry config virtualenvs.create false
RUN poetry install --only main
EXPOSE 80

CMD ["waitress-serve", "--host", "0.0.0.0", "--port" , "80", "--call", "pz_server_manager:create_app"]

