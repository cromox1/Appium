#!/bin/bash

torun="$1"
ondevice="$2"

if [ x"$ondevice" == x ]; then
ondevice='default'
fi

date1=`date +%Y%m%d_%H`
minit=`date +%M`
minit2=$(((minit / 5 ) * 5))
if [ $minit2 -lt 10 ]; then
   minit1=0${minit2}
else
   minit1=${minit2}
fi
masani=${date1}${minit1}00

if [ x"$torun" == xtestsuite -o x"$torun" == xtest_suite -o x"$torun" == xsuite ]; then

file1=console_${masani}_test_suite.txt
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/MobileApp_Appium" > "$file1"
echo "$ py.test.exe -v tests/test_suite_MobileApp_Appium.py > consoleoutput1.txt 2>&1" >> "$file1"
echo >> "$file1"
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/MobileApp_Appium" >> "$file1"
echo "$ cat consoleoutput1.txt" >> "$file1"
echo >> "$file1"

py.test.exe -v tests/test_suite_MobileApp_Appium.py --device "$ondevice" | tee -a "$file1"

elif [ x"$torun" == xchess -o x"$torun" == xChessAndroid -o x"$torun" == xchessfree ]; then

file1=console_${masani}_chessfree.txt
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/MobileApp_Appium" > "$file1"
echo "$ py.test.exe -v -s tests/ChessAndroid/chessfree_tests.py > consoleoutput1.txt 2>&1" >> "$file1"
echo >> "$file1"
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/MobileApp_Appium" >> "$file1"
echo "$ cat consoleoutput1.txt" >> "$file1"
echo >> "$file1"

py.test.exe -v -s tests/ChessAndroid/chessfree_tests.py --device "$ondevice" | tee -a "$file1" 

else

echo
echo "./xruntest.sh test_suite  [ testsuite / test_suite / suite ] [ new ]"
echo "./xruntest.sh login       [ chess / ChessAndroid ]           [ new ]"
echo

fi
