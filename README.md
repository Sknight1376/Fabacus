# Fabacus Coding Exercise

## Objectives

1 - Extract data from provided file <br>
2 - Form data structures in line with the three required outputs<br>
3 - Write outputs to csv files<br>
4 - Use outputs during analyis to gain the required insights into the provided data

## Process Outline

For this project I attempted to make the processing application as lightweight as possible, using minimal code to achieve the required result. Both the ingest and output are simple and standard processes, using widely used packages from the python ecosystem (JSON + Pandas). Three seperate functions are defined to deal with the processing of the data into the required structures, using a combination of loops to deal with each entry in turn, and maps to wrangle the data into a more useful structure for the final output. Once produced, the files are loaded to tableau for further analysis.

## Roadblocks

During the process a couple of issues arose, principally around the initial data ingest. The file provided contained a number of json-like structures, all newline seperated. Initially this made it difficult to load in a single go, so the alternative approch was to iterate down each row and add to an internal list within the application. Once gathered and analysed, it also became clear that the data was inconsistent in its construction, with differing number of key:value entries in each row. Therefore an approach had to be found that could deal with those inconsitancies while returning the required result.

## Limitations

Although the provided solution does generate the required files and analysis, there are a number of limitaions that could and should be overcome before being allowed into production. 

Firstly, the functions used are all very similar in their approch, it's likely that a single fuction could be defined which generates the data required when passed the relevent parameters (apply DRY concepts)

The solution provided hasn't been containerised, so it is likely to fail in the future as the integrity of the required dependancies cannot be guarenteed

Finally, the inflexibility of the provided solution means it currently cannot be expanded beyond the objectives above - if a new data source was required then this would mean a major re-factoring of the application to fit the new requirements. Modularising and good documentaion could provide a solution for this issue going forward. 

## Links

[Link to tableau dashboard](https://public.tableau.com/views/Fabacus_Coding_Test/FabacusCodingTest?:language=en-US&:sid=&:redirect=auth&:display_count=n&:origin=viz_share_link)

[Pandas](https://pandas.pydata.org/)

[Map Function](https://www.w3schools.com/python/ref_func_map.asp)