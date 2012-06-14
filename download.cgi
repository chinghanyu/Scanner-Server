#!/bin/sh
#
# Linux Scan Server
# http://scannerserver.online02.com
#
# Written by PHiLLIP KLiEWER
# Last Update: 09/13/2008
#
# Download File Script


# SIZE=$(ls -s scans/$QUERY_STRING | sed 's/ .*$//g')


echo 'Content-type: application/octet-stream'
echo 'Content-Disposition: in-line; filename="'$QUERY_STRING'"'
echo ''
cat scans/$QUERY_STRING

# End of Script
