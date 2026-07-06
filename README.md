# RadioRussia

De russische overheid wil een goede verdeling van zendfrequenties. Er zijn precies zeven types zendmasten (transmitters) beschikbaar, voor het moment bekend als type A t/m type G. Voor een goede verdeling is het noodzakelijk dat twee aangrenzende provincies niet dezelfde zendertypes hebben. Omdat wiskundigen van de russische overheid de details van de optimale oplossing niet precies kennen hebben ze ook wat kaarten van kleinere landen ter hand genomen, in de hoop het probleem wat beter te gaan begrijpen en tot een goede oplossing te komen.

## Aan de slag

### Vereisten

Deze codebase is volledig geschreven in Python (>=3.13). In pyproject.toml staan alle benodigde packages om de code succesvol te draaien. Deze zijn gemakkelijk te installeren via pip dmv. de volgende instructie:

```
pip install -e .
```

### Gebruik

Na installatie is de package te draaien met `python -m radio_russia`, met twee
subcommando's: `algorithm` en `experiment`.

**Let op:** commando's (en de standalone visualisatiescripts) verwachten dat je
ze vanuit de root van de repository draait, aangezien paden naar `data/`,
`experiments/` en `results/` relatief zijn ten opzichte van de working
directory.

Een los algoritme draaien op een dataset:

```
python -m radio_russia algorithm hillclimber --iterations 2000 --visualise
```

Zie `python -m radio_russia algorithm --help` voor alle beschikbare algoritmes en opties.

De experimenten in `/experiments` zijn reproduceerbaar via hun bijbehorende
JSON-configuratiebestand:

```
python -m radio_russia experiment experiments/depth_first/depth_first.json
```

De resultaten van een experiment worden geplot door de bijbehorende scripts in
`/visualisation`. Elk script staat op zichzelf en is los te draaien nadat het
experiment is uitgevoerd, bijvoorbeeld:

```
python visualisation/depth_first/depth_first_memory_graph.py
```

### Structuur

De hierop volgende lijst beschrijft de belangrijkste mappen en files in het project, en waar je ze kan vinden:

- **/radio_russia**: bevat alle code van dit project
  - **/radio_russia/algorithms**: bevat de code voor algoritmes
  - **/radio_russia/classes**: bevat de drie benodigde classes voor deze case
  - **/radio_russia/visualisation**: bevat de bokeh code voor de visualisatie
- **/data**: bevat de verschillende databestanden die nodig zijn om de graaf te vullen en te visualiseren
- **/experiments**: bevat de scripts en JSON-configuraties om de experimenten te draaien
- **/visualisation**: bevat de scripts die de resultaten van de experimenten plotten
  - **/visualisation/comparisons**: bevat de scripts die resultaten van meerdere experimenten met elkaar vergelijken

## Auteurs
- Quinten van der Post
- Wouter Vrielink
- Okke van Eck
