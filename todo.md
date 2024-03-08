# Notities contactmomenten

## Hoe run ik lokaal de flake8 code checks
```
docker build -t porrima_web:latest .
docker run --rm -v ${pwd}:/library/porrima porrima_web:latest flake8
```

(.git folder hooks, pre-commit hooks is iets om te onderzoeken.
Dit zijn shell scripts die activeren bij specifieke events, waardoor je de lokale test commands niet manueel meer moet uitvoeren.)

## seeden database

Django fixures is een manier om een database te seeden met dummy data voor development

#### interessante links hiervoor
https://docs.djangoproject.com/en/5.0/howto/initial-data/#:~:text=A%20fixture%20is%20a%20collection,the%20manage.py%20dumpdata%20command

https://dev.anet.be/porrima/cover/b/any/thumbnail?default=nocoverfound&isbn=0-87474-433-4&isbn=9780444594044

## Vragen rond de database
*Hoe moet de database werken, moet themis een appart project zijn met zijn eigen database of 
moet ik die van cover aanspreken? Is dit mogelijk en hoe?*

http://localhost:8014/cover/check/b/ scraped alle mogelijke coverfoto's van de verschillende clients.

**uitbreiding**
```
http://localhost:8014/cover/check/b/detail/
```
een suburl die alle covers toont, maar met een bepaalde predictie van Themis. Hierna zou er gefilterd kunnen worden op basis van:
- algemeen 'goed' of 'slecht'
- tussen parameters “vanDatum” en “totDatum”
- kunnen filteren op annotatie: "te veel witruimte", "gedraaid", "slechte kwaliteit", "Fake cover"

IF statement in de view gaat checken op parameter, gaat annotaties tonen en filters, dropdowns met annotaties.
```
http://localhost:8014/cover/choose/b/isbn/9780444594044
```
Hier moeten de labels toegewezen kunnen worden.
