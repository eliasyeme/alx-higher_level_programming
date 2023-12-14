# 0x0F-python-object_relational_mapping
---
## Tasks 
### 0. Get all states
Write a script that lists all `states` from the database `hbtn_0e_0_usa`:
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- You must use the module `MySQLdb` (`import MySQLdb`)
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

```bash
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./0-select_states.py root root hbtn_0e_0_usa
(1, 'California')
(2, 'Arizona')
(3, 'Texas')
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$
```
**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x0F-python-object_relational_mapping`
- File: `0-select_states.py`

### 1. Filter states
Write a script that lists all `states` with a `name` starting with `N` (upper N) from the database `hbtn_0e_0_usa`:
- Your script should take 3 arguments: `mysql username`, `mysql password` and `database name` (no argument validation needed)
- You must use the module `MySQLdb (import MySQLdb)`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

```bash
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./1-filter_states.py root root hbtn_0e_0_usa
(4, 'New York')
(5, 'Nevada')
guillaume@ubuntu:~/0x0F$
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x0F-python-object_relational_mapping`
- File: `1-filter_states.py`

### 2. Filter states by user input
Write a script that takes in an argument and displays all values in the `states` table of `hbtn_0e_0_usa` where `name` matches the argument.
- Your script should take 4 arguments: `mysql username`, `mysql password`, `database name` and `state name` searched (no argument validation needed)
- You must use the module `MySQLdb (import MySQLdb)`
- Your script should connect to a MySQL server running on `localhost` at port `3306`
- You must use `format` to create the SQL query with the user input
- Results must be sorted in ascending order by `states.id`
- Results must be displayed as they are in the example below
- Your code should not be executed when imported

```bash
guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql
-- Create states table in hbtn_0e_0_usa with some data
CREATE DATABASE IF NOT EXISTS hbtn_0e_0_usa;
USE hbtn_0e_0_usa;
CREATE TABLE IF NOT EXISTS states ( 
    id INT NOT NULL AUTO_INCREMENT, 
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
INSERT INTO states (name) VALUES ("California"), ("Arizona"), ("Texas"), ("New York"), ("Nevada");

guillaume@ubuntu:~/0x0F$ cat 0-select_states.sql | mysql -uroot -p
Enter password: 
guillaume@ubuntu:~/0x0F$ ./2-my_filter_states.py root root hbtn_0e_0_usa 'Arizona'
(2, 'Arizona')
guillaume@ubuntu:~/0x0F$
```

**Repo:**
- GitHub repository: `alx-higher_level_programming`
- Directory: `0x0F-python-object_relational_mapping`
- File: `2-my_filter_states.py`