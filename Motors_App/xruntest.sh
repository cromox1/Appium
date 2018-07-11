#!/bin/bash

torun="$1"
ondevice="$2"

if [ x"$ondevice" == x ]; then
ondevice='test1'
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
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/Motors_Web" > "$file1"
echo "$ py.test.exe -v tests/test_suite_Motors_Web.py > consoleoutput1.txt 2>&1" >> "$file1"
echo >> "$file1"
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/Motors_Web" >> "$file1"
echo "$ cat consoleoutput1.txt" >> "$file1"
echo >> "$file1"

py.test.exe -v tests/test_suite_Motors_App.py --device "$ondevice" | tee -a "$file1"

elif [ x"$torun" == xbase -o x"$torun" == xhome ]; then

file1=console_${masani}_login.txt
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/Motors_Web" > "$file1"
echo "$ py.test.exe -v -s tests/home/login_tests.py > consoleoutput1.txt 2>&1" >> "$file1"
echo >> "$file1"
echo "PC-TALIBR2+cromox@PC-TALIBR2 /cygdrive/c/Users/cromox/Desktop/newselenium/UDEMY/Motors_Web" >> "$file1"
echo "$ cat consoleoutput1.txt" >> "$file1"
echo >> "$file1"

py.test.exe -v -s tests/motors/motors_base_tests.py --device "$ondevice" | tee -a "$file1" 

else

echo
echo "./xruntest.sh test_suite  [ testsuite / test_suite / suite ] [ test1 / test2 / test3 / default ]"
echo "./xruntest.sh base        [ base / home ]                    [ test1 / test2 / test3 / default ]"
echo

fi
