# lib/table_layout.py

import pandas as pd

def format_excel_file(data, columns, file_path):
    # Convert the list to a DataFrame
    df = pd.DataFrame(data, columns=columns)

    # Prepare the Excel writer
    writer = pd.ExcelWriter(file_path, engine='xlsxwriter')

    # Write the DataFrame to an Excel file
    df.to_excel(writer, index=False, sheet_name='Sheet1')

    # Get the xlsxwriter workbook and worksheet objects
    workbook  = writer.book
    worksheet = writer.sheets['Sheet1']

    # Set the column widths
    worksheet.set_column('A:A', 80)
    worksheet.set_column('B:B', 230)
    worksheet.set_column('C:C', 30) 
    worksheet.set_column('D:D', 20)
    worksheet.set_column('E:E', 20)

    # Add a header format
    header_format = workbook.add_format({
        'bold': True,
        'text_wrap': True,
        'valign': 'top',
        'fg_color': '#D7E4BC',
        'border': 1})

    # Write the column headers with the defined format
    for col_num, value in enumerate(df.columns.values):
        worksheet.write(0, col_num, value, header_format)

    # Close the Pandas Excel writer and output the Excel file
    writer.close()
