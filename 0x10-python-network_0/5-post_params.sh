#!/bin/bash
# send post with data to url
curl -sX POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
