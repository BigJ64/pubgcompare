# pubgcompare

## Goal
Provide a simple script interface for comparing two players of Player Unknown's Battlegrounds in their K/D Ratio, Win %, and Skill Rating statistics.

## Prerequisites
* [Python 3](https://www.python.org/)
* [Pypubg Library](https://github.com/lbrictson/pypubg)
* [TRN PUBG Tracker API Key](https://pubgtracker.com/site-api)

## Setup
Once you have a version of Python 3 installed you will need to install the Pypubg Library. Once this library is installed you can clone this repo and place your TRN PUBG Tracker API key in the api_key file.  The script should be ready to run.

## Usage
Once setup is complete you can run the compare.py script. It will ask you for two players and then compare their K/D Ratio, Win % and Skill Rating.

```shell
$ python compare.py
Enter the 2 players you would like to compare:
> denahuen
> akustic

denahuen has a K/D Ratio of 3.41.
akustic has a K/D Ratio of 1.09.
denahuen has the better K/D Ratio.

denahuen has a Win % of 15.32%
akustic has a Win % of 0.83%.
denahuen has the better Win %.

denahuen has a Skill Rating of 3288.8.
akustic has a Skill Rating of 1753.87.
denahuen has the better Skill Rating.
```
