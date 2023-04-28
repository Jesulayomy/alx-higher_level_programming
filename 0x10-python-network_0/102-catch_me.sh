#!/bin/bash
# send a req to url and respond by string
curl -sLX PUT 0.0.0.0:5000/catch_me_2 -H "Origin: School" -d "user_id=98"
