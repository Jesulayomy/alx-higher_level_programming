#!/bin/bash
# returns the status code from a request
curl -so /dev/null -w %{http_code} "$1"
