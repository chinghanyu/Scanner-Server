#!/bin/sh
#
# Print Image
# http://scannerserver.online02.com
#
# Written by PHiLLIP KLiEWER
# Last Update: 09/14/2008
#

# Spit out that HTML!
echo 'Content-type: text/html'
echo ''
echo '<title>'
echo $QUERY_STRING
echo '</title>'

EXT=$(echo $QUERY_STRING | tr '\n' ' ' | tail -c 4)

case "$EXT" in
	'jpg ')
		echo '<img src="scans/'$QUERY_STRING'">'
		echo '<script language="JavaScript"> window.print() </script>'
	;;
	'png ')
		echo '<img src="scans/'$QUERY_STRING'">'
		echo '<script language="JavaScript"> window.print() </script>'
	;;
	'txt ')
		cat scans/$QUERY_STRING | sed 's/$/<br>/g'
		echo '<script language="JavaScript"> window.print() </script>'
	;;
esac

echo '<script language="JavaScript"> window.close() </script>'

# End of Script
