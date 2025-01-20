from typing import List
import pandas as pd


# Função para trasnformar uma lista de datas frames em um unico data frame
def concatenate_data_frames(data_frame_list: List[pd.DataFrame]) -> pd.DataFrame:
    return pd.concat(data_frame_list, ignore_index = True)

