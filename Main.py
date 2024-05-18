from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
import time
import pandas as pd

# Function to perform the scraping task
def scrape_ups():
    options = uc.ChromeOptions()
    driver = uc.Chrome(options=options, version_main=124)
    try:
        # Open the UPS website
        driver.get('https://www.ups.com/lasso/login');

        # Example of interaction: Input a tracking number and submit (adjust this based on actual needs)
        tracking_input = driver.find_element(By.ID, 'email')
        tracking_input.send_keys('adminCom')  # Replace with an actual tracking number

        # Wait for the results to load
        time.sleep(5)

        # Scrape the needed information
        # Adjust the selectors based on the actual page structure
        status_element = driver.find_element(By.ID, 'submitBtn')
        status_element.click()

        time.sleep(20)

        pwd = driver.find_element(By.ID, 'pwd')
        pwd.send_keys('adminSingh@1')


        status_elements = driver.find_element(By.ID, 'submitBtn')
        status_elements.click()
        
    except Exception as e:
        print(f'An error occurred: {e}')
    finally:
        driver.quit()

def ReadDataFrame(df):
    for index, row in df.iterrows():
        print(index)
        print(f"UserName: {row['UserName']}, Passsword: {row['Passsword']}")
        scrape_ups();


def read_csv(file_path):
    """Read the CSV file and return a DataFrame."""
    return pd.read_csv(file_path)
# Run the scraping task 100
if __name__ == "__main__":
    file_path = 'data.csv'
    df = read_csv(file_path)
    ReadDataFrame(df)
    scrape_ups()
    time.sleep(5)  # Optional: Add a delay between iterations
