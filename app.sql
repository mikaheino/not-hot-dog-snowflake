-- create database and schema to host streamlit app
CREATE OR REPLACE DATABASE DB_HD ; 
CREATE OR REPLACE SCHEMA SCHEMA_HD ;

CREATE OR REPLACE STAGE DB_HD.SCHEMA_HD.IMAGES
    DIRECTORY = (ENABLE = TRUE)
    ENCRYPTION = (TYPE = 'SNOWFLAKE_SSE');


GRANT READ, WRITE ON STAGE DB_HD.SCHEMA_HD.IMAGES TO ROLE PUBLIC;

--upload app.py to images stage

USE DATABASE DB_HD ;
USE SCHEMA SCHEMA_HD ;

--create wh to use and grant access to it
CREATE OR REPLACE WAREHOUSE HD_WH ;
GRANT USAGE ON WAREHOUSE HD_WH TO PUBLIC ;


-- crate streamlit app
-- this will work, but will complain about st_camera_input, load app.py manually into Streamlit
CREATE OR REPLACE STREAMLIT NOT_HOTDOG_APP
FROM @images
MAIN_FILE = 'app.py'
QUERY_WAREHOUSE = 'HD_WH';
