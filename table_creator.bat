@echo off
echo --------Creating Tables----------

set /p password= Enter your Password (mysql login) : 

mysql -uroot -p%password% < "migration_script.sql"
echo Your Tables have been Created Successfully!!
PAUSE