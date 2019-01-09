FROM ubuntu:latest
RUN apt-get update
RUN apt-get -y install python
RUN mkdir /csv
COPY * /csv/
RUN useradd -ms /bin/sh worker
WORKDIR /csv
RUN chown worker /csv/csv_to_insert.py
RUN chmod a+x csv_to_insert.py
RUN chmod a+w insert.sql
USER worker
CMD ["/csv/csv_to_insert.py"]