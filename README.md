# Uitbreiding Coverserver UAntwerpen
## Themis
Themis *Griekse godin van orde* is een Model ontwikkeld voor het onderscheiden van goede en slechte coverfoto's.

## Deze Repo
Deze repo dient voor het ontwerpen van mijn model, dat op slimme manier kan omgaan met digitale afbeeldingen.
In eerste instantie zal dit model getraind en getest worden met covers van boeken,
om zo goede en slechte covers van elkaar te kunnen onderscheiden.

Het model is geïntegreerd in de codebase van porrima, de software die in de bibliotheken draait. Wegens confidentialiteit hou ik de code strikt gescheiden.
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


## Mogelijke toekomstige projecten DI voor Anet
*(in overeenstemming met Bart Moelans van Anet)*

### Cover locken -> popup api themis
Wanneer er een cover gescraped wordt en deze is slecht wordt deze "gelocked" in de cover applicatie. Dit zorgt ervoor dat deze cover niet meer gescraped kan worden, hij komt op een blacklist als het ware. Het zou fijn zijn moest er na het locken een popup verschijnen die het mogelijk maakt om een annotatie toe te voegen in de themis database. 

Bekijk zeker de documentatie van de cover- & themisapplicatie in porrima om dit beter te begrijpen.

### Bijsnijden van afbeeldingen
Anet wil al lang een manier om afbeeldingen te kunnen bijsnijden. Dit zou ergens in de cover applicatie moeten worden geïntegreerd. In eerste instantie zou een manuele tool al veel zijn. Op termijn kan er gekeken worden naar een geautomatiseerde tool.
Door de integratie van Themis worden er annotaties bijgehouden voor slechte covers. Een van deze annotaties is "te veel witruimte", dit kan hiervoor nuttig zijn.

### data:img
Op dit moment is er nog geen manier om met data:img files te werken. Er kan alleen met urls worden gewerkt zoals deze: https://www.sjoppertjes.com/storage/2023/12/57595.jpg. Het zou interessant zijn om een manier te vinden om hiermee te kunnen werken.

### opkuisen op basis van gelijkende covers
Er zijn veel manieren om gelijkende covers te herkennen, verwijderen of filteren. Er zou gekeken moeten worden naar een manier om dit te doen met bijvoorbeeld:
- een management tool
- een cluster algoritme
- vector databases

### Verbetering algoritme dat generic cover-not-found afbeeldingen filtert

We weten van bepaalde servers dat deze een standaard "cover-not-found" hebben, bijvoorbeeld voor mijnbibliotheek (https://bitbucket.org/anetbrocade/porrima/src/master/cover/client/BibBe/client.py) is dat https://bitbucket.org/anetbrocade/porrima/src/master/cover/static/no_cover/mijnbibbe_no_cover.jpeg

Als ik cover binnenhaal test ik dan ook of de binnengehaalde cover gelijkt op deze cover. Zie _is_valid_cover in bijvoorbeeld https://bitbucket.org/anetbrocade/porrima/src/master/cover/client/BibBe/client.py. Dit lijkt zijn werk al jaren te doen.


Nu is er recent een cover client bijgekomen, MoreBooks waarbij we pas achteraf merkte dat deze ook zo een standaard "cover-not-found"-image had. Nu we hadden reeds een management commando om slechte covers te vinden en op te kuisen (bijvoorbeeld covers die maar 1pixel groot zijn) => https://bitbucket.org/anetbrocade/porrima/src/master/cover/management/commands/cover_inspect.py
Dus mijn idee, ik maak een extra functie def nocover , ga over alle covers en vergelijk deze met gekende "cover-not-found"-image in.
Echter werd al snel duidelijk dat de methode met ImageChops.difference veel False positives geeft.
Dus ik kijk uit naar een functie die beter presteert.

Ik ga zeker 2 versies nodig hebben. 1 die die files vergelijkt, maar ook 1 die met reeds geladen images kan werken. Concreet wil ik de "cover-not-found" preprocessen en hiermee functie oproepen en niet voor elke cover, elke "cover-not-found"-image opnieuw laden.

### Kunst op de campus
Soms komt men ergens een kunstwerk tegen en is de vraag, is dit al geïnventariseerd. 
Maar ook, klopt de locatie van dit schilderij met locatie volgens het systeem.
Door een foto te trekken zou je een query by picture kunnen doen en zo meer info over het werk te krijgen.

Iets soortgelijks zou ook voor de covers gebruikt kunnen worden.
Vandaar is het belangrijk om de toepassing zo breed mogelijk te maken.