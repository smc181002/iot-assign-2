#!/bin/bash

docker run -it --rm -v $PWD/mysql-data/:/var/lib/mysql -e MARIADB_ROOT_PASSWORD="rootpass"  -e MARIADB_PASSWORD="passwd@123"  -e MARIADB_USER="mqtt"  -p 3306:3306  --name database  mariadb
