# Data-Analise-Test
## Investigative Analysis and Data Cleaning Project
### We take data of tweets that are classified as antisemitic and non-antisemitic, locate all kinds of tweets according to parameters, then clean the data and export it to files.

## Folder structure:
### src
* |- data_cleaning.py
* |- data_exportet.py
* |- data_investigation.py
* |- data_loader.py
* |- main.py
### results |
* |- results.json
* |- tweets_dataset_cleaned.csv

### The main file actually manages all the logic. It takes data from all the files, loads it, runs all the manipulations of all the classes, and exports the files using the export class.