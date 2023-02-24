```
Table Waifu {
  waifu_id int [pk, increment]
  name string [not null]
  likes int [not null]
  display_picture string [not null]
}

Table score {
  score_id int [pk, increment]
  points int
}
```

### Framework:
  - Backend: Django
  - Database: PostgresSQL
