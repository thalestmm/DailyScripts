import os
from datetime import date, datetime



class DirectoryCleanse:
    def __init__(self, path="/Users/thalestmm/Downloads", days_limit= 7):
        self.now = datetime.utcnow()
        self.path = path
        self.days_limit = days_limit
        self.filename = "message.txt"


    def delete_old_files(self, comment = False):
        total_size = 0
        self.deleted_files = []
        for file in os.listdir(self.path):
            filepath = self.path + "/" + file
            stats = os.stat(filepath)
            last_opened = datetime.utcfromtimestamp(stats.st_ctime)
            time_delta = int((self.now - last_opened).days)
            if time_delta > self.days_limit:
                if comment == True:
                    print(f"Deleted {file}")
                total_size += stats.st_size
                self.deleted_files.append(file)
                os.remove(filepath)
        self.saved_space = total_size/1000000

    def create_html_message(self,comment=False):
        self.message = f"<h2></b>Directory Cleansing for {self.path}</b></h2>"
        if len(self.deleted_files) > 0:
            self.message += f"<p>A total of <b>{len(self.deleted_files)} files</b> were deleted:</p><br>"
            for name in self.deleted_files:
                self.message+=f"<p>- {name}</p>"
            self.message+=f"<p>Total memory saved: <b>{self.saved_space} mb</b>"
        else:
            self.message += f"<p><b>No files deleted</b></p>"
        self.message += "<hr>"
        if comment:
            print(self.message)

    def add_to_file(self,comment=False):
        with open(self.filename, "a") as myfile:
            myfile.write(self.message)
            myfile.close()
        if comment:
            print("Message added")

    def partial_execute(self):
        self.delete_old_files()
        self.create_html_message()
        self.add_to_file()

if __name__ == "__main__":
    dc = DirectoryCleanse()
    dc.delete_old_files(comment=True)
    dc.create_html_message()
    pass
