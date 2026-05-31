----------------------------------------------uzee_visit in db---------------------
CREATE USER uzee_visit WITH PASSWORD 'uzee_visit';
CREATE SCHEMA uzee_visit AUTHORIZATION uzee_visit;
ALTER ROLE uzee_visit SET search_path TO uzee_visit;
GRANT ALL ON SCHEMA uzee_visit TO uzee_visit;
------------------------------------------------------------------------------------
SELECT * FROM main_news mn WHERE id NOT IN (1,2);