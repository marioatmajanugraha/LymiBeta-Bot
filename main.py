from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import random
import string
from colorama import Fore, Style, init
import pyfiglet
import time

# Initialize colorama
init()

# Watermark
ascii_banner = pyfiglet.figlet_format("Airdrop 888")
print(Fore.CYAN + ascii_banner + Style.RESET_ALL)
sub_banner = "Script Code by - @balveerxyz || Lymi Beta BOT"
print(Fore.CYAN + sub_banner + Style.RESET_ALL)

def generate_email(username):
    random_number = random.randint(1, 100000)
    return f"{username}{random_number}@mailnesia.com"

def submit_email(driver, email):
    try:
        # Find the email input field and enter the email
        email_input = driver.find_element(By.ID, "form-field-input-306dde85-d3cf-4ccf-2653-bc0b8fe6a979-:R3b:")
        email_input.clear()
        email_input.send_keys(email)

        # Find the submit button and click it
        submit_button = driver.find_element(By.XPATH, "//button[@data-hook='submit-button']")
        submit_button.click()

        # Wait for the response
        time.sleep(3)

        # Check if the registration was successful
        success_message = "Join Beta"
        if success_message in driver.page_source:
            print(Fore.GREEN + "[Success] - Register " + email + Style.RESET_ALL)
            return True
        else:
            print(Fore.RED + "[Failed] - Failed " + email + Style.RESET_ALL)
            return False
    except Exception as e:
        print(Fore.RED + "[Failed] - An error occurred: " + str(e) + Style.RESET_ALL)
        return False

def main():
    # Setup Chrome options
    chrome_options = Options()
    chrome_options.add_argument('--headless')
    chrome_options.add_argument('--no-sandbox')
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--log-level=3')  # Suppress log output

    # Initialize the driver
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

    try:
        # Open the website
        driver.get("https://www.lymi.app/")

        # Wait for the page to load
        time.sleep(3)

        # Ask user for username and the number of emails to submit
        username = input("Masukan Username: ")
        num_emails = int(input("Berapa email yang mau di submit? "))

        successful_emails = []
        failed_emails = []

        for _ in range(num_emails):
            email = generate_email(username)
            if submit_email(driver, email):
                successful_emails.append(email)
            else:
                failed_emails.append(email)
            # Add a 2-second delay between submissions
            time.sleep(2)

        # Save successful emails to file
        with open("accounts.txt", "w") as f:
            for email in successful_emails:
                f.write(email + "\n")

        # Print summary
        print(Fore.CYAN + f"Berhasil - {len(successful_emails)} Email Terdaftar, Gagal - {len(failed_emails)} Email" + Style.RESET_ALL)

    except Exception as e:
        print(Fore.RED + "[Failed] - An error occurred: " + str(e) + Style.RESET_ALL)
    finally:
        driver.quit()

if __name__ == "__main__":
    main()