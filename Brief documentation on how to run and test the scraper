### 1. Prerequisites

Install Necessary Tools
1. Python:  
   Ensure Python 3.7 or above is installed. Download it [here](https://www.python.org/downloads/).

2. Python Libraries:  
   Install required libraries by running the following:
   ```
   pip install selenium beautifulsoup4 pandas openpyxl
   ```

3. Google Chrome:  
   Install Google Chrome if not already installed.

4. ChromeDriver:  
   - Download ChromeDriver matching your Chrome version from [here](https://sites.google.com/chromium.org/driver/).  
   - Add the ChromeDriver executable to a folder in your system's PATH or keep it in the same directory as the script.


### 2. Running the Script

1. Save the Script  
   Copy the code into a file named `restaurant_scraper.py`.

2. Execute the Script 
   Run the script via the terminal or command prompt:
   ```
   python restaurant_scraper.py
   ```

3. **How the Script Works**:
   - The script automates Google search results for restaurants in Mumbai.
   - Selenium loads web pages, and BeautifulSoup extracts relevant restaurant details.
   - Extracted data includes restaurant names, ratings, price ranges, cuisines, and addresses.
   - All data is stored in a Pandas DataFrame and exported to an Excel file named `restaurants__data.xlsx`.


### 3. Key Features

#### Script Functionalities
- Pagination Handling:  
  Automatically scrapes multiple pages using `page_num` increments.

- Error Handling:  
  Handles missing data and page structure changes gracefully.

- Data Cleaning:  
  - Uses regex to clean names and ratings (e.g., removes numbers like `1.5K` from names).  
  - Ensures valid rating extraction and proper formatting.

#### Output File
The data is saved in `restaurants__data.xlsx` with the following columns:
| Column Name          | Description                                               |
|----------------------|-----------------------------------------------------------|
| Name                 | Restaurant name                                           |
| Rating               | Average rating (1 to 5, single decimal point)             |
| Price Range          | Price range (e.g., ₹₹₹)                                   |
| Location             | Cuisine or location information                           |
| Delivery Options     | Delivery or address information                           |


### 4. Testing the Script

Validation Steps
1. Verify Browser Automation 
   Observe Chrome as it navigates through Google search results.

2. Inspect Output File  
   Open the generated Excel file `restaurants__data.xlsx` to verify:
   - Data is properly extracted and aligned under respective columns.
   - No blank or malformed rows (check for missing names or ratings).

3. Test Error Handling  
   Intentionally interrupt or provide incorrect ChromeDriver setup to test error messages.

Possible Issues
- Anti-Bot Detection:  
   Google may block automated queries. To avoid this:
   - Increase the `time.sleep()` delay (e.g., 15–20 seconds).
   - Use a VPN or different Google account.

- Structure Changes:  
   If Google changes its layout, adjust the BeautifulSoup selectors accordingly.



### 5. Customization

For Other Locations
To scrape restaurants in other cities:
- Modify the search query URL:
  ```
  url = f"https://www.google.com/search?q=restaurants+<city_name>+near+me&tbm=lcl&start={page_num}"
  ```

Adjust Sleep Time
Modify `time.sleep(15)` to handle slower or faster page loads.



### 6. Notes

- Legal Compliance:  
  Web scraping may violate terms of service for websites. Use this script responsibly and only for personal/educational purposes.

- Error Recovery:  
  If the script crashes due to unexpected structure changes, review the HTML of the target page and update selectors.

