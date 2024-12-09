from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup
import pandas as pd
import time

# Initialize Selenium WebDriver
driver = webdriver.Chrome()

# Lists to aggregate all data across pages
all_names = []
all_ratings = []
all_price_ranges = []
all_cuisines = []
all_addresses = []
all_delivery_options = []

# Loop through pages
page_num = 0
while True:
    try:
        # Open Google search results page
        url = f"https://www.google.com/search?q=restaurants+mumbai+near+me&tbm=lcl&start={page_num}"
        driver.get(url)

        # Wait for the page to load
        time.sleep(5)

        # Check if the page has results by looking for specific elements
        soup = BeautifulSoup(driver.page_source, "html.parser")
        results = soup.find_all("div", class_="rllt__details")
        if not results:
            print(f"No more results found on page {page_num}. Exiting.")
            break  # Exit loop if no results are found

        # Extract restaurant details
        des = []  # Reset `des` for each page
        for result in results:
            des.append(result.text)

        # Process each entry
        for entry in des:
            split_entry = entry.split("·")
            
            # Extract the name and rating
            try:
                first_part = split_entry[0]
                name = first_part.strip()
                rating = ''.join([c for c in first_part if c.isdigit() or c == "."]).strip()
            except IndexError:
                name, rating = None, None

            # Extract other components
            try:
                price_range = split_entry[1].strip() if len(split_entry) > 1 else None
                cuisine = split_entry[2].strip() if len(split_entry) > 2 else None
                address = ''.join(split_entry[3:]).split("Dine-in")[0].strip() if len(split_entry) > 3 else None
                delivery = ', '.join(split_entry[3:]).split("Dine-in")[1:] if len(split_entry) > 3 else None
            except Exception as e:
                price_range, cuisine, address, delivery = None, None, None, None

            # Append to aggregated lists
            all_names.append(name)
            all_ratings.append(rating)
            all_price_ranges.append(price_range)
            all_cuisines.append(cuisine)
            all_addresses.append(address)
            all_delivery_options.append(delivery)

        print(f"Processed page {page_num}")
        page_num += 10  # Increment to the next page

    except Exception as e:
        print(f"Error encountered: {e}. Exiting loop.")
        break  # Exit loop on error (e.g., page not found)

# Close the browser after all iterations
driver.quit()

# Combine all data into a single DataFrame
data = {
    "Name": all_names,
    "Rating": all_ratings,
    "Price Range": all_price_ranges,
    "Adreess": all_cuisines,
    "Delivery Options": all_addresses,
    
}
df = pd.DataFrame(data)

# Save all data to a single Excel file
excel_file_path = "restaurants_combined_data_final1.xlsx"
df.to_excel(excel_file_path, index=False)
print(f"Saved all data to {excel_file_path}")
