import pandas as pd
import openpyxl

def Retrieve_names(file_path: str) -> list:
    """"""
    df = pd.read_excel(file_path)
    names = df["Names"].tolist()
    return names

def Create_excel(seated_names: list) -> None:

    workbook = openpyxl.Workbook()
    sheet = workbook.active

    sheet["A1"] = "Table / Seat"
    sheet["B1"] = "Name"

    table_count = 6
    seats_count = 4
    row = 2

    for table in range(1, table_count + 1):
        for seat in range(1, seats_count + 1):
            sheet[f"A{row}"] = f"Table {table} / Seat {seat}"
            
            if row - 2 < len(seated_names):
                sheet[f"B{row}"] = seated_names[row - 2]
            row += 1

    workbook.save("Openspace_ordering.xlsx")



