DO
$do$
BEGIN
   IF NOT EXISTS (
      SELECT FROM pg_database WHERE datname = 'auth-db'
   ) THEN
      PERFORM dblink_exec('dbname=postgres', 'CREATE DATABASE "auth-db"');
   END IF;
END
$do$;
