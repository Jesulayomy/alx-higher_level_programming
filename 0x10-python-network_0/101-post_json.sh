#!/bin/bash
# send a post req with json file as arg
curl -sX POST -H "Content-Type: application/json" -d "$(cat $2)" "$1"
