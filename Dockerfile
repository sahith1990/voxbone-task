FROM python:3

WORKDIR /usr/src/app

ADD https://github.com/SIPp/sipp/releases/download/v3.5.1/sipp-3.5.1.tar.gz ./

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN tar -xzf sipp-3.5.1.tar.gz

WORKDIR /usr/src/app/sipp-3.5.1

RUN ./configure

RUN make

WORKDIR /usr/src/app

CMD [ "python", "./run.py" ]
