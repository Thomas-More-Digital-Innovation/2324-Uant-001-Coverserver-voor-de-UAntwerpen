# Notities contactmomenten

## Hoe run ik lokaal de flake8 code checks
```
docker build -t porrima_web:latest .
docker run --rm -v ${pwd}:/library/porrima porrima_web:latest flake8
```

(.git folder hooks, pre-commit hooks is iets om te onderzoeken.
Dit zijn shell scripts die activeren bij specifieke events, waardoor je de lokale test commands niet manueel meer moet uitvoeren.)

## Nuttige commandos
```
migratie voor specifieke db
python manage.py makemigrations
python manage.py migrate cover --database=cover_db

http://localhost:8014/cover/choose/b/isbn/9780444594044
http://localhost:8014/cover/choose/b/isbn/9780444594044?datefrom=2024-01-29&dateto=2024-02-23

docker container aan terminal
docker ps 
docker attach "the id"

tests runnen
docker build -t porrima_web:latest .
docker run --rm -v ${pwd}:/library/porrima porrima_web:latest flake8
docker run --rm -e PORRIMA_ENV_FILE=/library/porrima/env/test.env -v ${pwd}:/library/porrima porrima_web:latest pytest --cov=/library/porrima/cover --cov=/library/porrima/stats --cov=/library/porrima/brocade --cov=/library/porrima/api/client --cov=/library/porrima/api/numbertype --cov-report=term-missing:skip-covered /library/porrima
```

## seeden database

Django fixures is een manier om een database te seeden met dummy data voor development

#### interessante links hiervoor
https://docs.djangoproject.com/en/5.0/howto/initial-data/#:~:text=A%20fixture%20is%20a%20collection,the%20manage.py%20dumpdata%20command

https://dev.anet.be/porrima/cover/b/any/thumbnail?default=nocoverfound&isbn=0-87474-433-4&isbn=9780444594044
