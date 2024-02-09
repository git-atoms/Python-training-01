import os
import openpyxl
import platform

def search_in_workbook(file_path, search_value):
    workbook = openpyxl.load_workbook(file_path)
    for sheet_name in workbook.sheetnames:
        sheet = workbook[sheet_name]
        for row in sheet.iter_rows(values_only=True):
            for cell in row:
                if cell == search_value:
                    # Zwróć nazwę pliku, nazwę zakładki i adres komórki
                    return file_path, sheet_name, sheet.cell(row=row[0].row, column=row[0].column).coordinate
    return None

def search_in_directory(search_value, directory='.'):
    for file in os.listdir(directory):
        if file.endswith('.xlsx'):
            result = search_in_workbook(file, search_value)
            if result:
                print(f"Znaleziono w pliku: {result[0]}, zakładka: {result[1]}, komórka: {result[2]}")
                return  # Zatrzymaj po znalezieniu pierwszego wystąpienia

if __name__ == "__main__":
    search_value = input("Podaj szukaną wartość: ")
    search_in_directory(search_value)

    # Oczekiwanie na naciśnięcie dowolnego klawisza przed zamknięciem
    if platform.system() == 'Windows':
        os.system('pause')  # Tylko dla Windows
    else:
        input("Press any button to continue...")  # Dla Unix/Linux i MacOS