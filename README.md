# UO CS322 - Project 4 #

Abie Safdie


asafdie11@gmail.com


# Description of Project

This project utlizes an AJAX interaction to create a brevet calculator without needing a page reload.


The algorithm used to calcualte the times can be found at: https://rusa.org/pages/acp-brevet-control-times-calculator


This project required a reverse-engineering of the algorithm, which is what is implemented in `acp_times.py`



# Notes on Webpage

The user can input a distance, start time, and checkpoints and have the correct opening and closing times associated with each checkpoint be displayed without a page reload. The displayed times follow the rules goverened by RUSA. 

# Test Cases

In `test/test_acp_times.py` there are 5 test cases which test the obscurities of the RUSA algorithm. 

