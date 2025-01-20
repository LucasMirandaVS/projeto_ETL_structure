from pipeline.extract import extract_from_excel
from pipeline.transform import concatenate_data_frames
from pipeline.load import load_excel

if __name__ == "__main__":
    data_frame_list = extract_from_excel("C:\\Users\\lucas\\Desktop\\ESTUDOS\\Python\\workshop_1_projeto_do_zero\\data\\input")
    print(type(data_frame_list))
    data_frame = concatenate_data_frames(data_frame_list)
    print(type(data_frame))
    load_excel(data_frame, "C:\\Users\\lucas\\Desktop\\ESTUDOS\\Python\\workshop_1_projeto_do_zero\\data\\output", "output")