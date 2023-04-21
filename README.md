# Data Analytics Migration to Tableau

Scenario: Take on the role of a Data Analyst at Skyscanner and work on a project requirement to migrate existing data analytics tasks from an Excel-based manual system into interactive Tableau reports.

## Milestone 1

- Set up the dev environment.

## Milestone 2

- Load the CSV data files into Pandas dataframes.
- Clean the data to remove any columns which contain all NA records. Replace any records which still contain NAs with zeros.
- Integrate all of the dataframes together into one master dataframe.
- Export the master dataframe into one file 'combined_data.csv'. Copy the file to S3 bucket.

## Milestone 3

- Connect pgAdmin4 to the PostgreSQL RDS database.
- Import the 'combined_data.csv' and explore the data.
- Using SQL, answer the below business queries;
    - Which year had the most number of total inbound and outbound flights?
    - Which country is the most popular destination for flights?

## Milestone 4

- Install Tableau desktop on local machine.
- Configure Tableau to be used with PostgreSQL and connect to the RDS database.

## Milestone 5

 - Create a variety of analytical reports based on the flights dataset in Tableau;
    - Where are the top flight destinations?
    - What is the average distance airplanes travel for all carriers?
    - What are the top most used flight numbers and their destinations?
    - Which airports have the most arrival delays, departure delays & cancellations?