# Prediction of Product Sales

## Analyzing Predictors for Big Mart's Item Sales by Outlet 

David Atkins

### <><>

## Data Source: 
BigMart Sales Data 
https://www.kaggle.com/datasets/brijbhushannanda1979/bigmart-sales-data

For this dataset, there were 8523 rows and 12 columns.

## Data Dictionary

<p align = "center"> 
  ![Data_Dictionary](https://github.com/Gondram/Prediction-of-Product-Sales/assets/8175014/a76d0afd-ad07-40ed-bc59-c8a15e72ec11 "Data Dictionary")
</p>


## To prepare this data, the data was cleaned, and the following processes were performed:

### Exploratory Data Analysis
    - During the exploratory data analysis, a boxplot and histogram was visualized for each numeric datatype column. 
    - Also, a barplot was visualized for each categorical column. 
    - This gave a good baseline for all of the numeric and categorical columns for univariate EDA.
    

<p align = "center"> 
![item_visibility_hist](https://github.com/Gondram/Prediction-of-Product-Sales/assets/8175014/68852655-7b6d-4994-a929-6a433b9ab844)
</p>

This histogram shows that the majority of the salaries are around $100,000.


 ### Expanatory Data Analysis
    - To visualize the data for explantory purposes, three bargraphs were chosen and one linegraph was chosen.
    - The bargraphs were chosen to show how the categories compare to each other. 
    - Finally, a linegraph was chosen to show the trend of salaries over the past three years. 


## Explanatory Visuals

<p align = "center"> 
![big_mart_sales_heatmap](https://github.com/Gondram/Prediction-of-Product-Sales/assets/8175014/f014c9ae-7bb2-4c6a-b2d4-85f81b3fdd1b)
</p>

There is a moderate positive correlation between item MRP (the list price) and item sales. 

<p align = "center"> 
![item_visibility_hist](https://github.com/Gondram/Prediction-of-Product-Sales/assets/8175014/68852655-7b6d-4994-a929-6a433b9ab844)
</p>

The Item visibility mean is higher than median. This likely reflects the fact that nothing can go below 0% visibility, so the curve skews positive.

<p align = "center"> 
  <img src = "https://lh3.googleusercontent.com/drive-viewer/AITFw-wctmTdTcf8LMX-wWkk8mM1GKWGkAdmenQqe6wcu61JDxvMPG17cW8l5k58BtXWPom8zfkVQU8E3Z5yWvHOadYneJ44=s2560">
</p>

This graph shows that item visibility has a very slight negative trend in relation to sales.



 ### Machine Learning Using the Following Models:
    - Linear Regression Model
    - Random Forest Regressor Model
    - Tuned Random Forest Regressor Model
    
    
## Models Evaluated & Results

- Linear Regression Model (Testing Set):
  - R^2: 0.567
  - MAE: 803.927
  - MSE: 1194032.031
  - RMSE: 1092.718

- Random Forest Regressor Model (Testing Set):
  - R^2: 0.559
  - MAE: 766.587
  - MSE: 1216867.058
  - RMSE: 1103.117

- Tuned Random Forest Regressor Model (Testing Set):
  - R^2: 0.600
  - MAE: 731.019
  - MSE: 1,102,724.272
  - RMSE: 1,050.107


- The Final Model Chosen was a `Random Forest Regressor Model` with the n_estimators tuned to 10, max_depth tuned to 5, min_samples_leaf tuned to 2, and min_samples_split.
- For the testing set on the model, `60%` of the variance in y was explained by x. 
- The Mean Absolute Error was off by about `$731.02`.
- The Mean Squared Error was `$1,102,724.27`.
- The Root Mean Squared Error had a calculation of `$1,050.11`.

Using this model to make predictions about the best places to live and which careers to choose to earn the most money would not be a very reliable. Considering the previous regression metrics from how the model performed, there is a disparity between the R^2 score and also the Root Mean Squared Error that cannot be ignored.

## Recommendations

Data Science Insights

- For those who have an interest in Data Science:
  - Data Analytics Leads & Principal Data Engineers earn the most amount of money. However, this are usually not entry level careers and I would recommend going through a program, like Coding Dojo, where you can earn your data science certificate and then map out your career to these positions.

  - Data Engineers & Data Scientists have the most 100% remote positions. So, if you are wanting to work from home, or work from anywhere in the world, choosing one of the top five remote positions would be a good choice to build your career upon.
  
  - Lastly, the trend for the last three years show that data science and related fields are increasingly earning more money each year. So, choosing a career in one of these fields can be very lucrative.

Model Performance
- Overall, the best model is definitely the tuned Random Forest Regressor Model. There was still some bias in the model, but by far it outperformed the linear regression model. 


## Limitations & Next Steps

From here, a student could use the insights from the visuals on how to tailor their path for their career. As mentioned before, Coding Dojo has a fantastic program that prepares inspiring data scientists for the field of data science. 

## For Further Information

For any additional questions, please contact: 
- David Atkins (Data Analyst)
- gondram@gmail.com

