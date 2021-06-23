===== NBA : Game prediction using deep learning =====

Dataset folder contains the data file used for the project.

Dataset is taken from Kaggle NBA dataset. 

https://www.kaggle.com/pablote/nba-enhanced-stats

Context:

Dataset is based on box score and standing statistics from the NBA.
Calculations such as number of possessions, floor impact counter, strength of schedule, and simple rating system are performed.
Finally, extracts are created based on a perspective:
	•	teamBoxScore.csv communicates game data from each teams perspective
	•	officialBoxScore.csv communicates game data from each officials perspective
	•	playerBoxScore.csv communicates game data from each players perspective
	•	standing.csv communicates standings data for each team every day during the season

Data Sources:

Box score and standing statistics were obtained by a Java application using RESTful APIs provided by xmlstats.

Calculation Sources:

Another Java application performs advanced calculations on the box score and standing data. 
Formulas for these calculations were primarily obtained from these sources:
	•	https://basketball.realgm.com/info/glossary
	•	https://www.nbastuffer.com/team-evaluation-metrics/
	•	https://www.basketball-reference.com/about/glossary.html



