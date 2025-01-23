## Analyse av regional transportutvikling

Det har vært et ønske om å få greie på hvordan befolkningsveksten påvirker Transportarbeidet i Norge. Transportarbeidet er i denne sammenheng et produkt av antall passasjerer og gjennomsnittlig reiselengde per region.

Datasettet kommer fra to kilder SSB og SVV. Fra SSB har jeg hentet data om befolknigng per år fordelt på regionene.

Datasettet inneholder informasjon om transportarbeid og befolkningsendringer, med kontroll for region. Det inkluderer blant annet prosentvis endring i befolkningen, transportarbeid, samt en regioninndeling. Dataene er tilrettelagt for analyser som tar sikte på å undersøke hvordan endringer i befolkning påvirker transportarbeid, samtidig som regionenes unike karakteristikker kontrolleres for.

# Resultater

avhengig variabel: "Trafikkarbeid"

### modeller og "Population_Percent_Change" sin koefisient med signifikansnivå
- `transport_prediction_with_population_and_region.py`: 0.8704***
- `region_population_ols_with_reduction.py`:           -0.0678

## Innholdsfortegnelse

1. **Resultater av analysene**  
    1.1. Prediksjon av transportarbeid ved hjelp av befolkningsendringer og regionkontroll (Script: `transport_prediction_with_population_and_region.py`)  
    1.2. Prediksjon av transportarbeid med dimensjonalitetsreduksjon (Script: `dimensionality_reduction_ols.py`)

2. **Kilde til datasettet**  
Datasettet er hentet fra interne registre og er bearbeidet for bruk i denne analysen. Dersom ytterligere detaljer om dataenes opprinnelse er nødvendige, kontakt prosjektansvarlig.

---

## Detaljer om analyser

### 1.1 Prediksjon av transportarbeid ved hjelp av befolkningsendringer og regionkontroll
Dette scriptet analyserer hvordan endringer i befolkningen påvirker transportarbeid, samtidig som effektene av ulike regioner kontrolleres. Regionen er kodet som dummyvariabler ved hjelp av one-hot encoding. Scriptet bruker en OLS-regresjon for å estimere sammenhengene.

**Script:** `transport_prediction_with_population_and_region.py`

### 1.2 Prediksjon av transportarbeid med dimensjonalitetsreduksjon
I denne analysen blir dimensjonaliteten i datasettet redusert ved å tilfeldig fjerne en andel av regionrelaterte dummyvariabler. Dette gjør at analysen unngår overtilpasning, samtidig som regionenes variasjon bevares. Analysen estimeres ved bruk av en OLS-regresjon.

**Script:** `dimensionality_reduction_ols.py`

---

## Kilde til datasettet
Datasettet kommer fra interne registre og inneholder anonymiserte og bearbeidede data som er egnet for analyser knyttet til transport og befolkningsendringer. Kontakt prosjektansvarlig for ytterligere detaljer.

Det har vært noen utfordringer med datagrunnlaget som resultat av fylkessammenslåingene som tredde i kraft ...

Det har også vært en vurdering av hvilke aldersgrupper som skulle inkluderes i befolknignsgrunnlaget. Jeg har vurdert at

Bruttonasjonalprodukt er i seg selv en vanskelig parameter å ta stilling til. I Norge er det SSB som tar på seg ansvaret for å regne på "varer og tjenester som omsettes per region", som er en passe omfattende og krevende jobb. VIdere, er det ikke gitt at regional omsettnign kommer av varer og tjenester som leveres på vegnettet. I Oslo for eksempel er det flere bedrifter som har hovedkontor, og leverer "white color" arbeid til resten av  landet der selve produktet eller råvaren produseres og sendes fra. I tillegg er antallet biler per person lavere her enn i resten av landet på grunn av bedre kollektivtilbud og høyere kostnader for å eie bil. Men når allt dette er sagt er det av interesse å kontorllere for BNP i regionene (Kansje droppe Oslo som en ekstremverdi) siden det er rimelig at regioner av tilsvarende samme størrelse og næring vil ha ligndende BNP.


Fylkene som ble slått sammen var som følger

Data om transportarbeidet kommer fra Statens vegvesen og har blitt presentert i årlige rapporter i .pdf format. Utofrdringen med dette var å overføre denne dataen til et sammenfattet tidserie fordelt per region i en enkelt fil. Noe som har blitt gjort av Chat GPT og manuell kontroll av meg i etterkant. Ta forbehold om at det kan ha forekokmmet feil i denne prosessen og føl deg fri til å kontrollere dette selv. 

