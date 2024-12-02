import pandas as pd

def analyze_data(crypto_data):
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(crypto_data)

    # Debugging: Print the DataFrame structure and column names
    print("Converted DataFrame:")
    print(df.head())  # Print the first 5 rows of the DataFrame
    print("Columns in DataFrame:", df.columns)  # Print all column names

    # Ensure column names match your data structure
    # Adjust these column names based on your actual data
    top_5 = df.nlargest(5, "market_cap")  # Replace 'market_cap' with the correct column name if needed
    print("Top 5 Cryptocurrencies by Market Cap:")
    print(top_5)

    avg_price = df["current_price"].mean()  # Replace 'current_price' with the correct column name
    print(f"Average Price: ${avg_price:.2f}")

    highest_change = df["price_change_percentage_24h"].max()  # Replace with correct column if needed
    lowest_change = df["price_change_percentage_24h"].min()  # Replace with correct column if needed
    print(f"Highest 24h % Change: {highest_change:.2f}%")
    print(f"Lowest 24h % Change: {lowest_change:.2f}%")


