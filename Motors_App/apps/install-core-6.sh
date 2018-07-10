#!/sbin/sh

LCD=$(grep ro.sf.lcd_density /system/build.prop | cut -d "=" -f 2);

if [ "$LCD" == 320 ]; then
  echo "LCD 320 detected."
  cp -f /tmp/gms/priv-app/PrebuiltGmsCore/PrebuiltGmsCore.apk /system/priv-app/PrebuiltGmsCore/
fi
rm -f /tmp/gms/priv-app/PrebuiltGmsCore/PrebuiltGmsCore.apk

