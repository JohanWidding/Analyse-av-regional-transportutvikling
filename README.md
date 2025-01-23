## Beskrivelse av datasettet
Datasettet inneholder informasjon om transportarbeid og befolkningsendringer, med kontroll for region. Det inkluderer blant annet prosentvis endring i befolkningen, transportarbeid, samt en regioninndeling. Dataene er tilrettelagt for analyser som tar sikte på å undersøke hvordan endringer i befolkning påvirker transportarbeid, samtidig som regionenes unike karakteristikker kontrolleres.

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

