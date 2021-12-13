# LinkedinConnectionBot

Recently, I joined [WomenTech Network](https://www.womentech.net/about/womentech-membership?join=NDA0MjE=) slack community I found that lot of interesting people have shared their Linkedin profile links,
Then a thought pop up into my mind what if we download all the links in one csv and automatically send the connection request with personalised to them.

## Steps that I followed to build this automated bot:
                
### 1. Downloading all the profile links from slack or discord channel :
       I used Data Miner chrome extension tool to download all the links into csv file
### 2. Cleaning and procession the csv file data to identify the potential profile links
       Either you can write script in excel to filter out only linkedin profile urls among other links or you can use Python to do this.
### 3. Writing the Python script for automation
       I worked with selenium and pyautogui library to open the url and click the buttons, 
       I faced difficulty to find css selector or element for connect button so I used Automation Anywhere free community software to get the target attribute.
### 4. Testing the script
        I selected one sample profile to run my program but I found out something different about Linkedin. 
        There are two types of people one who preferred to be follow so for them connect button is available on drop down of more option
        while for the other one connect button is directly available so you have to write the code for both the scenarios.
### 5. Final Execution
       Now when you use the final csv file you will likely to come across certain exceptions so I wrote them on my code and then it worked like a charm.
       
 ####[Note : for people who prefers to be followed my automation bot will just follow them it won't send connection request to them]
 
 If you want to understand my code in more detail way then please go through my medium article here :
 https://medium.com/@ektamishra335
 
 follow me on :
 
 [![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/shweta-mishra-374614110/)
 
 [medium](https://medium.com/@ektamishra335)
 
 Interested to be a part of women techpreneurs or to meet awesome women in tech ?
 
 [Click here](https://www.womentech.net/about/womentech-membership?join=NDA0MjE=)
