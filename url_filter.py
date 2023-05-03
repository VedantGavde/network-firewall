import csv
import urllib.parse
import webbrowser

def check_url(pkt_url):
    print("inside check url")
    # Step 1: Get user input URL
    #user_input_url = input("Enter URL: ")
    user_input_url = pkt_url
    
    # Step 2: Open CSV file
    with open('malware_url_online.csv', 'r') as file:
        reader = csv.DictReader(file)

        # Step 3: Compare user input URL with URLs in CSV file
        for row in reader:
            csv_url = row['url']
            if user_input_url == csv_url:
                print(f"Blocked {csv_url}")
                return (0, None)

        # Step 4: Execute user input URL if it is not in the CSV file and is valid
        parsed_input_url = urllib.parse.urlparse(user_input_url)
        if parsed_input_url.scheme and parsed_input_url.netloc:
            print(f"Executed {user_input_url}")
            return (1, user_input_url)
    
    # Step 5: If URL is not in CSV file and is not valid, print an error message and return -1
    print("Error: Invalid URL")
    return (-1, None)
