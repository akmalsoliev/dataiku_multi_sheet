import tempfile
import os 
import shutil
import dataiku
import pandas as pd 


def xlsx_constructor(file_name = str, folder_name = str, sheet_names = list, dataframe_list = list):
    """
    Function to exports DataFrames to Multiple Worksheets Excel File.
    
    Upon recieveing 'Job is completed!' please check assigned folder for an Excel file.
    
    :param file_name: Name of the Excel file to be created.
    :param folder_name: Name of the folder where the Excel file will be exported to. 
    NOTE: Please make sure that the folder exists. Follow README.md for more information. 
    :param sheet_names: List of sheet names to be created in the Excel file. It is a list of strings.
    :param dataframe_list: List of DataFrames to be exported to the Excel file. It is a list of DataFrames.
    :return: None
    """
    if len(sheet_names) != len(dataframe_list):
        raise ValueError('The length of sheet_names and dataframe_list should match!')
    
    with tempfile.TemporaryDirectory() as temp_dir:
        excel_path = os.path.join(temp_dir, file_name)
        for i, (df, sheet_name) in enumerate(zip(dataframe_list, sheet_names)):
            if i == 0:
                df.to_excel(excel_path, sheet_name=sheet_name)
            else:
                with pd.ExcelWriter(excel_path, mode='a', engine='openpyxl') as writer:
                    df.to_excel(writer, sheet_name=sheet_name)

        folder_api = dataiku.Folder(folder_name)
        target_folder = folder_api.get_path()
        target_file = os.path.join(target_folder, file_name)

        shutil.move(excel_path, target_file)
        
        return 'Job is completed!'
 
