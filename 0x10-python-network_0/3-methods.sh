#!/bin/bash
# sends a req and displays the accepted HTTP methods?
curl -sIX OPTIONS "$1" | grep -E 'Allow: ' | cut -d " " -f 2-
