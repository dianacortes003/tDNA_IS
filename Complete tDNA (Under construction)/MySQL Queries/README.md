# MySQL Queries

These folders contain the all the SQL queries/scripts used to create and populate the database. 

## Tables

### patients
Contains paients' general information that doesn't get updated once a new patient is created. The only scenario where a row in this table would be updated is if a patient legally changes their name. 

### clinical_data
Contains medical information about a patient and keeps record of any updated information. Data here can be constantly updated based on patients' progress. 

### countries
Contains countries with their ISO code. This table could be updated to include more countries. 