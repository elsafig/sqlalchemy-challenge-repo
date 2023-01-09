# sqlalchemy-challenge-repo Requirements<br>
Jupyter Notebook Database Connection (10 points)<br>
To receive all points, you must<br>
Use the SQLAlchemy create_engine() function to connect to your SQLite database (1 point)<br><br>

Use the SQLAlchemy automap_base() function to reflect your tables into classes (3 points)<br><br>

Save references to the classes named station and measurement (4 points)<br><br>

Link Python to the database by creating a SQLAlchemy session (1 point)<br><br>

Close your session at the end of your notebook (1 point)<br><br>

Precipitation Analysis (16 points)<br>
To receive all points, you must<br>
Create a query that finds the most recent date in the dataset (8/23/2017) (2 points)<br><br>

Create a query that collects only the date and precipitation for the last year of data without passing the date as a variable (4 points)<br><br>

Save the query results to a Pandas DataFrame to create date and precipitation columns (2 points)<br><br>

Sort the DataFrame by date (2 points)<br><br>

Plot the results by using the DataFrame plot method with date as the x and precipitation as the y variables (4 points)<br><br>

Use Pandas to print the summary statistics for the precipitation data (2 points)<br><br>

Station Analysis (16 points)<br>
To receive all points, you must<br>
Design a query that correctly finds the number of stations in the dataset (9) (2 points)<br><br>

Design a query that correctly lists the stations and observation counts in descending order and finds the most active station (USC00519281) (2 points)<br><br>

Design a query that correctly finds the min, max, and average temperatures for the most active station (USC00519281) (3 points)<br><br>

Design a query to get the previous 12 months of temperature observation (TOBS) data that filters by the station that has the greatest number of observations (3 points)<br><br>

Save the query results to a Pandas DataFrame (2 points)<br><br>

Correctly plot a histogram with bins=12 for the last year of data using tobs as the column to count. (4 points)<br><br>

API SQLite Connection & Landing Page (10 points)<br>
To receive all points, your Flask application must<br>
Correctly generate the engine to the correct sqlite file (2 points)<br><br>

Use automap_base() and reflect the database schema (2 points)<br><br>

Correctly save references to the tables in the sqlite file (measurement and station) (2 points)<br><br>

Correctly create and binds the session between the python app and database (2 points)<br><br>

Display the available routes on the landing page (2 points)<br><br><br>

API Static Routes (15 points)<br>
To receive all points, your Flask application must include<br>
A precipitation route that:<br><br>

Returns json with the date as the key and the value as the precipitation (3 points)<br><br>

Only returns the jsonified precipitation data for the last year in the database (3 points)<br><br>

A stations route that:<br><br>

Returns jsonified data of all of the stations in the database (3 points)<br>
A tobs route that:<br><br>

Returns jsonified data for the most active station (USC00519281) (3 points)<br><br>

Only returns the jsonified data for the last year of data (3 points)<br><br>

API Dynamic Route (15 points)<br>
To receive all points, your Flask application must include<br>
A start route that:<br><br>

Accepts the start date as a parameter from the URL (2 points)<br><br>

Returns the min, max, and average temperatures calculated from the given start date to the end of the dataset (4 points)<br><br>

A start/end route that:<br><br>

Accepts the start and end dates as parameters from the URL (3 points)<br><br>

Returns the min, max, and average temperatures calculated from the given start date to the given end date (6 points)<br><br>

Coding Conventions and Formatting (8 points)<br>
To receive all points, your code must<br>
Place imports at the top of the file, just after any module comments and docstrings, and before module globals and constants. (2 points)<br><br>

Name functions and variables with lowercase characters, with words separated by underscores. (2 points)<br><br>

Follow DRY (Don't Repeat Yourself) principles, creating maintainable and reusable code. (2 points)<br><br>

Use concise logic and creative engineering where possible. (2 points)<br><br>

Deployment and Submission (6 points)<br>
To receive all points, you must<br>
Submit a link to a GitHub repository that’s cloned to your local machine and contains your files. (2 points)<br><br>

Use the command line to add your files to the repository. (2 points)<br><br>

Include appropriate commit messages in your files. (2 points)<br><br>

Comments (4 points)<br>
To receive all points, your code must<br>
Be well commented with concise, relevant notes that other developers can understand. (4 points)
