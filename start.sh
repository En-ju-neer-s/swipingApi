#!/bin/bash
app="swiping_api"
docker build -t ${app} .
docker run -p 5000:5000 ${app} \
