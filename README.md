Projectvoorstel: Coverserver

Klanten
  Susanna De Schepper, coördinator metadata Anet
  Jef De Ridder, expter acquisitie en metadatabeheer

Probleemstelling

  We hebben een uitgebreide catalogus en natuurlijk een foto zegt meer dan duizend woorden, dus annoteren we zoekresultaten van boeken ook met een cover.
  Om deze cover te tonen hebben we een eigen ontwikkelde cover server.
  Deze doet naar de klanten toe een behoorlijke job maar zowel naar klanten als beheerders toe kan hier nog aan verbeterd worden.
    Mogelijke uitbreidingen:
    • Online bijwerken van afbeeldingen
    • Covers ook als URI uploaden, dus met data:image/jpeg;base64,/
    • (Semi-)automatisch herkennen van slechte covers
    • Annoteren van manuele aanpassingen (beheerders doen aanpassingen, maar momenteel is er geen manier om aan te geven waarom de automatisch gevonden cover niet goed genoeg was
    • Mobile friendly interface
    • Gamification
    • Ook auteursinfo verzamelen
    • Met Smarthpone ISBN scannen, huidige cover zien en eventueel foto nemen van cover als alternatief
    
Technologieën
  • Django (webapplicatie-framework geschreven in Python volgens het MVC-model)
  • Python
  • Git (waarbij we intern Bitbucket gebruiken als platform)
  • OpenCV en/of andere computervisie softwarebibliotheken
  • Docker
  • SQL
  
Roadmap
  Er is geen harde deadline voor dit project maar we zouden wel graag volgende eerste milestones zien:
  • Een kleine webapp naar keuze gemaakt in Django binnen een Docker-container met een versiebeheer. Gewoon kwestie van deze technologieën (meer) onder de knie te krijgen bijvoorbeeld op basis van https://www.djangoproject.com/start/.
  • Het lokaal runnen van onze cover server en vertrouwd worden met de opbouw.
  In samenspraak kiezen welke uitbreiden worden geïmplementeerd met bijhorende roadmap en zodanig extra milestones definiëren.
