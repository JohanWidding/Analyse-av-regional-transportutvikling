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

Kilder:

Tabell 06913: Befolkning og endringer, etter statistikkvariabel, region og år
Befolkningsdata er hentet fra:
https://www.ssb.no/statbank/table/06913/tableViewLayout1/

07849: Registrerte kjøretøy, etter statistikkvariabel, region, type kjøring, drivstofftype og år
Bilpark per region:
https://www.ssb.no/statbank/table/07849/tableViewLayout1/

09391: Hovedtall fylkesfordelt nasjonalregnskap, etter statistikkvariabel, region og år
Bruttonasjonalprodukt:
https://www.ssb.no/statbank/table/09391/tableViewLayout1/

Trafikkutvikling
vegtrafikkindekser 2003 - 2023
https://www.vegvesen.no/fag/trafikk/trafikkdata/trafikkutvikling/


Fylkessammenslåingene som trådte i kraft i Norge har introdusert utfordringer knyttet til datagrunnlaget, særlig når det gjelder konsistens og sammenlignbarhet over tid. Tabeller og datasett som brukes i analyser har ofte ikke enhetlige tidsserier som reflekterer de sammenslåtte fylkene. For eksempel er det nasjonalregnskapet som ikke har oppdaterte regionale data, mens datasett som bilpark og befolkningsstatistikk har fulgt en sammenslått struktur. Videre er data fra Statens vegvesen (SVV) fordelt per år, noe som gjør at trafikkindeksen for ulike fylker reflekterer fylkesstrukturen som var gjeldende på det aktuelle tidspunktet. Eksempelvis eksisterte både Sør- og Nord-Trøndelag som separate fylker før 2017, men etter fylkessammenslåingen inngår de som én enhet. Siden trafikkdataene ofte er presentert som prosentvis økning i forhold til foregående år, innen samme region, kan det gi et skjevt bilde å slå sammen dataene. Å beregne gjennomsnittlig vekst for sammenslåtte fylker kan være problematisk dersom det er betydelige regionale forskjeller, ettersom dette kan maskere ulikheter og gi et feilaktig grunnlag for videre analyser.

I vurderingen av befolkningsgrunnlaget har det også vært nødvendig å fastsette hvilke aldersgrupper som skal inkluderes i analysen. Det er besluttet at befolkningen under 18 år ikke skal tas med i vurderingen av trafikkutviklingen. Begrunnelsen for dette er at denne aldersgruppen ikke selv kan kjøre bil og i større grad er avhengig av lokale transportmidler, snarere enn å generere trafikk over lengre avstander. Videre antas det at barn i byområder i større grad benytter kollektivtransport til lengre reiser, noe som gjør deres påvirkning på trafikkutviklingen marginal. Å ekskludere denne gruppen reduserer støy i datagrunnlaget og gir analyseresultater som er mer relevante for anvendelse i befolkningsprognoser for regioner, der kun voksne (18+) inngår.

Bruttonasjonalprodukt (BNP) representerer en kompleks variabel i denne sammenhengen. I Norge er det Statistisk sentralbyrå (SSB) som har ansvaret for å beregne omsetningen av varer og tjenester per region, en omfattende og krevende oppgave. Likevel er det ikke gitt at regional omsetning stammer fra varer og tjenester som produseres eller distribueres via veinettet. Eksempelvis fungerer Oslo som et nasjonalt senter for "white-collar"-arbeid, der mange hovedkontor leverer tjenester til andre deler av landet, mens råvarer og produkter ofte produseres og distribueres fra andre regioner. Dette kompliserer bruken av BNP som en indikator for veibasert transportaktivitet. I tillegg har Oslo lavere antall biler per innbygger enn resten av landet, noe som skyldes et bedre kollektivtilbud og høyere kostnader for bileierskap. Til tross for disse utfordringene er det relevant å inkludere BNP i analysene, med unntak av Oslo som en mulig ekstremverdi, ettersom regioner med sammenlignbare næringsstrukturer og befolkningsstørrelser antas å ha lignende BNP. Dette kan gi bedre grunnlag for å forstå de økonomiske drivkreftene bak regional trafikk og transportbehov.


Fylkene som ble slått sammen var som følger:

| Sammenslåing                     | Nytt fylkesnavn       | Ny fylkes-kommune fra |
|----------------------------------|-----------------------|-----------------------|
| Nord-Trøndelag og Sør-Trøndelag | Trøndelag             | 01.01.2018            |
| Hordaland og Sogn og Fjordane   | Vestland              | 01.01.2020            |
| Aust-Agder og Vest-Agder        | Agder                 | 01.01.2020            |
| Vestfold og Telemark            | Vestfold og Telemark  | 01.01.2020            |
| Oppland og Hedmark              | Innlandet             | 01.01.2020            |
| Buskerud, Akershus og Østfold   | Viken                 | 01.01.2020            |
| Troms og Finnmark               | Troms og Finnmark     | 01.01.2020            |


| Sammenslåtte fylker              | Oppløst til fylker            | Oppløsning fra |
|----------------------------------|-------------------------------|----------------|
| Viken                            | Akershus, Buskerud, Østfold   | 01.01.2024     |
| Vestfold og Telemark             | Vestfold, Telemark            | 01.01.2024     |
| Troms og Finnmark                | Troms, Finnmark               | 01.01.2024     |

Data om transportarbeidet kommer fra Statens vegvesen og har blitt presentert i årlige rapporter i .pdf format. Utofrdringen med dette var å overføre denne dataen til et sammenfattet tidserie fordelt per region i en enkelt fil. Noe som har blitt gjort av Chat GPT og manuell kontroll av meg i etterkant. Ta forbehold om at det kan ha forekokmmet feil i denne prosessen og føl deg fri til å kontrollere dette selv. 

