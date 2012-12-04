#!/bin/sh
/usr/bin/iostat -xd 30 2 > /tmp/iostat.tmp
mv /tmp/iostat.tmp /var/cache/snmp/iostat

