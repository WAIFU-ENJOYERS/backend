### Prerequisites:
  - Django
    - \<details here\>
  - Ufw (firewall set-up):
    - (sudo) apt-get install ufw
    - ufw enable
    - ufw allow in on docker0
    - ufw allow 5432/tcp
  - Docker:
    - Docker Engine:
      - apt-get install \<the below\>
        - ca-certification
        - curl
        - gnupg
        - lsb-release
    - Docker Compose:
      - apt-get install \<the below\>
        - docker-ce
        - docker-ce-cli
        - containerd.io
        - docker-buildx-plugin
        - docker-compose-plugin
  - Python's dependencies:
    - psycopg2
    - json
    - pytest
    
### Database setup:
  - Run init-script.sh in db-stuff/
    - To check whether the database is set-up sucessfully, do (sudo) docker ps -a
      - Find the database named "db-db-1", unless that name already exist, then find the lastest created database that is around the same time you ran the script
    - Or when you ran the script, the output at the end should an ID of the docker, it should be a string mixed with digits of approximately 20 in length
  - Run waifu-converter. Make sure that it takes in waifus.json properly (Change directory to db-stuff/)
  - To test the database:
    - On VSCode:
      - Install PostgreSQL extensions.
      - Open up the command palette (CTRL + SHIFT + P [Windows])
      - In command palette, type in PostgreSQL: Add Connection
        -
      - Make a SQL Query file, you can also find PostgreSQL: New Query in command palette
        -
      - In command palette, type in PostgreSQL: Select Connection
        -
      - With the SQL Query file focused, on command palette, type in PostgreSQL: Run Query
        - 
    - On PyCharm
      - WIP 
    - Or just run the automated test in test/
      - Do "pytest" on your cmd
        - If you don't have it, install it
      - If you see assertion returns, then it's all good, hopefully
        - If not, the table is probably not setup properly. (Or the whole process doesn't work)

```
Table Waifu {
  waifu_id int [pk, increment]
  name string [not null]
  likes int [not null]
  display_picture string [not null]
}
```

### TODO:
```
Table score {
  score_id int [pk, increment]
  points int
}
```

### Framework:
  - Backend: Django
  - Database: PostgresSQL
