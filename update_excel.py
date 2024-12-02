import openpyxl

def update_excel(crypto_data):
    # Create a new workbook and sheet
    wb = openpyxl.Workbook()
    ws = wb.active
    ws.title = "Crypto Data"

    # Set the headers for the Excel sheet
    ws.append(['#', 'Name', 'Symbol', 'Current Price (USD)', 'Market Cap', '24h % Change', '24h Volume'])

    # Loop through the crypto_data to write each row
    for index, coin in enumerate(crypto_data, start=1):
        # Extract the required data from the coin
        # Ensure the row data is in list format, not a dictionary
        row = [
            index,
            coin['name'],
            coin['symbol'],
            coin['current_price'],
            coin['market_cap'],
            coin['price_change_percentage_24h'],
            coin['total_volume']
        ]
        # Append the row to the Excel sheet
        ws.append(row)

    # Save the Excel file
    wb.save('crypto_data.xlsx')
    print("Excel file 'crypto_data.xlsx' has been created.")

