from PIL import ImageTk, Image
from bs4 import BeautifulSoup
import requests
import tkinter as tk

def scrapeSchedule():
    # Send an HTTP request to the website
    url = 'https://www.sportsmediawatch.com/nba-tv-schedule-2023-how-to-watch-stream-games-today/'
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the table you want to scrape
    table = soup.find('table')

    tr_tags = table.find_all('tr')

    # Creating a variable to store the scraped data
    scraped_data = ""

    # This is process and collect the data from each row
    for tr in tr_tags:

        # Extract individual <td> elements within the row
        td_tags = tr.find_all('td')[:-1] # excludes the local channels with [:-1] (the last td tag)

        # Process and collect the data within each <td> element
        for td in td_tags:
            if ":" in td.get_text(strip=True):
                scraped_data += "----\n" + td.get_text(strip=True) + "\n"
            else:
                text = td.get_text(strip=True).replace('-', '@', 1)
                scraped_data += text + " | "
        scraped_data += "\n"

    # Display the scraped data in the text box
    result_text.delete(1.0, tk.END)  # Clear previous results
    result_text.insert(tk.END, scraped_data)
    result_text.config(font=("Arial", 18))  # Change the font to Arial, size 12


root = tk.Tk()
root.geometry("500x600")
root.title("NBA Schedule")

label = tk.Label(root, text="Today's NBA Schedule - ET Timezone", font=('Arial', 20))
label.pack()

result_text = tk.Text(root, wrap=tk.WORD, width=100, height=20)
result_text.pack()

# Call the scrapeSchedule function immediately when the GUI is started
scrapeSchedule()

img = ImageTk.PhotoImage(Image.open("nba-logo.jpg"))
label = tk.Label(root, image=img)
label.pack()


root.mainloop()
