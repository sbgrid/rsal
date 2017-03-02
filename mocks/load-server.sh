#!/bin/bash

echo {\"id\":1, \"name\":\"Jojoba22\"} | http POST localhost:5050/start/
echo {\"id\":22, \"name\":\"Jojoba22\"} | http POST localhost:5050/start/
echo {\"id\":333, \"name\":\"Jojoba22\"} | http POST localhost:5050/start/

http GET localhost:5050/pending/
