#!/bin/sh
#
# Linux Scan Server
# http://scannerserver.online02.com
#
# Originally Written by PHiLLIP KLiEWER
# Currently Maintained by Ching-Han Yu
# Last Update: 06/08/2012
#
#
# V1.0   - Worked for MEH!
# V1.1   - Added line at the bottom for users to uncomment if their scanner doesn't support
#          the 'brightness' and 'mode' settings.
# V1.1.1 - Added Error output to webpage if scan doesn't work. 
#          Centered webpage.
#          Fixed scale error when set at 100%
#
# V1.1.9 - Total refresh/rewrite - CSS instead of tables
#          New Features: Config Page, Multiple scanner support,
#          Save Settings, Recent Scans page, OCR
#
# V1.2_Beta1 - Bug Fixes - Download.cgi added
#
# V1.3   - Add multi-language interface
#          Use language files stored in JSON format, currently we have US English and Traditional Chinese.
#
# V1.3.1 - Adjust formatted output of scanimage -f
#          Enlarge scanners' name to 48 characters
#          Add SANE package version string
#          Tweak language tab
# V1.3.2 - Fix tool tip bug in Recent Scans page
#          Adjust lang file format


# ****************
# General Settings
# ****************
NAME="Scanner Server"
VER="1.3.2"
SERVER_NAME="BCCL"
SERVER_URL="bcclib.ee.nchu.edu.tw"
SERVER_LANG="zh_TW"

# ****************
# Functions
# ****************

Get_Values () {	# Read in form Values
	export SCANNER=`echo "$QUERY_STRING" | grep -oE "(^|[?&])scanner=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`
	export QUALITY=`echo "$QUERY_STRING" | grep -oE "(^|[?&])quality=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`
	export SIZE=`echo "$QUERY_STRING" | grep -oE "(^|[?&])size=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`
	export BRIGHT=`echo "$QUERY_STRING" | grep -oE "(^|[?&])bright=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`
	export MODE=`echo "$QUERY_STRING" | grep -oE "(^|[?&])mode=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`
	export ORNT=`echo "$QUERY_STRING" | grep -oE "(^|[?&])ornt=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`
	export ROTATE=`echo "$QUERY_STRING" | grep -oE "(^|[?&])rotate=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`
	export FILETYPE=`echo "$QUERY_STRING" | grep -oE "(^|[?&])filetype=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`
	export SCALE=`echo "$QUERY_STRING" | grep -oE "(^|[?&])scale=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`
	export SAVEAS=`echo "$QUERY_STRING" | grep -oE "(^|[?&])saveas=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`
	export SET_SAVE=`echo "$QUERY_STRING" | grep -oE "(^|[?&])set_save=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`
}

Put_Values () {	# Update values back to form
	echo '<script type="text/javascript">'
	echo 'document.scanning.scanner.value="'$SCANNER'"'
	echo 'document.scanning.quality.value="'$QUALITY'"'
	echo 'document.scanning.size.value="'$SIZE'"'
	echo 'document.scanning.bright.value="'$BRIGHT'"'
	echo 'document.scanning.mode.value="'$MODE'"'
	echo 'document.scanning.ornt.value="'$ORNT'"'
	echo 'document.scanning.rotate.value="'$ROTATE'"'
	echo 'document.scanning.filetype.value="'$FILETYPE'"'
	echo 'document.scanning.scale.value="'$SCALE'"'
	echo '</script>'
}

Print_Message () { # Add a Message div after the page has loaded
	MES=$(cat inc/message.inc | sed 's/$$TITLE/'"$1"'/g' | sed 's/$$MESSAGE/'"$2"'/g')
	echo '<script type="text/javascript">'
	echo 'document.getElementById("new_mes").innerHTML="'"$MES"'";'
	echo '</script>'
}

Update_Preview () { # Change the Preview Pane image via JavaScript
	echo '<script type="text/javascript">'
	echo 'document.getElementById("preview_image").innerHTML="<p><img src='$1'></p>";'
	echo '</script>'
}

Update_Links () { # Change the Preview Pane image links via JavaScript
	LINKS=$(cat inc/previewlinks.inc | sed 's/$$FILE/'"$1"'/g')
	echo '<script type="text/javascript">'
	echo 'document.getElementById("preview_links").innerHTML="'$LINKS'"'
	echo 'document.getElementById("link_download").title=lang_scan.DOWNLOAD;'
	echo 'document.getElementById("link_printer").title=lang_scan.PRINTER;'
	echo 'document.getElementById("link_delete").title=lang_scan.DELETE;'
	echo '</script>'
}

Header () { # Spit out HTML header
	cat inc/header.inc | sed 's/$$SERVER_NAME/'$SERVER_NAME'/g' | sed 's/$$SERVER_URL/'$SERVER_URL'/g' | sed 's/$$PAGE_NAME/'"$1"'/g' | sed 's/$$PROG_NAME/'"$NAME"'/g' | sed 's/$$PAGE/'"$PAGE"'/g' | sed 's/$$SERVER_LANG/'"$SERVER_LANG"'/g'
}

Footer () { # Spit out HTML footer
	cat inc/footer.inc | sed 's/$$SERVER_NAME/'$SERVER_NAME'/g' | sed 's/$$SERVER_URL/'$SERVER_URL'/g' | sed 's/$$VER/'$VER'/g' | sed 's/$$PROG_NAME/'"$NAME"'/g'
}

I18n () { # Internationalization
	cat lang/$SERVER_LANG.js | grep $1 | cut -d\' -f2
}

# ****************
# Spit out that HTML!
# ****************

PAGE=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])page=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "=")
ACTION=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])action=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "=")
LANGUAGE=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])language=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "=")
#echo $LANGUAGE

# ****************
# Language setting
# ****************
if [ ! -f config/lang.conf ]; then
	echo 'en_US' > config/lang.conf
elif [ $LANGUAGE ]; then
	echo $LANGUAGE > config/lang.conf
fi
SERVER_LANG=$(cat config/lang.conf)

echo 'Content-type: text/html'
echo ''
#echo $ACTION

# ****************
# Recent Scans Page
# ****************
if [ $PAGE = "scans" ]; then
	#Header "Recent Scans"
	Header "$(I18n "TAB_RECENT_SCANS")"

	# Delete selected scanned image
	DELETE=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])delete=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "=")

	if [ $DELETE = "Remove" ]; then
		FILE=$(echo "$QUERY_STRING" | grep -oE "(^|[?&])file=[^&]+" | sed "s/%20/ /g" | sed "s/%7E/~/g" | cut -f 2 -d "=")
		#FILE=$(echo $FILE | sed "s/....$//g" | sed 's/Scan_//g')
		rm scans/*$FILE*
		#Print_Message "Delete Image" "$FILE has been deleted"
		Print_Message "$(I18n "DELETE_IMAGE_TITLE")" "$(cat lang/$SERVER_LANG.js | grep DELETE_IMAGE_MSG | sed 's/$$FILE/'$FILE'/g' | cut -d\' -f2)"
	fi

	# Display Thumbnails of scanned images, if any
	FILES=$(ls scans/Preview*)

	if [ -z $FILES ]; then
		#Print_Message "No Image" "There is no previously scanned image"
		Print_Message "$(I18n "NO_IMAGE_TITLE")" "$(I18n "NO_IMAGE_MSG")"
	else
		DOWNLOAD_IMG=$(I18n "DOWNLOAD_IMG")
		PRINT_IMG=$(I18n "PRINT_IMG")
		DELETE_IMG=$(I18n "DELETE_IMG")
		for IMAGE in $FILES
		do
			FILE=$(echo $IMAGE | sed 's/jpg//g' | sed 's/scans\/Preview/Scan/g')
			FILE=$(ls scans/$FILE* | sed 's/scans\/Scan_//g')
			IMAGE=$(echo $IMAGE | sed 's/scans\///g')
			cat inc/scans.inc | sed 's/$$IMAGE/'"$IMAGE"'/g' | sed 's/$$FILE/'"$FILE"'/g' | sed 's/$$DOWNLOAD_IMG/'"$DOWNLOAD_IMG"'/g' | sed 's/$$PRINT_IMG/'"$PRINT_IMG"'/g' | sed 's/$$DELETE_IMG/'"$DELETE_IMG"'/g'
		done
	fi
	Footer

# ****************
# Config Page
# ****************
elif [ $PAGE = "config" ]; then
	if [ $ACTION = "color" ]; then # Change color sceme
		COLORS=`echo "$QUERY_STRING" | grep -oE "(^|[?&])colors=[^&]+" | sed "s/%20/ /g" | cut -f 2 -d "="`
		BK_COLOR=$(echo $COLORS | sed 's/.......$//g')
		LK_COLOR=$(echo $COLORS | sed 's/......+//g')
		cat inc/style.css | sed 's/$$BG_COLOR/'$BK_COLOR'/g' | sed 's/$$LK_COLOR/'$LK_COLOR'/g' > config/style.css
	fi

	#Header "Configure"
	Header "$(I18n "TAB_CONFIGURE")"
	SANE_VER=$(scanimage -V)
	#echo "Remote IP: $REMOTE_ADDR"
	#SET_RESTORE=$(cat config/settings.conf | tr '\n' ' ' | sed 's/ ]/ <img src=inc\\\/images\\\/delete.png width=10  > ] <br>/g' )
	cat inc/config.inc | sed 's/$$SANE_VER/'"$SANE_VER"'/g' # | sed 's/$$SET_RESTORE/'"$SET_RESTORE"'/g'
	Footer

	#DETECT_BTN_RESULT="Search+For+Scanners"
	DETECT_BTN_RESULT="$(I18n "DETECT_BTN_RESULT")"
	if [ $ACTION = $DETECT_BTN_RESULT ]; then # Find avalible scanners on the system
		#Print_Message "Detecting Scanners" "Now detecting scanners. Please wait..."
		Print_Message "$(I18n "SCANNER_DETECTING_TITLE")" "$(I18n "SCANNER_DETECTING_MSG")"

		# Find scanners with formatted output
		# scanimage -f "scanner number %i device %d is a %t, model %m, produced by %v" 
		OP=$(scanimage -f "ID=%i INUSE=0 DEVICE=%d NAME=%m %t,")
		OP=$(echo $OP | sed 's/,/\n/g')
		echo "$OP" > config/scanners.conf
		OP=$(cat config/scanners.conf | sed 's/^.*NAME\=//g' | sed 's/$/<br>/g' | sed 's/_/ /g' | tr -d '\n')
 		echo $OP > config/message.conf
		if [ -z $OP ]; then
			#Print_Message "No Scanner Found" "Please make sure all scanners are plugged in and turned on. If still not found, your scanner may not be supported by SANE."
			Print_Message "$(I18n "SCANNER_NOT_FOUND_TITLE")" "$(I18n "SCANNER_NOT_FOUND_MSG")" 
		else
			#Print_Message "Scanner Found" "$OP"
			Print_Message "$(I18n "SCANNER_FOUND_TITLE")" "$OP"
		fi
	fi

# ****************
# Scan Image Page
# ****************
else
	#Header "Scan Image"
	Header "$(I18n "TAB_SCAN_IMAGE")"

	Get_Values

	SCANNERS=$(cat config/scanners.conf)

	if [ -n "$SAVEAS" ]; then # Save settings to conf file
		if [ -n "$SET_SAVE" ]; then
			ACTION="Save Set"
			SET_SAVE=$(echo $SET_SAVE | sed 's/+/ /g')
			echo "[ <a href=index.cgi?page=scan\&action=restore\&scanner=$SCANNER\&quality=$QUALITY\&size=$SIZE\&ornt=$ORNT\&mode=$MODE\&bright=$BRIGHT\&rotate=$ROTATE\&scale=$SCALE\&filetype=$FILETYPE >$SET_SAVE<\/a> ]" >> config/settings.conf
		fi
	fi

	if [ -z $SCANNERS ]; then # Add scanners to scanner list
		#Print_Message "No Available Scanners" "Scanners are not ready for use. Please go to Configure section to set your scanners"
		Print_Message "$(I18n "NO_SCANNER_AVAIL_TITLE")" "$(I18n "NO_SCANNER_AVAIL_MSG")"
	else
		SCANNER_OPTION=""
		SCANNER_IDS=$(cat config/scanners.conf | sed 's/ID\=//g' | sed 's/ INUSE.*$//g' | tr '\n' ' ')
		SCANNERS=$(cat config/scanners.conf | sed 's/^.*NAME\=/{/g' | tr '\n' '}')
		SCANNERS="$SCANNERS {"

		for NUM_SCAN in $SCANNER_IDS
		do
			SCN=$(echo $SCANNERS | sed 's/{/ /g' | sed 's/}.*.$//' | sed 's/_/ /g' | head -c 48)
			SCANNERS=$(echo $SCANNERS | sed 's/^[^}]*}//')
			SCANNER_OPTION=$SCANNER_OPTION"<option value=$NUM_SCAN>$SCN<\/option> "
		done
		SET_RESTORE=$(cat config/settings.conf | tr '\n' ' ' )
		cat inc/scan.inc | sed 's/$$SCANNERS/'"$SCANNER_OPTION"'/g' | sed 's/$$SET_RESTORE/'"$SET_RESTORE"'/'
	fi

	if [ -n "$ACTION" ]; then # Only update values back to form if they aren't empty
		Put_Values
	fi
	Footer

	#SCAN_BTN_RESULT="Scan+Now"
	SCAN_BTN_RESULT="$(I18n "SCAN_BTN_RESULT")"
	if [ $ACTION = $SCAN_BTN_RESULT ]; then # $ACTION = "Scan+Now", Check to see if scanner is in use
		SCAN_IN_USE=$(cat config/scanners.conf | grep "ID=$SCANNER " | grep "INUSE=0")
		if [ -z "$SCAN_IN_USE" ]; then
			#Print_Message "Scanner Is Busy" "The selected scanner is currently busy, please wait or select another one"
			Print_Message "$(I18n "SCANNER_BUSY_TITLE")" "$(I18n "SCANNER_BUSY_MSG")"
			ACTION="Do Not Scan"
		fi
	fi

	if [ $ACTION = $SCAN_BTN_RESULT ]; then # $ACTION = "Scan+Now" Scan Image!
		Update_Preview "inc/images/loading.gif"

		# Scanner in Use
		cat config/scanners.conf | sed 's/ID='"$SCANNER"' INUSE=0/ID='"$SCANNER"' INUSE=1/g' > /tmp/scn
		mv /tmp/scn config/scanners.conf

		# Get Device
		DEVICE=$(cat config/scanners.conf | grep "ID=$SCANNER" | sed 's/^.*DEVICE=//g' | sed 's/ .*$//g')

		# Set size & orientation of scan
		if [ $SIZE = "full" ]
		then
			SIZE=""
		else
			SIZE_X=`echo "$SIZE" | cut -f 1 -d "-"`
			SIZE_Y=`echo "$SIZE" | cut -f 2 -d "-"`
			if [ $ORNT = "vert" ]
			then
				SIZE="-x "$SIZE_X" -y "$SIZE_Y
			else
				SIZE="-y "$SIZE_X" -x "$SIZE_Y
			fi
		fi

		#echo "scanimage -d $DEVICE --resolution $QUALITY $SIZE --mode $MODE --format=ppm > /tmp/scan_file$SCANNER.ppm"
		scanimage -d $DEVICE --resolution $QUALITY $SIZE --mode $MODE --format=ppm > /tmp/scan_file$SCANNER.ppm

		# Adjust Brightness
		if [ $BRIGHT != "0" ]; then
			ppmbrighten -v $BRIGHT /tmp/scan_file$SCANNER.ppm > /tmp/_scan_file$SCANNER.ppm
			rm /tmp/scan_file$SCANNER.ppm
			mv /tmp/_scan_file$SCANNER.ppm /tmp/scan_file$SCANNER.ppm
		fi

		# Rotate Image
		if [ $ROTATE != "0" ]
		then
			pnmflip -r$ROTATE /tmp/scan_file$SCANNER.ppm > /tmp/_scan_file$SCANNER.ppm
			rm /tmp/scan_file$SCANNER.ppm
			mv /tmp/_scan_file$SCANNER.ppm /tmp/scan_file$SCANNER.ppm
		fi

		# Scale Image
		if [ $SCALE != "100" ]
		then
			pnmscale -xscale 0.$SCALE -yscale 0.$SCALE /tmp/scan_file$SCANNER.ppm > /tmp/_scan_file$SCANNER.ppm
			rm /tmp/scan_file$SCANNER.ppm
			mv /tmp/_scan_file$SCANNER.ppm /tmp/scan_file$SCANNER.ppm
		fi

		# Dated Filename for scan image & preview image
		FILENAME=`date +%b_%d_%Y~%H-%M-%S`
		S_FILENAME='Scan_'$SCANNER'_'$FILENAME'.'$FILETYPE
		P_FILENAME='Preview_'$SCANNER'_'$FILENAME'.jpg'

		# Generate Preview Image
		pnmscale -xysize 450 450 /tmp/scan_file$SCANNER.ppm > /tmp/scan_preview$SCANNER.ppm
		pnmtojpeg /tmp/scan_preview$SCANNER.ppm > scans/$P_FILENAME
		rm /tmp/scan_preview$SCANNER.ppm

		# Convert scan to file type
		case "$FILETYPE" in
     		'jpg')
			pnmtojpeg /tmp/scan_file$SCANNER.ppm > scans/$S_FILENAME
	 	;;
		'png')
	         	pnmto$FILETYPE /tmp/scan_file$SCANNER.ppm > scans/$S_FILENAME
	 	;;
		'tiff')
	         	pnmto$FILETYPE /tmp/scan_file$SCANNER.ppm > scans/$S_FILENAME
	        ;;
		'txt')
			S_FILENAMET=$(echo $S_FILENAME | sed 's/.txt//g')
			pnmtotiff /tmp/scan_file$SCANNER.ppm > /tmp/_scan_file$SCANNER.tiff
			tesseract /tmp/_scan_file$SCANNER.tiff scans/$S_FILENAMET -l eng
			rm /tmp/_scan_file$SCANNER.tiff
		;;
		esac
		rm /tmp/scan_file$SCANNER.ppm

		# Check if image is empty and post error, otherwise post image to page
		IFSCAN=$(ls -lh scans/$P_FILENAME | grep "K")
		if [ -z $IFSCAN ] ; then
			rm scans/$P_FILENAME
			rm scans/$S_FILENAME
			Update_Preview "inc/images/preview.png"
			#Print_Message "Unable To Scan" "Please make sure all scanners are plugged in and turned on. If still not found, your scanner may not be supported by SANE."
			Print_Message "$(I18n "UNABLE_TO_SCAN_TITLE")" "$(I18n "UNABLE_TO_SCAN_MSG")"
		else
			Update_Links "$S_FILENAME"
			Update_Preview "scans/"$P_FILENAME
		fi
		cat config/scanners.conf | sed 's/ID='"$SCANNER"' INUSE=1/ID='"$SCANNER"' INUSE=0/g' > /tmp/scn
		mv /tmp/scn config/scanners.conf
		rm /tmp/scn

	fi

	echo '<script type="text/javascript">document.scanning.action.disabled=false</script>'
fi

# End of Script
