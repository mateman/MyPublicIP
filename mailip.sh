#!/bin/bash
echo $(curl -s icanhazip.com )'; ' $(date) >>ip.txt
sendmail \
-f unaventonpass@gmail.com \
-t pcuyeu@gmail.com \
-s smtp.gmail.com:587 \
-o tls=yes \
-u IP \
-m $(tail -n 1 ip.txt | cut -d ";" -f 1) \
-xu unaventonpass \
-xp TwoPines1234
