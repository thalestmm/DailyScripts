import SmilesPromoTracker, DirectoryCleanse, Tools

if __name__ == "__main__":
    spt = SmilesPromoTracker.SmilesPromoTracker()
    dc = DirectoryCleanse.DirectoryCleanse()
    tools = Tools.Tools()
    tools.create_global_file()
    spt.partial_execute()
    dc.partial_execute()
    tools.send_email()
    pass