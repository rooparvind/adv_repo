Simple Streamlit app & deployment to Render.com

Project Overview

This project focuses on analyzing a dataset of used cars, containing various attributes such as price, model year, condition, odometer reading, fuel type, and more. The goal is to clean, process, and extract insights from the data to support decision-making related to car sales and pricing trends.

Data Description

The dataset includes the following columns:
price: Listed price of the vehicle.
model_year: Year of manufacturing.
model: Make and model of the vehicle.
condition: The stated condition of the car (e.g., good, excellent, fair).
cylinders: Number of engine cylinders.
fuel: Type of fuel used (e.g., gas, diesel, electric).
odometer: Distance the vehicle has traveled.
transmission: Type of transmission (e.g., automatic, manual).
type: Vehicle type (e.g., SUV, pickup, sedan).
paint_color: Exterior color of the vehicle.
is_4wd: Indicates if the vehicle has four-wheel drive.
date_posted: Date when the listing was posted.
days_listed: Number of days the vehicle has been listed for sale.

Sample Use Case

This dataset can be used to:
Analyze price trends based on model year, condition, and mileage.
Identify the most common car models and types in the used car market.
Detect potential anomalies or inconsistencies in pricing.

Project Structure

data/: Contains raw and processed datasets.
notebooks/: Jupyter notebooks for exploratory data analysis and model development.
README.md: Project documentation.

Future Improvements
Handling missing values and outliers for better data integrity.
Implementing machine learning models for price prediction.
Enhancing visualizations for improved insights.


Prerequisites
Pipenv

Install dependencies
pipenv shell
pipenv install

Run the app locally
streamlit run app.py
The app will be accessiable at http://localhost:8501/

Deploy the app to Render

![alt text](<Screenshot 2025-02-17 at 11.26.14 AM-1.png>)

Verify that your application is accessible at the following URL: [https://adv-repo.onrender.com](https://adv-repo.onrender.com)