# START STANDALONE
# docker run -d -p 4444:4444 -v /dev/shm:/dev/shm selenium/standalone-chrome:3.141.59-titanium
# 
# THEN BUILD / RUN -it into this and experiment around
#
FROM google/python-hello

RUN pip install selenium

RUN mkdir /selenium-test
COPY . ./selenium-test

# tail an empty file to trick the service to keep running - note I have no clue what this does if left running for a long time, this is meant to be a short test
CMD tail -f /dev/null