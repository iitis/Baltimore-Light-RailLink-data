[![DOI](https://zenodo.org/badge/839311612.svg)](https://zenodo.org/doi/10.5281/zenodo.13254841)


# Baltimore-Light-RailLink-data

Histograms of traffic data of Baltimore Light RailLink
Data supplied by the 

We acknowledge Swiftly’s GTFS-realtime API https://swiftly.zendesk.com/hc/en-us 
(accessed 11-31 January 2024) for supplying these real-time traffic data.

## To plot a histogram 

of passing times between selected stations use

```
hist --datafolder  ...  --direction
```

where: --datafolder (multiple) arguments of files input \outputs
       --direction  trains direction possible "n" north, "s" south "" both.

Plots are saved in ```\pics```.


Example plotter:

```
python3 hists.py --datafolder  "11012024_700/" "12012024_700/" "15012024_700/" "16012024_700/" "11012024_1500/" "12012024_1500/" "15012024_1500/" "16012024_1500/" --direction "n"
```

## Data description quality check

For data quality check, compare with manually collected data in folder ``description/Dane KG.xls``

For precise data/system description (in Polish) see folder ``description/expertises``

## Plaese cite

- M. Koniorczyk, K. Krawiec, L. Botelho, N. Bešinović, and K. Domino, "Solving rescheduling problems in heterogeneous urban railway networks using hybrid quantum-classical approach", Journal of Rail Transport Planning & Management, vol. 34, issue 100521, 05/2025, https://doi.org/10.1016/j.jrtpm.2025.100521

- K. Domino, E. Doucet, R. Robertson, B. Gardas, and S. Deffner, "On the Baltimore Light RailLink into the quantum future", Scientific Reports, vol. 15, issue 29576, 08/2025, 10.1038/s41598-025-15545-0

## Founding

The code was partially supported by Polish National Science Center under grant agreement number 2023/07/X/ST6/00396. 
