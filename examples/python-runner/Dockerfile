FROM google/python-hello

RUN pip install selenium

RUN mkdir /test
COPY . /test

ENTRYPOINT ["/test/entrypoint.sh"]