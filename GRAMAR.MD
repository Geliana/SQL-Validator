# Awino - Structured Query Language A-SQL
### qualities:
1. case-insensitive
2. semicolon at the end is not a requirement but is recommended to be used
3. supports common SQL syntax
4. minimal
5. fast

### Supported Data types
    integer
    boolean
    varchar
    float
    
### grammar Rules:
1. use spaces around operators 
    > e.g.(column1 = value1 not column1=value1 otherwise it will be interpreted as a string)
2. Insert space after a coma

### Modes:   
#### general mode:
> This mode is non-specific and is  unlimited in databases access but has limited access to its interaction to the same.

###### _Below is a list of the syntax available in general mode_

1. HELP
2. CREATE DATABASE 'database_name'
    >   _also accepted_
    >   
    >       CREATE 'database_name'
3. DROP DATABASE 'database_name'
    >   _also accepted_
    >   
    >       DROP 'database_name'
4. INFORM
5. INFORM 'database_name'
6. USE DATABASE 'database_name'
7. ALTER DATABASE 'database_name' RENAME 'new_database_name'
8. USE DATABASE 'database_name'
    >   _also accepted_
    >   
    >       USE 'database_name'
9. USING DATABASE 'database_name' DROP TABLE 'table_name' 
    >   _also accepted_
    >   
    >       USING DATABASE 'database_name' DROP 'table_name'
10. USING DATABASE 'database_name' CREATE 'table_name'
11. USING DATABASE 'database_name' ALTER TABLE 'table_name' RENAME TO 'new_table_name'
12. USING DATABASE 'database_name' ALTER TABLE 'table_name' ADD COLUMN 'column_name' (DATA TYPE)

#### specific mode:
>This mode is specific per database and grants full access to all its functionalities

###### _Below is a list of the syntax available in specific mode_

1. INFORM
2. INFORM 'table_name'
3. CREATE TABLE 'table_name' CREATE TABLE ('table_name1', 'table_name2', 'table_name3', ....)
4. CREATE 'table_name' || CREATE ('table_name1', 'table_name2', 'table_name3', ....)
5. CREATE 'table_name' ('column_name' DATA_TYPE(LENGTH) CONSTRAINT, 'column_name_2' DATA_TYPE(LENGTH) CONSTRAINT, ....)
6. DROP 'table_name'
7. ALTER 'table_name' ADD COLUMN 'column_name' [DATA_TYPE]
8. ALTER 'table_name' DROP COLUMN 'column_name'
9. ALTER 'table_name' RENAME TO 'new_table_name'
10. INSERT INTO 'table_name' VALUES (`values`)
11. INSERT INTO 'table_name' (`columns`) values (`values`)
12. SELECT * FROM 'table_name'
13. SELECT (`columns`) FROM 'table_name'
14. UPDATE 'table_name' SET 'column = value' WHERE 'column = value'
15. UPDATE 'table_name' SET 'column = value'
16. UPDATE 'table_name' SET 'column1 = value1', 'column2 = value2', 'column3 = value3', .....
17. UPDATE 'table_name' SET 'column1 = value1', 'column2 = value2', 'column3 = value3', ..... WHERE 'column = value'
18. DELETE FROM 'table_name'
19. DELETE FROM 'table_name' WHERE 'column = value'


### **Constraints**
This version currently supports the following constraints
NULL
NOT NULL
DEFAULT
