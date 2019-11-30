#!/usr/bin/env bash

./apache-flume-1.9.0-bin/bin/flume-ng agent \
   -f /home/acerrato/flume/conf/flume_images2.conf \
   --name Agent1 \
   -Dflume.root.logger=INFO,console


#####################################################
## Para enviar datos:
##  
##  $> nc localhost 1357
##  blbblalalablba
##  OK
##  dlsakjdlakjdsalk
##  OK
#####################################################

