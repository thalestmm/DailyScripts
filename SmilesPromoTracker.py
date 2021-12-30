from bs4 import BeautifulSoup
import requests
import time
import Tools

class SmilesPromoTracker:
    def __init__(self,search_text = "Transferir Pontos do Cartão", url="https://www.smiles.com.br/promocao"):
        self.url = url
        self.page = requests.get(url).text
        self.doc = BeautifulSoup(self.page, "html.parser")
        self.search_class = "titulo-promo"
        self.search_text = search_text
        self.filename = "message.txt"

    def search_trough_smiles(self, comment=False):
        # Begin Scraping
        boxes = self.doc.find_all("div", attrs={"class": self.search_class})
        # Lists for keeping all the data from the matches
        self.limit_dates = []
        self.links = []
        for box in boxes:
            # Clean the original HTML
            text = str(box).split(">")[1].split("<")[0].split("[sorriso]")
            text = str(text[0] + " " + text[1])

            # Find the limit epoch
            epoch = int(
                str(box.parent.find("span", attrs={"class": "card-data-validade"})).split(">")[1].split("<")[
                    0]) / 1000 + 46800
            # Transform the epoch into the actual date
            limit_date = time.strftime('%d-%m-%Y %H:%M:%S', time.localtime(epoch))
            # Find the specific URL
            link = "https://www.smiles.com.br" + str(box.parent.a.get("href"))

            # Find a match for the target text
            if text == self.search_text:
                self.limit_dates.append(limit_date)
                self.links.append(link)

        if comment:
            print(f"You are looking for '{self.search_text}':\n")
            for date, link in zip(self.limit_dates, self.links):
                print(f"Due till: {date}\nLink: {link}\n")

        # Connection failed test (does't actually raise any errors)
        if len(self.limit_dates) == 0:
            print("Smiles Scraping Failed")

    def create_message(self,comment=False):
        self.message = f"Smiles Offers:\n\n"
        if len(self.limit_dates) > 0:
            self.message += f"Total results for '{self.search_text}': {len(self.limit_dates)}\n\n"
            for date,link in zip(self.limit_dates, self.links):
                self.message+=f"Due till {date}\nLink: {link}\n\n"
        else:
            self.message += f"No available offers for '{self.search_text}'\n"

        if comment:
            print(self.message)

    def create_html_message(self,comment=False):
        self.message = f"<h2></b>Smiles Offers:</b></h2>"
        if len(self.limit_dates) > 0:
            self.message += f"<p>Total results for '{self.search_text}': <b>{len(self.limit_dates)}</b></p><br>"
            for date,link in zip(self.limit_dates, self.links):
                self.message+=f"<p>Due till {date}    Link: <a href='{link}'>{link}</a></p><br>"
        else:
            self.message += f"<p><b>No available offers</b> for '{self.search_text}'</p>"
        self.message += "<hr>"
        if comment:
            print(self.message)

    def create_self_file(self,comment=False):
        file = open(f"{self.filename}","w+")
        file.write(self.message)

        if comment:
            print("File Created")
        return None

    def add_to_file(self,comment=False):
        with open(self.filename, "a") as myfile:
            myfile.write(self.message)
            myfile.close()
        if comment:
            print("Message added")

    def full_execute(self):
        self.search_trough_smiles()
        self.create_message()
        self.create_self_file()

    def partial_execute(self):
        self.search_trough_smiles()
        self.create_html_message()
        self.add_to_file()


if __name__ == '__main__':
    test = SmilesPromoTracker()
    test.full_execute()
    tools = Tools.Tools()
    tools.send_email()
