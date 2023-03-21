-- MySQL setup test
-- creation of database "hbnb_test_db"
CREATE DATABASE IF NOT EXISTS hbnb_test_db;
-- creation of user hbnb_test (in localhost)
CREATE USER IF NOT EXISTS "hbnb_test"@"localhost" IDENTIFIED BY hbnb_test_pwd;
-- give all privileges for the user on the database hbnb_test_db
GRANT ALL PRIVILEGES ON hbnb_test_db TO "hbnb_test"@"localhost"
-- give select privilege to the user on performance_schema
GRANT SELECT PRIVILEGES ON performance_schema TO "hbnb_test"@"localhost";