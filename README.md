-Run data_menu.py with any python IDE or in a virtual environment with a network flow csv file (Currently using goflow2 sample output) 

-3 options on main menu dropdown: 

**1. Utilization percentage**

Next, asks what threshold percentage you want to show 

Displays all networks with utilization percentage higher than that threshold 

uses formula ->current network traffic / maximum available bandwidth * 100 

Current network traffic = bytes transferred * 8 (bits) / flow time (sec) 

Assuming maximum available bandwidth is 1 GB/s 

Sums up all the flows for each source address, and displays the source address, along with its network utilization percentage, if it’s greater than the threshold. 

**2. Top n networks (by bytes transferred) **

Next, asks user for n 

Then, sum up the bytes transferred for each src address 

Displays results, in descending order based on bytes that the network transferred 

**3. Top Flows today **

Next, asks user for number of top flows 

Displays results 
