# MLR_railway_data
traffic data of Maryland Light Railways (MLR)


## To read real time GFTS-RT data from SWIFTLY data use:

```
swiftly.py --folder ...
```

where argument is the folder in \outputs where data are saved .

## To plot histogram of passing times between MR and CS stations use:

```
hist --datafolder  ...  --direction
```

where: --datafolder (multiple) arguments of files input \outputs
       --direction  trains direction possibne "n" north, "s" south "" both.

Plots are saved in ```\pics```.


Example plotter:

```
python3 hists.py --datafolder  "11012024_700/" "12012024_700/" "15012024_700/" "16012024_700/" "11012024_1500/" "12012024_1500/" "15012024_1500/" "16012024_1500/" --direction "n"
```


### In other_gfts general (static) GTFS data and station codes are present.

### In analyzis_transportation there is the feedback of specialist in transportation on this data.
