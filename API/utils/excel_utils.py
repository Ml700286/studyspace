import openpyxl


def read_excel(file_path):
    workbook = openpyxl.load_workbook(file_path)
    worksheet = workbook["Sheet1"]

    data = []
    keys = [cell.value for cell in worksheet[2]]
    # print(keys)
    for row in worksheet.iter_rows(min_row=3, values_only=True):
        d = dict(zip(keys, row))
        if d.get("execute"):
            data.append(d)
    # print(data)
    workbook.close()
    return data