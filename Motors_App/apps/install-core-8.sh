#!/sbin/sh

LCD=$(grep ro.sf.lcd_density /system/build.prop | cut -d "=" -f 2);

if [ "$LCD" == 480 ]; then
  echo "LCD 480 detected."
  cp -f /tmp/gms/priv-app/PrebuiltGmsCore/PrebuiltGmsCore.apk /system/priv-app/PrebuiltGmsCore/
fi
rm -rf /tmp/gms

