import tempfile
import os 
import shutil
import dataiku 

def excel_sheet_constructor(file_name = str, folder = str, sheet_names = list, dataframe_list = list):

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

        target_folder = dataiku.Folder(folder)
        target_folder = folder_api.get_path()
        target_file = os.path.join(target_folder, file_name)

        shutil.move(excel_path, target_file)
 
