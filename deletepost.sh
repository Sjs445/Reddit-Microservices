#!/bin/sh

curl --verbose \
     --request DELETE \
    http://localhost:5000/api/v1/resources/posts/$1

