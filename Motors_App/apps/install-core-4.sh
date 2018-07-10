#!/sbin/sh

LCD=$(grep ro.sf.lcd_density /system/build.prop | cut -d "=" -f 2);

if [ "$LCD" == 240 ]; then
  echo "LCD 240 detected."
  cp -f /tmp/gms/priv-app/PrebuiltGmsCore/PrebuiltGmsCore.apk /system/priv-app/PrebuiltGmsCore/
fi
rm -f /tmp/gms/priv-app/PrebuiltGmsCore/PrebuiltGmsCore.apk

