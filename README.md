# DB2
Dette prosjektet inneholder Python og SQL filer for å konstruere og bruke en DB Browser for SQLite i forbindelse med prosjektet for TDT4145 Datamodellering og databasesystemer. Prosjektet modellerer en database for SiT Trening i Trondheim og har implementert kode for å fullføre flere ulike brukertilfeller.

## Filstruktur
```text
DB2/
├── table_construction/
│   ├── table_construction.py
│   └── table_construction.sql
│
├── usecase/
│   ├── usecase_1/
│   │   ├── usecase_1.py
│   │   └── usecase_1.sql
│   │
│   ├── usecase_2/
│   │   ├── usecase_2.py
│   │   └── usecase_2.sql
│   │
│   ├── usecase_3/
│   │   ├── usecase_3.py
│   │   └── usecase_3.sql
│   │
│   ├── usecase_4/
│   │   └── usecase_4.py
│   │
│   ├── usecase_5/
│   │   └── usecase_5.py
│   │
│   ├── usecase_6/
│   │   ├── usecase_6.py
│   │   └── usecase_6.sql
│   │
│   ├── usecase_7/
│   │   ├── usecase_7.py
│   │   └── usecase_7.sql
│   │
│   └── usecase_8/
│       ├── usecase_8.py
│       └── usecase_8.sql
│
├── .gitignore
├── DB2.db
├── README.md
└── usecase_interface.py
```

## Brukstilfeller implementert

1. Opprette tabeller for treningssenter, saler, fasiliteter, brukere, gruppetimer og mer (Python + SQL).

2. Booke Spin60 for Johnny (Python + SQL).

3. Registrere oppmøte av Spin60 for Johnny (Python + SQL).

4. Ukeplan for alle treninger i en gitt uke (Python + SQL).

5. Personlig besøkshistorie for Johnny (SQL).

6. Svartelisting av Johnny etter å få tre prikker innen 30 dager (Python + SQL).

7. Finne brukere med flest gruppetimer i en måned (Python + SQL).

8. Finne to brukere som trener sammen (SQL).

Alle brukstilfeller er implementert i SQL, med Python-filer i tilegg der oppgaven krever det eller for å enkelt lese og kjøre SQL-filene.

## Hvordan kjøre database applikasjonen
Database applikasjon er tekstbasert og utføres i terminalen dersom man kjører *usecase_interface.py*. Brukeren presenteres med en meny med ulike valg som støtter de implementerte brukstilfellene.

Database filen lagt ved i dette prosjektet er tom og for å bygge opp databasen må man utføre alle valgenen i menyen. Menyen består av valg fra 0-8, for at applikasjonen skal kjøre uten feil anbefales det å kjøre valgene i stigende rekkefølge.

Alle brukstilfellene krever at du bekrefter valget ditt, og noen ønsker at du skriver inn spesifikke krav for utføringen. Dette kan skrives direkte i terminalen der du kjører applikasjonen. Brukstilfellet vil forklare formatet du behøver å skrive på for å tilfredstille kravene til funksjonene. 

Dersom man har kjørt alle brukstilfellene eller ønsker å starte databasen på nytt, kan man kjøre brukstilfelle 0, som vil tilbakestille alle tabellene til å være tomme.

### Brukertilfelle 0
Vi har valgt å legge til brukertilfelle 0 for å gi bruker en mulighet til å laste inn de tomme tabellene i databasen. Dette er gjort separat ifra å legge inn dataen i databasen slik at bruker kan gjøre brukertilfelle 0 dersom de ønsker å tømme databasen fra data. 

![Resultat av output for brukertilfelle 0](images/usecase_0_result.png)

### Brukertilfelle 1

![Resultat av output for brukertilfelle 1](images/usecase_1_result.png)

### Brukertilfelle 2

![Resultat av output for brukertilfelle 2](images/usecase_2_result.png)

### Brukertilfelle 3

![Resultat av output for brukertilfelle 3](images/usecase_3_result.png)

### Brukertilfelle 4

![Resultat av output for brukertilfelle 4](images/usecase_4_result.png)

### Brukertilfelle 5

![Resultat av output for brukertilfelle 5](images/usecase_5_result.png)

### Brukertilfelle 6

![Resultat av output for brukertilfelle 6](images/usecase_6_result.png)

### Brukertilfelle 7

![Resultat av output for brukertilfelle 7](images/usecase_7_result.png)

### Brukertilfelle 8

![Resultat av output for brukertilfelle 8](images/usecase_8_result.png)

## Merknadder til implementasjon av databasen
* Det er ikke implementert en sjekk av dato og tid for booking eller registrering av en gruppetime før den implementeres. Dette ble aktuvt utelatt da det er usikkert når bruker skal utføre brukertilfellene, og vi ønsket ikke at feilmeldinger skulle oppstå dersom de prøver å melde seg på en time før eller etter fristen.
* Dersom brukertilfelle spesifiserte at handlingen skulle håndtere et tilfelle for Johnny har vi valgt at tekstapplikasjonen kun skal utføre dette for Johnny, selv om fler av python filene tillater å utføre handlingen for ulike brukere. Dette er gjort slik at det er lett for brukere å utføre handlingen uten å måtte skrive inn informasjon angående gruppetimer eller brukere. 

## Endringer gjort i skjema fra første innlevering

## KI deklarasjon


## Gruppeinformasjon
Gruppenummer: 134

Gruppemedlemmer: Eline Jåsund, Gina Giske, Catrin Johansen 