FROM python:3.6

RUN apt update && \
    apt install -y build-essential

COPY . /test_server

WORKDIR /test_server

RUN pip install --upgrade pip && \
    pip install -r requirements.txt


#RUN apt-get remove -y build-essential && \
#    apt-get autoremove -y && \
#    apt-get clean -y && \
#    rm -rf /var/lib/apt/lists/* && \
#    rm -rf /root/.cache

CMD ["/test_server/start.sh"]

EXPOSE 80

RUN echo "OK" > test.log
