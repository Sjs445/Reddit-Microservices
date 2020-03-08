#!/bin/sh

curl --verbose \
     --request POST \
     --header 'Content-Type: application/json' \
     --data @newpost.json \
    http://localhost:5000/api/v1/resources/posts

