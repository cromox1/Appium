#!/sbin/sh

good_ffc_device() {
  if [ -f /sdcard/.forcefaceunlock ]; then
    return 0
  elif [ -f /sdcard/.removefaceunlock ]; then
    return 1
  elif cat /proc/cpuinfo | grep -qE 'Victory|herring|sun4i'; then
    return 1
  else
    return 0
  fi
}

if good_ffc_device && [ -e /system/etc/permissions/android.hardware.camera.front.xml ]; then
  echo "Installing face detection support"
  cp -a /tmp/face/* /system/
  mkdir -p /system/app/FaceLock/lib/arm
  ln -s /system/lib/libfacelock_jni.so /system/app/FaceLock/lib/arm/libfacelock_jni.so
elif [ -d /system/vendor/pittpatt/ ]; then
  rm -rf /system/vendor/pittpatt/
  rm -rf /system/app/FaceLock/
  rm -f /system/lib/libfilterpack_facedetect.so
  rm -f /system/lib/libfacelock_jni.so
  rm -f /system/addon.d/71-gapps-faceunlock.sh
fi
rm -rf /tmp/face

TYPE=$(grep ro.build.characteristics /system/build.prop | grep tablet);

if [ -f /sdcard/.removesetupwizard ]; then
  sed -i '/Provision/ d' /system/addon.d/70-gapps.sh
  sed -i '/SetupWizard/ d' /system/addon.d/70-gapps.sh
else
  rm -rf /system/app/Provision
  mkdir /system/priv-app/SetupWizard
  if [ ! "$TYPE" == "" ]; then
    echo "Tablet detected."
    cp -f /tmp/setup/tablet/priv-app/SetupWizard/SetupWizard.apk /system/priv-app/SetupWizard/
  else
    echo "Phone detected."
    cp -f /tmp/setup/phone/priv-app/SetupWizard/SetupWizard.apk /system/priv-app/SetupWizard/
  fi
fi
rm -rf /tmp/setup
mkdir /tmp/gms
