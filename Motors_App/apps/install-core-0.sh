#!/sbin/sh

LCD=$(grep ro.sf.lcd_density /system/build.prop | cut -d "=" -f 2);

#if [ ! "$LCD" == 240 ] && [ ! "$LCD" == 320 ] && [ ! "$LCD" == 480 ]; then
if [ ! "$LCD" == 320 ] && [ ! "$LCD" == 480 ]; then
  echo "Installing default."
  cp -f /tmp/gms/priv-app/PrebuiltGmsCore/PrebuiltGmsCore.apk /system/priv-app/PrebuiltGmsCore/
fi
rm -f /tmp/gms/priv-app/PrebuiltGmsCore/PrebuiltGmsCore.apk

