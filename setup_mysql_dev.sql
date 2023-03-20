-- script that prepares a MySQL server for the project
--creation of database "hbnb_dev_db"
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
-- creation of the user "hbnb_dev"
CREATE USER IF NOT EXISTS "hbnb_dev"@"localhost" IDENTIFIED BY "hbnb_dev_pwd";
-- give all privileges to the user on "hbnb_dev_db"
GRANT ALL PRIVILEGES ON hbnb_dev_db TO "hbnb_dev"@"localhost";
-- give select privilege to the user on performance_schema
GRANT SELECT PRIVILEGES ON performance_schema TO "hbnb_dev"@"localhost";
