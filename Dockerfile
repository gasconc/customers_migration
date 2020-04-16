FROM python:alpine3.7
COPY . /customers_migration
WORKDIR /customers_migration
RUN pip3 install -r requirements.txt
EXPOSE 5000
CMD python3 main.py
