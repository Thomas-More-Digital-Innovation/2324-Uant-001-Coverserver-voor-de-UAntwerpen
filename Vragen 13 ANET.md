Notes 1/3 ANET

- Hoe run ik lokaal de flake8 code checks
```
docker build -t porrima_web:latest .
docker run --rm -v ${pwd}:/library/porrima porrima_web:latest flake8
```

.git folder hooks, pre-commit hooks is iets om te onde

django fixures is een manier om te seeden

https://docs.djangoproject.com/en/5.0/howto/initial-data/#:~:text=A%20fixture%20is%20a%20collection,the%20manage.py%20dumpdata%20command.
Django
https://dev.anet.be/porrima/cover/b/any/thumbnail?default=nocoverfound&isbn=0-87474-433-4&isbn=9780444594044
The web framework for perfectionists with deadlines.
- Hoe moet de database werken, moet themis een appart project zijn met zijn eigen database of 
moet ik die van cover aanspreken? Is dit mogelijk en hoe?

boek invoegen, show command wordt opgeroepen en anders live scrapen
http://localhost:8014/cover/check/b/ is voor de tijd gescraped
na de b een suburl die alle covers toont, maar met een bepaalde predictie
dropdown, toon goed, toon slecht, sub
b/detail dan zie je alle covers berekenen op kwaliteit en dan pas filteren
if statement in de view gaat checken op parameter, gaat annotaties tonen en filters, dropdowns met annotaties.

choose/b/isbn is het interessant om labels te geven

b/
andere sqlite maken

Wat moet er in de templates kunnen gebeuren:
    - Een lijst met kunnen ophalen van covers gescraped  tussen parameters “vanDatum” en “totDatum”.
    - Kunnen filteren op "te veel witruimte", "gedraaid", "slechte kwaliteit", "Fake cover", maar ook algemeen "slecht", dat deze moet groeperen.

Is dit voor in cover of in themis?

Maak ik de themis applicatie, die op basis van een afbeelding een waarde/dict teruggeeft tussen 0 & 1 dat goed en slecht voorstellen?


docker run -it --rm -e PORRIMA_ENV_FILE=/library/porrima/env/local.env -v ${pwd}:/library/porrima porrima_web:latest bash
