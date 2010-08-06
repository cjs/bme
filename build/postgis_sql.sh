echo "Installing the Postgis data, if prompted for a password, give the postgres database user password."
echo "If this is a reinstall, just hit enter instead of entering the password."
echo "That will skip loading the SQL, but won't kill the buildout script."

createdb -E UTF8 template_postgis
createlang -d template_postgis plpgsql
psql -d template_postgis -f $1/share/lwpostgis.sql
psql -d template_postgis -f $1/share/spatial_ref_sys.sql
psql -d template_postgis -c "GRANT ALL ON geometry_columns TO PUBLIC;"
psql -d template_postgis -c "GRANT ALL ON spatial_ref_sys TO PUBLIC;"
