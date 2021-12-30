import SmilesPromoTracker as spt
import Tools

if __name__ == "__main__":
    spt = spt.SmilesPromoTracker()
    tools = Tools.Tools()
    tools.create_global_file()
    spt.partial_execute()
    tools.send_email()
    pass