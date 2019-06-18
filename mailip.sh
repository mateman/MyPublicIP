#!/bin/bash
echo $(curl -s icanhazip.com )'; ' $(date) >>ip.txt
sendmail \
-f mailOrigen@gmail.com \
-t mailDestino@gmail.com \
-s smtp.gmail.com:587 \
-o tls=yes \
-u IP \
-m $(tail -n 1 ip.txt | cut -d ";" -f 1) \
-xu mailOrigen \
-xp unaPassword
