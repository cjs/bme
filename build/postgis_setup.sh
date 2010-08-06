echo "Installing Postgis libraries"
TGT=/etc/ld.so.conf.d/postgis.conf
if [ -d /etc/ld.so.conf.d ]; then
  if [ -f $TGT ]; then
    echo "$TGT already exists, skipping."
  else
    echo $1/lib > $TGT
    echo $2/lib >> $TGT
    echo $3/lib >> $TGT
    ldconfig
  fi
else
  echo "You don't have the directory '/etc/ld.so.conf.d'"
  echo "SKIPPING ldconfig for you.  If you get errors in the"
  echo "next step, then you need to add"
  echo "---"
  echo "$1/lib"
  echo "$2/lib"
  echo "$3/lib"
  echo "---"
  echo "to your /etc/ld.so.conf file and run 'ldconfig' as root"
  echo "before rerunning this script."
fi