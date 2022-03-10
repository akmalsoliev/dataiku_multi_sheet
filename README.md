# Multiple Worksheet Constructor and Extractor for DataIku

This package avoids the requirements to install additional plugins in order to create a multi-worksheet Excel file. 

Currently, suggestions made on DataIku forum is to create store the information on `BytesIO` using `openpyxl`, however, this method will create a corrupted Excel file. 

The issue of corrupted file lead to the a creation of the following package. 

**TESTED ON:** Dataiku Version: 8.0.4

## Requirements:
* Python version 3.6 and up
* openpyxl installed in your env

## Setup:
DataIku currently offers multiple ways of constructing a folder, these are the settings that have been tested and were proven to be successful:

1. Go to your Flow
2. Click `DATASET` and select `Folder`
3. Insert name of the folder in `Label` and select `Filesystem` as a storage location (preferably `filesystem_folder`). `Partioning`: `Not partioned`

**NOTE:** Label is the name of the folder, that will be required as an input.

## How to use:
Import the package to your `Library` section either using `Git` > `Import Git`. 
Open up your notebook and import using: 
`from dataiku_multi_sheet import xlsx_constructor`
Upon receiving 'Job is completed!' please check assigned folder for an Excel file.

## Params:     
:param: file_name: Name of the Excel file to be created.
:param: folder_name: Name of the folder where the Excel file will be exported to.
NOTE: Please make sure that the folder exists. Follow README.md for more information. 
:param: sheet_names: List of sheet names to be created in the Excel file. It is a list of strings.
:param: dataframe_list: List of DataFrames to be exported to the Excel file. It is a list of DataFrames.
:return: None
