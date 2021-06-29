def write_battery_data_to_file(file_path, list):
    # with open(file_path, 'w') as f1:
    file_path.write("var power_data=[\n")
    for i in list:
        file_path.write(i)
    file_path.write('];\n')


def write_moudel_data_to_file(file_path, list):
    file_path.write("[")
    for i in list:
        file_path.write(i)
    file_path.write('],\n')
