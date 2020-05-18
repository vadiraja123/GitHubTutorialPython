from pathlib import Path

import xlrd

def get_data():
    wb=xlrd.open_workbook(str(Path(__file__).parent)+r"\add_payee_details.xlsx")
    sheet=wb.sheet_by_name("add_payee_details")
    datali=[]
    for i in range(1, sheet.nrows):
        data=[]
        for j in range(0, sheet.ncols):
            data.append(sheet.cell_value(i,j))
        datali.append(data)

    return datali








