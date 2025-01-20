import pandas as pd
from app.pipeline.transform import concatenate_data_frames

df_1 = pd.DataFrame({'col1': [1,2], 'col2': [3,4]})
df_2 = pd.DataFrame({'col1': [5,6], 'col2': [7,8]})

def testar_a_concatenacao_da_lista_de_dataframe():
    # arrange 
    data_fame_list = [df_1, df_2]
    data_frame = pd.concat(data_fame_list, ignore_index = True)

    # act 
    df = concatenate_data_frames(data_fame_list)

    # assert 
    assert df.shape == (4,2)
    assert data_frame.equals(df)