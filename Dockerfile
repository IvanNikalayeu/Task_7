FROM python:3

WORKDIR /python

EXPOSE 8001

COPY . /python

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "python", "./main.py" ]
