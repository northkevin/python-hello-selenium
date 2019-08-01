# START STANDALONE
# docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome:3.141.59-titanium
# 
# THEN BUILD / RUN -it into this and experiment around
#
FROM google/python-hello

RUN pip install selenium

RUN mkdir /test
COPY . ./test

