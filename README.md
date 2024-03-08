# Uitbreiding Coverserver UAntwerpen
## Themis
Themis *Griekse godin van orde* is een Model ontwikkeld voor het onderscheiden van goede en slechte coverfoto's.

## Deze Repo
Deze repo dient voor het ontwerpen van mijn model, dat op slimme manier kan omgaan met digitale afbeeldingen.
In eerste instantie zal dit model getraind en getest worden met covers van boeken,
om zo goede en slechte covers van elkaar te kunnen onderscheiden.

Deze zal later geïntegreerd worden in de codebase van Porrima 
en dan kan ook op termijn gekeken worden om dit model ook toe te passen binnen andere gebieden.
```
└───cover
    └───tools
            badCoverScraper.py          -> scraper voor slechte covers
            cleanser.py                 -> converteert alle images naar jpg in google drive (en verwijdert zo corrupted images)
            convertToJPG.py             -> zelfde als cleanser maar dan lokaal
            goodCoverScraper.py         -> scraper voor goede covers
            studie.ipynb                -> zelfstudie op de mnist dataset
            themis.ipynb                -> trainen van Themis model
```
## Probleemstelling covers
Anet heeft een uitgebreide catalogus en natuurlijk zegt een foto meer dan duizend woorden, 
dus annoteren we zoekresultaten van boeken ook met een cover. 
Om deze cover te tonen heeft Anet een eigen ontwikkelde cover server. 
Deze doet naar de klanten toe een behoorlijke job, 
maar zowel naar klanten als beheerders toe kan hier nog aan verbeterd worden.

Door een ML-model te trainen wordt het onderscheiden van goede en slechte covers vergemakkelijkt.
#
### Mogelijke toekomstige projecten DI voor Anet
#### Kunst op de campus
Soms komt men ergens een kunstwerk tegen en is de vraag, is dit al geïnventariseerd. 
Maar ook, klopt de locatie van dit schilderij met locatie volgens het systeem.
Door een foto te trekken zou je een query by picture kunnen doen en zo meer info over het werk te krijgen.

Iets soortgelijks zou ook voor de covers gebruikt kunnen worden.
Vandaar is het belangrijk om de toepassing zo breed mogelijk te maken.