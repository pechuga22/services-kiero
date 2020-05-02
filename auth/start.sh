#!/bin/bash
app="auth"
docker run --name ${app} -d -p 3003:80 -v $PWD/app:/app robpco/nginx-uwsgi-flask-mssql:python3.6
