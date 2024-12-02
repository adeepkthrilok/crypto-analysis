from fetch_data import fetch_crypto_data
from analyze_data import analyze_data
from update_excel import update_excel

def main():
    # Fetch live cryptocurrency data
    crypto_data = fetch_crypto_data()

    # Check the type of the fetched data for debugging
    print(f"Type of crypto_data: {type(crypto_data)}")
    
    # Analyze the fetched data
    analyze_data(crypto_data)

    # Update the Excel sheet with the data
    update_excel(crypto_data)

if __name__ == "__main__":
    main()

