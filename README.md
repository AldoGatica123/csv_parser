# CSV Parser

This project is a lab from "Docker for Professionals" in Udemy for using a bind mount.  

The project consists in a python script that takes a csv file and writes in another file a SQL script to insert it to a table.  

## Quickstart
The docker image has a csv file that runs by default when the container is running.  
To use another file name it *people.csv* and bind the volume to the container.
```docker
docker run -it -v "$(pwd)"/localdir:/csv/res aldogatica123/csv_parser
```

### SQL Table Structure

| ID | LAST_NAME | FIRST_NAME | ADDRESS | CITY |
|---|---|---|---|---|
| INT | VARCHAR 255| VARCHAR 255 | VARCHAR 255  | VARCHAR 255|
