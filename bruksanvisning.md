## Hvordan kjøre database applikasjonen
Database-applikasjonen er tekstbasert og kjøres i terminalen dersom man kjører *usecase_interface.py* på følgende vis:
```python
python3 usecase_interface.py
```

Brukeren presenteres da med en meny der man kan velge hvilket brukstilfelle man ønsker å kjøre.

Når man har valgt brukstilfellet man ønsker å kjøre, vil man i mange av tilfellene få valget:
```python
"Ønsker du å gjøre dette? [Y/n]"
```

Her vil det være tilstrekkelig å trykke *Enter* dersom man ønsker å svare "Y", for "yes".

Database-filen [TreningDB.db](TreningDB.db) lagt ved i dette prosjektet er tom og for å bygge opp databasen må man utføre alle valgenen i menyen. Menyen består av valg fra 0-8, for at applikasjonen skal kjøre uten feil anbefales det å kjøre valgene i stigende rekkefølge.

Alle brukstilfellene krever at du bekrefter valget ditt, og noen ønsker at du skriver inn spesifikke krav for utføringen. Dette skrives direkte i terminalen der applikasjonen kjøres. Brukstilfellet vil forklare formatet du behøver å skrive på for å tilfredstille kravene til funksjonene.

Dersom man har kjørt alle brukstilfellene eller ønsker å starte databasen på nytt, kan man kjøre brukstilfelle 0. Dette vil tilbakestille alle tabellene til å være tomme.

### Brukstilfelle 0
Vi har valgt å legge til *Brukstilfelle 0* for å gi bruker mulighet til å lage de de tomme tabellene i databasen. Dette er gjort separat ifra å legge inn dataen i databasen slik at bruker kan gjøre Brukstilfelle 0 dersom de ønsker å tømme databasen fra data.

*For at applikasjonen skal kjøre må brukstilfelle 0 kjøres først*

![Resultat av output for Brukstilfelle 0](images/usecase_0_result.png)

### Brukstilfelle 1
Brukstilfelle 1 fyller databasen med eksempeldata som forklart i brukstilfellet.

![Resultat av output for Brukstilfelle 1](images/usecase_1_result.png)

### Brukstilfelle 2
Ved å kjøre brukstilfelle 2 booker man en Spin60 time for Johnny tirsdag 17. mars kl. 18:30. Output vil her være en bekreftelse på at bookingen er gjennomført. Dersom man prøver å booke en time før eksempeldataen er satt inn vil man få en feilmelding.

![Resultat av output for Brukstilfelle 2](images/usecase_2_result.png)

### Brukstilfelle 3
I brukstilfelle 3 registrerer man oppmøte for Johnny på gruppetimen fra brukstilfelle 2. Dersom man prøver å registrere oppmøte før man har booket timen hans vil man få en melding om at registreringen ikke kunne gjennomføres fordi man ikke er påmeldt timen.

![Resultat av output for Brukstilfelle 3](images/usecase_3_result.png)

### Brukstilfelle 4
Ved å velge brukstilfelle 4 vil man kunne se en ukentlig timeplan for gitt tidsperiode. Inputen man skal gi her er for eksempel *mandag*.

Som det står forklart når man kjører dette brukstilfellet er det kun lagt inn eksempeldata for mandag og tirsdag i uke 12, og ved å velge andre dager enn dette vil man ikke få noen resultater.

![Resultat av output for Brukstilfelle 4](images/usecase_4_result.png)

### Brukstilfelle 5
Brukstilfelle 5 viser besøkshistorien til Johnny.

![Resultat av output for Brukstilfelle 5](images/usecase_5_result.png)

### Brukstilfelle 6
I brukstilfelle 6 testes funksjonaliteten for å svarteliste et medlem. Etter man har valgt å svarteliste Johnny ved å gi han 3 prikker kan man velge å prøve å booke en time for han for å se at svartelistingen har blitt implementert.

![Resultat av output for Brukstilfelle 6](images/usecase_6_result.png)

### Brukstilfelle 7
Brukstilfelle 7 gir de medlemmene som har deltatt på flest gruppetimer i den gitte måneden. For å kjøre denne anbefales det å skrive følgende:

*2026-03*

Det er i denne perioden det er mest eksempeldata å basere spørringen på.

![Resultat av output for Brukstilfelle 7](images/usecase_7_result.png)

### Brukstilfelle 8
Ved å kjøre brukstilfelle 8 får man vite hvilke medlemmer som trener sammen, og hvor mange treninger de har vært på sammen.

For å løse denne oppgaven valgte gruppen å sjekke hvilke to medlemmer som har ankommet senteret sammen (innenfor 1 minutt av hverandre) mer enn 3 ganger de siste 3 månedene.

![Resultat av output for Brukstilfelle 8](images/usecase_8_result.png)