# Daily Scripts

In here I'll keep all the automations I plan for my day-to-day use. All the specific automations are structured like modules and controled by the `main.py` file, with the generic tools like making files and sending emails stored within `Tools.py`. On my MacBook, the central file is actually controlled by the Scheduler.

A brief explanation about the automated tasks:

* `SmilesPromoTracker.py` - A simple application that scrapes the Smiles website on the lookout for credit card points transference bonuses, and then sends them to my e-mail. With this, I don't have to everyday access the website and scroll through the entire page on my phone (which is actually very cumbersome)
* `DirectoryCleanse.py` - A script to check for old files on any directory. I'll mostly use it to delete files and folders from the Downloads, as it can get pretty clogged up at times, and having to go through each file can be very cumbersome 

Later on, I hope to deploy all (or most) of these applications to the cloud, so the laptop won't need to be turned on everyday on a specific time.
