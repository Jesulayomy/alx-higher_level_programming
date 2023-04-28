#!/bin/bash
# Send a req to the url and display response size
curl -s "$1" | wc -c
