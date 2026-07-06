# Experimenten

Elke submap bevat één algoritmefamilie: een `<naam>_experiment.py`-module met de
uitvoerbare functies, en per run één JSON-bestand. Een run-JSON bevat `data_folder`
(welke map onder `data/<folder>` geladen wordt), `function` (naam van de functie die
uit de module aangeroepen wordt) en `params` (keyword-argumenten voor die functie).
Een run start je met:

```
python -m radio_russia experiment experiments/<folder>/<run>.json
```

## depth_first
Uitputtende zoektocht over zenderplaatsingen.
- `depth_first.json` — gewone depth-first search
- `branchandbound.json` — depth-first search met branch-and-bound pruning

## breadth_first
Uitputtende zoektocht, breadth-first in plaats van depth-first.
- `breadth_first.json` — gewone breadth-first search
- `best_first.json` — best-first search (priority queue op basis van kosten)

## greedy
Heuristieken die zenders in één keer gulzig plaatsen.
- `random_greedy.json` — herhaalde gerandomiseerde gulzige plaatsing
- `greedy.json` — deterministische gulzige plaatsing

## hillclimber
Lokale zoektocht die een oplossing steeds muteert en verbeteringen behoudt.
- `hillclimb.json` — één hillclimber-run
- `hillclimber_averages.json` — gemiddelde resultaten over meerdere runs
- `hillclimber_xopt_comparison.json` — vergelijkt prestaties bij verschillende mutatiegroottes

## simulatedannealing
Lokale zoektocht zoals hillclimber, maar accepteert slechtere oplossingen met een
kans die afneemt ("afkoelt") naarmate de tijd vordert.
- `simulateannealing.json` — één simulated-annealing-run
- `simulatedannealing_averages.json` — gemiddelde resultaten over meerdere runs
- `simulatedannealing_temperature_comparisons.json` — vergelijkt prestaties bij verschillende starttemperaturen

## random
- `baseline.json` — volledig willekeurige plaatsing, gebruikt als baseline ter vergelijking

## Resultaten
Elke run schrijft zijn uitvoer weg naar `results/<folder>/`, geplot door de
bijbehorende scripts in `/visualisation`.
