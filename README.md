# MogBot
Discord Bot capable of outputting information about the weather, League of Legends statistics of players and champions and Reddit subreddits on your discord channel.

#### Weather Commands
##### Main command : !weather
###### Subcommands : 
- -cur cityName, areaName : output the current weather of the specific city.
- -for cityName, areaName : forecast the next 7 days of that city.
- -c numericalValue : output the conversion of fahrenheit value to celsius.
- -f numericalValue : output the conversion of celsius value to fahrenheit.

##### Example : 
!weather -f 25 = bot outputs 77 to the channel that the user typed the command. 

### League of Legends Commands 
#### Main command : !league
##### Subcommands :
###### champion (-c)
- -stats championName : provide all relevant statistic of champion such as skills with description and base stats.
- -lore championName : Output the lore of the champion that is selected.
- -skin championName : Provide list of skins of champion and provide the option to send image of a specific skins wanted.

###### summoner (-s)
- most summonerName,Region : Provide the most played champions and statistic of player on those champions for current season.
- best summonerName,Region : Output the best champions and statistic of player on those champion for current season based on KDA and KP.

### Reddit
#### Main command : !reddit
#### Subcommands : 
- top subredditName,numberOfLinks : output the top links of the specific subreddit with the number of links wanted.
- hot subredditName,numberOfLinks : output the hottest links with the number of links wanted.
- new subredditName : update channel with new links to the specific subreddit.

