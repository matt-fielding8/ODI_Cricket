# ODI Cricket Investigation

The 2019 ICC Cricket World Cup was one of the most dramatic and unpredictable we
have ever seen. I wanted to dig a little deeper into the statistics behind this
weird and wonderful game.

### One Day International Overview

In the One Day International (ODI) format, the team batting first will have 50
overs (6 balls in an over) to amass as higher score as possible whilst the other
team attempt to take wickets and limit their score. The second team will then
have 50 overs to try and chase down that score. Either team can lose a maximum
of 10 wickets within the 50 over innings.

## Objective

There is a vast amount of data collected within cricket. Every ball bowled
represents a potentially interesting data point (runs scored, wickets taken),
and each has the potential to follow patterns. This project will investigate
trends within the data and attempt to recommend a winning strategy for
One Day International matches.

## Methods Used
 - Data Wrangling - Web Scraping, Cleaning
 - Data Visualisation
 - Exploratory Data Analysis
 - Statistics

## Technologies
 - Python
 - Jupyter
 - Matplotlib
 - Seaborn
 - Pandas
 - Numpy
 - BeautifulSoup
 - Requests

## Data Overview

The datasets we are focussing on is available to download from [this Kaggle kernel](https://www.kaggle.com/venky73/icc-cricket-world-cup-2019-analysis).
The data has been scraped from [https://www.espncricinfo.com/](https://www.espncricinfo.com/)
and split into 6 dataframes contained within .csv files. In this project we
focus on 2 of these dataframes:

 - **ODI_Match_Results.csv** - Contains match data such as start date, ground,
    countries, result, coin toss, batting order.
 - **ODI_Match_Totals.csv** - Contains score data such as, runs scored,
    wickets lost, result margin.

There is a lot of duplicated data between each dataframe, as well as some
missing data. The first task is to collect the missing data, restructure and
clean each dataframe before exploratory data analysis.

## Notebooks
 - [ODI_Cricket_Wrangle](http://localhost:8888/notebooks/notebooks/ODI_Cricket_Wrangle.ipynb) - Documents the steps taken during the gathering and cleaning process.
 - [ODI_Cricket_Explore](http://localhost:8888/notebooks/notebooks/ODI_Cricket_Explore.ipynb) - Documents the exploratory data analysis process, including visualisations and statistics and hypothesis testing.
 - [ODI_Cricket_Findings](http://localhost:8888/notebooks/notebooks/ODI_Cricket_Findings.ipynb) - Summarises the key findings from the EDA phase with polished visualisations, conclusions and recommendations.
 - [ODI_Cricket_Findings.slides](http://localhost:8888/view/notebooks/ODI_Cricket_Findings.slides.html) - Summarises the key findings in a jupyter slide deck.

## Key Findings
- India and England win 20% more matches on English grounds than any other team.
- Batting first or second makes very little difference to win percentages.
- Teams performed better after **losing** the coin toss.
- Teams that score more than 40 runs above the ground average win 75% of their matches.
- Teams that lost 5 wickets or less won 90% of their matches.
- The luck of the Irish is no myth, they win 65% of the coin tosses.

## Project Organisation
.
├── Data
│   ├── external
│   ├── interim
│   │   ├── archive
│   │   └── __pycache__
│   ├── processed -----------> Cleaned .csv files
│   └── raw       -----------> Raw data
│       ├── archive
│       └── cricket-world-cup-2019-players-data
├── docs
├── models
├── notebooks  -----------> all notebooks
├── references
├── reports    -----------> contains slides and notebooks in .html
│   └── figures
└── src        -----------> contains custom python modules
    ├── data
    │   └── __pycache__
    ├── features
    ├── __pycache__
    └── visualization
        └── __pycache__



--------

<p><small>Project based on the <a target="_blank" href="https://drivendata.github.io/cookiecutter-data-science/">cookiecutter data science project template</a>. #cookiecutterdatascience</small></p>
