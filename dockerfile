FROM python:3.7
COPY . /app
WORKDIR /app
COPY main.py .
COPY requirements.txt .
RUN pip install -r requirements.txt
#ARG some_variable_name=default_value

CMD [ "python", "./main.py", "https://github.com/microsoft/nni","2020-04-02", "2020-09-02" ]

