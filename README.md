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
