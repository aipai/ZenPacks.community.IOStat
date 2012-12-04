#!/bin/sh
iostat=/usr/bin/iostat
action="Util"
if [ $# -eq 1 ]
then
	action=$1
fi
case $action in
	"DeviceDescr" ) 
	${iostat} -x | grep '^[s|h]d. '| sed -r 's/ +/\t/g' | cut -f1
	;;
	"Util" )
	${iostat} -x | grep '^[s|h]d. '| sed -r 's/ +/\t/g' | cut -f12
	;;
	"Index" )
	${iostat} -x | grep '^[s|h]d. ' | nl -nln | cut -f 1 | sed 's/[ \t]*//g'
	;;
esac
