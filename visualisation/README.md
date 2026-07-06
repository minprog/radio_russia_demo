# Visualisatie

Elk script leest de resultaten van een experiment uit `results/<folder>/` en
genereert daaruit een grafiek of tabel als `.png`, opgeslagen in diezelfde
`results/<folder>/`-map (niet in de `visualisation`-map zelf). Een script draai
je met bijvoorbeeld:

```
python -m visualisation.depth_first.depth_first_table
```

## Per-algoritme mappen
Bevatten scripts die de resultaten van één algoritme visualiseren, zoals een
tabel met kerncijfers (bezochte staten, oplossingen, doelwaarde) of een grafiek
van het geheugengebruik tijdens het zoeken.
- `depth_first/`, `breadth_first/`, `greedy/`, `hillclimber/`, `simulatedannealing/`, `random/`

## comparisons
Bevat scripts die resultaten van meerdere experimenten met elkaar vergelijken,
bijvoorbeeld de uitputtende zoekalgoritmes onderling, of de invloed van
parameters zoals mutatiegrootte (hillclimber) en starttemperatuur (simulated
annealing) op de prestaties.
