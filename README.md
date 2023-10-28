
Introduction:
----------------
This project using dataset from UCI - Wine to prepare a dataset for a Machine Learing Project, select some main features and store data in a Postgres database provided by Neon Tech. The end of script will transfer to a ClickHose Cloud which is Free Trail service.

Dataset summary:
----------------
Using chemical analysis to determine the origin of wines
Database Name: Wine
Database URL: https://archive.ics.uci.edu/dataset/109/wine
Input variables:
- fixed acidity: most acids involved with wine or fixed or nonvolatile
- volatile acidity: the amount of acetic acid in wine
- citric acid: found in small quantities, citric acid can add 'freshness' and flavor to wines
- residual sugar: the amount of sugar remaining after fermentation stops
- chlorides: the amount of salt in the wine
- free sulfur dioxide: the free form of SO2 exists in equilibrium between molecular SO2 (as a dissolved gas) and bisulfite ion
- total sulfur dioxide: amount of free and bound forms of S02
- density: the density of water is close to that of water depending on the percent alcohol and sugar content
- pH: describes how acidic or basic a wine is on a scale from 0 (very acidic) to 14 (very basic)
- sulphates: a wine additive which can contribute to sulfur dioxide gas (S02) levels
- alcohol: the percent alcohol content of the wine
Output variable:
- quality (score between 0 and 10)

Config summary:
----------------
Postgres server: neon.tech
Clickhouse cloud: Free Trail

Setup:
----------------
pip install requirements.txt