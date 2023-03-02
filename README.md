### Prerequisites:
  - Django
    - \<details here\>
  - Docker:
    - Docker Engine:
      - 
    - Docker Compose:
      - 
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
