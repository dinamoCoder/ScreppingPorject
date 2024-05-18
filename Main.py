from selenium.webdriver.common.by import By
import undetected_chromedriver as uc
from fake_useragent import UserAgent
import time
import pandas as pd
from fp.fp import FreeProxy

# Function to perform the scraping task
def scrape_ups(username, password):
    data=""
    count=0;
    for _ in range(100):
        try:
            data =  FreeProxy(country_id=['IN'], https=True).get()
            print(data)
            break;
        except FreeProxyException:
            print("not getting ")
            time.sleep(1)
    #print(proxy);
    try:
        ua = UserAgent()
        options = uc.ChromeOptions()
        options.add_argument(f"--proxy-server={data}")  # Use correct protocol and port
        options.add_argument(f"user-agent={ua.random}")
        #print(options.toString())
        driver = uc.Chrome(options=options, version_main=124)
        try:
            # Open the UPS website
            driver.get('https://www.ups.com/lasso/login')
            
            time.sleep(10)

            # Interact with login form
            tracking_input = driver.find_element(By.ID, 'email')
            tracking_input.send_keys(username)

            # Wait for the element to be interactable
            time.sleep(5)

            status_element = driver.find_element(By.ID, 'submitBtn')
            status_element.click()

            time.sleep(5)

            pwd = driver.find_element(By.ID, 'pwd')
            pwd.send_keys(password)

            status_elements = driver.find_element(By.ID, 'submitBtn')
            status_elements.click()
            
            time.sleep(20)  # Adjust as needed

        except Exception as e:
            print(f'An error occurred: {e}')
        finally:
            driver.quit()
    except Exception:
        if(count==0):
            scrape_ups(username,password);
            count+=1;
            return;
        else:
            return;
def ReadDataFrame(df):
    for index, row in df.iterrows():
        print(index)
        print(f"UserName: {row['UserName']}, Passsword: {row['Password']}")
        scrape_ups(row['UserName'], row['Password'])

def read_csv(file_path):
    """Read the CSV file and return a DataFrame."""
    return pd.read_csv(file_path)

# Run the scraping task
if __name__ == "__main__":
    file_path = 'Book1.csv'
    df = read_csv(file_path)
    ReadDataFrame(df)
