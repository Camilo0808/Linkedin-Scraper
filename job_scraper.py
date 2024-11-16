# web_scraper.py
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import time

# Configure Chrome options
chrome_options = Options()
chrome_options.add_argument("--headless")  # Run in headless mode
chrome_options.add_argument("--disable-gpu")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# Initialize WebDriver
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

# Function to scrape Google search results
def scrape_google_search(query, max_results=10):
    try:
        driver.get("https://www.google.com")

        # Accept cookies if the button exists
        try:
            accept_button = driver.find_element(By.ID, "L2AGLb")
            accept_button.click()
        except Exception:
            pass  # Cookie banner might not appear

        # Perform the search
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        # Wait for results to load
        time.sleep(2)

        # Collect search result titles and URLs
        results = []
        search_results = driver.find_elements(By.XPATH, "//div[@class='tF2Cxc']")

        for result in search_results[:max_results]:
            try:
                title = result.find_element(By.TAG_NAME, "h3").text
                url = result.find_element(By.TAG_NAME, "a").get_attribute("href")
                results.append({"title": title, "url": url})
            except Exception as e:
                print(f"Error extracting result: {e}")

        return results

    except Exception as e:
        print(f"Error occurred during scraping: {e}")
        return []

    finally:
        driver.quit()

if __name__ == "__main__":
    query = input("Enter a search query: ")
    results = scrape_google_search(query)

    print("\nSearch Results:")
    for idx, result in enumerate(results, start=1):
        print(f"{idx}. {result['title']} - {result['url']}")