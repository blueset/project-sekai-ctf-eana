#!/bin/sh
# Add your startup script

# DO NOT DELETE
# /etc/init.d/xinetd start;
# sleep infinity;
socat TCP-LISTEN:9999,reuseaddr,fork,nodelay EXEC:"python3 /home/ctf/ktane.py",pty