import os
import openpyxl

def search_in_workbook(file_path, search_value):
    workbook = openpyxl.load_workbook(file_path, data_only=True)
    for sheet_name in workbook.sheetnames:
        sheet = workbook[sheet_name]
        for row in sheet.iter_rows():
            for cell in row:
                if cell.value == search_value:
                    # Zwróć nazwę pliku, nazwę zakładki i adres komórki
                    return file_path, sheet_name, cell.coordinate
    return None

def search_in_directory(search_value, directory):
    for file in os.listdir(directory):
        if file.endswith('.xlsx'):
            file_path = os.path.join(directory, file)
            result = search_in_workbook(file_path, search_value)
            if result:
                print(f"Znaleziono w pliku: {result[0]}, zakładka: {result[1]}, komórka: {result[2]}")
                # Zwróć, jeśli chcesz zakończyć po znalezieniu pierwszego wystąpienia
                return

if __name__ == "__main__":
    directory = input("Podaj ścieżkę do katalogu: ")
    search_value = input("Podaj szukaną wartość: ")
    search_in_directory(search_value, directory)
