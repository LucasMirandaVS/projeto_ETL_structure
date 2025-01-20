import os # manipular arquivos e pastas
import glob # listar arquivos e pastas
import pandas as pd 
from typing import List


# Função para ler os arquivos de uma pasta data/input e  retornar uma lista de dataframes
# args: input_path (str): caminho da pasta com os arquivos
# return: lista de dataframes


path = "C:\\Users\\lucas\\Desktop\\ESTUDOS\\Python\\workshop_1_projeto_do_zero\\data\\input"
path_encoded = path.encode('utf-8')  # Encode the path string
path = os.fsdecode(path_encoded)  # Decode using the appropriate encoding

def extract_from_excel(path: str) -> List[pd.DataFrame]:  
    all_files = glob.glob(os.path.join(path, "*.xlsx"))
    
    data_frame_list = []
    for file in all_files:
        data_frame_list.append(pd.read_excel(file))

    return data_frame_list