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
└── README.md
└── usecase_interface.py
```

## Brukstilfeller implementert

1. Opprette treningssenter, saler, utstyr, brukere, treninge og mer (Python + SQL).

2. Booke trening for en spesifikk bruker (Python + SQL).

3. Registrere oppmøte for en trening (Python + SQL).

4. Ukeplan for alle treninger i en gitt uke (Python + SQL).

5. Personlig besøkshistorie for en bruker (SQL).

6. Svartelisting etter tre prikker innen 30 dager (Python + SQL).

7. Finne brukere med flest gruppetimer i en måned (Python + SQL).

8. Finne to brukere som trener sammen flest ganger (SQL).

Alle brukstilfeller er implementert i SQL, med Python-filer i tilegg der oppgaven krever det eller for å enkelt lese og kjøre SQL-filene.

## Hvordan kjøre database applikasjonen
Database applikasjon er tekstbasert og utføres i terminalen dersom man kjører *usecase_interface.py*. Brukeren presenteres med en meny med ulike valg som støtter de implementerte brukstilfellene.

Database filen lagt ved i dette prosjektet er tom og for å bygge opp databasen må man utføre alle valgenen i menyen. Menyen består av valg fra 0-8, for at applikasjonen skal kjøre uten feil anbefales det å kjøre valgene i stigende rekkefølge.

Alle brukstilfellene krever at du bekrefter valget ditt, og noen ønsker at du skriver inn spesifikke krav for utføringen. Dette kan skrives direkte i terminalen der du kjører applikasjonen. Brukstilfellet vil forklare formatet du behøver å skrive på for å tilfredstille kravene til funksjonene. 

Dersom man har kjørt alle brukstilfellene eller ønsker å starte databasen på nytt, kan man kjøre brukstilfelle 0, som vil tilbakestille alle tabellene til å være tomme.

## Merknadder til implementasjon av databasen
* Det er ikke implementert en sjekk av dato og tid for booking eller registrering av en gruppetime før den implementeres. Dette ble aktuvt utelatt da det er usikkert når bruker skal utføre brukertilfellene, og vi ønsket ikke at feilmeldinger skulle oppstå dersom de prøver å melde seg på en time før eller etter fristen.
* Dersom brukertilfelle spesifiserte at handlingen skulle håndtere et tilfelle for Johnny har vi valgt at tekstapplikasjonen kun skal utføre dette for Johnny, selv om fler av python filene tillater å utføre handlingen for ulike brukere. Dette er gjort slik at det er lett for brukere å utføre handlingen uten å måtte skrive inn informasjon angående gruppetimer eller brukere. 
## KI deklarasjon


## Gruppeinformasjon
Gruppenummer: 134
Gruppemedlemmer: Eline Jåsund, Gina Giske, Catrin Johansen 