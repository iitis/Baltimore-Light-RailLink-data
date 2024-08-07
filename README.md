# Baltimore-Light-RailLink-data

Histograms of traffic data of Baltimore Light RailLink
Data supplied by the 

We acknowledge Swiftly’s GTFS-realtime API https://swiftly.zendesk.com/hc/en-us 
(accessed 11-31 January 2024) for supplying these real-time traffic data.

## To plot a histogram of passing times between MR and CS stations use:

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



## Founding

The code was partially supported by Polish National Science Center under grant agreement number 2023/07/X/ST6/00396. 
