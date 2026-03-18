CREATE DATABASE superamigos_db;
CREATE USER superamigos_user WITH PASSWORD '123456';
GRANT ALL PRIVILEGES ON DATABASE superamigos_db TO superamigos_user;

GRANT ALL PRIVILEGES ON DATABASE superamigos_db TO superamigos_user;

ALTER DATABASE superamigos_db OWNER TO superamigos_user;
