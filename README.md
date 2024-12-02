
Flask MySQL and MongoDB API Projects with EDA Practice

This repository contains projects that demonstrate the integration of Flask APIs with MySQL and MongoDB, along with exploratory data analysis (EDA) practices. The repository showcases CRUD operations using Flask, database manipulation in MySQL and MongoDB, and Python-based data handling.

Features

1. Flask API with MySQL

	•	Database Setup:
	•	Automatically creates the tasksql database and the mysqltable table if they do not exist.
	•	Supports CRUD operations through RESTful APIs.
	•	API Endpoints:
	•	/inserttablevalues (POST): Insert records into the MySQL table.
	•	/updatetable (POST): Update a record in the MySQL table.
	•	/deletetablevalues (POST): Delete a record from the MySQL table.
	•	/fetchvalues (GET): Fetch all records from the MySQL table.
	•	Technologies Used:
	•	Flask for API development.
	•	MySQL for relational data management.

2. Flask API with MongoDB

	•	Database Setup:
	•	Uses MongoDB Atlas as the cloud database service.
	•	Connects via the MongoDB Python driver pymongo.
	•	Data Models:
	•	Example JSON data structures for various domains like personal details, company records, and medication details.
	•	CRUD Operations:
	•	Insert single/multiple documents.
	•	Query documents using MongoDB filters ($gt, $or, etc.).
	•	Update and delete operations.
	•	Technologies Used:
	•	Flask for API development.
	•	MongoDB for document-based data storage.

3. Exploratory Data Analysis (EDA)

	•	Demonstrates EDA using Python with datasets for analysis.
	•	Includes data filtering, querying, and transformations.
	•	Employs MongoDB for querying structured data.

4. General Examples and Practices

	•	Examples of filtering, querying, and updating data in MongoDB using:
	•	Conditional filters ($in, $gte, $or, etc.).
	•	Update operations ($set).
	•	Delete operations.

How to Use

Prerequisites

	•	Python 3.x installed.
	•	MySQL installed locally or accessible remotely.
	•	MongoDB Atlas account or a locally running MongoDB instance.

Setup Instructions

	1.	Clone the repository:

git clone https://github.com/Nikitha130731/Python.git
cd your-repository


	2.	Install dependencies:

pip install -r requirements.txt


	3.	Run the Flask application:
	•	For MySQL-based APIs:

python flask_mysql_api.py


	•	For MongoDB-based APIs:

python flask_mongodb_api.py


	4.	Access APIs via Postman or a browser.

Example Data Models

MySQL Table: mysqltable

Column Name	Data Type
name	VARCHAR(30)
number	INT

MongoDB Data

	•	Personal Data:

{
    "name": "Nikitha",
    "email": "nikitha@gmail.com",
    "surname": "Kondreddy",
    "subject": ["data science", "big data", "data analytics"]
}


	•	Company Records:

{
    "company_name": "ineuron",
    "product": "Affordable AI",
    "course_offered": "ML with deployment"
}


	•	Medication Data:

{
    "name": "lisinopril",
    "strength": "10 mg Tab",
    "dose": "1 tab",
    "route": "PO",
    "sig": "daily",
    "pillCount": "#90",
    "refills": "Refill 3"
}



Project Highlights

	•	Combines API development with database management.
	•	Showcases practical use of Flask with both relational and NoSQL databases.
	•	Provides real-world use cases like filtering and querying structured and unstructured data.

Future Enhancements

	•	Include more robust error handling.
	•	Expand API functionality with authentication.
	•	Add support for additional data models.

Repository Contents

	•	flask_mysql_api.py: Flask API for MySQL integration.
	•	flask_mongodb_api.py: Flask API for MongoDB integration.
	•	eda_practice.py: Python-based EDA examples and practices.

