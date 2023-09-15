# Prediction of Product Sales

## Analyzing Predictors for Big Mart's Item Sales by Outlet 

David Atkins

## Data Source: 
BigMart Sales Data 
https://www.kaggle.com/datasets/brijbhushannanda1979/bigmart-sales-data

For this dataset, there were 8523 rows and 12 columns.

## Data Dictionary

<p align = "center"> 
  <img src = "https://github.com/Gondram/Prediction-of-Product-Sales/assets/8175014/a76d0afd-ad07-40ed-bc59-c8a15e72ec11">
</p>


## To prepare this data, the data was cleaned, and the following processes were performed:

### Exploratory Data Analysis
    - During the exploratory data analysis, a boxplot and histogram was visualized for each numeric datatype column. 
    - Also, a barplot was visualized for each categorical column. 
    - This gave a good baseline for all of the numeric and categorical columns for univariate EDA.
    

<p align = "center"> 
  <img src = "https://github.com/Gondram/Prediction-of-Product-Sales/assets/8175014/68852655-7b6d-4994-a929-6a433b9ab844">
</p>

This histogram shows that the majority of the salaries are around $100,000.


 ### Expanatory Data Analysis
    - To visualize the data for explantory purposes, three bargraphs were chosen and one linegraph was chosen.
    - The bargraphs were chosen to show how the categories compare to each other. 
    - Finally, a linegraph was chosen to show the trend of salaries over the past three years. 


## Explanatory Visuals

<p align = "center"> 
  <img src = "https://github.com/Gondram/Prediction-of-Product-Sales/assets/8175014/f014c9ae-7bb2-4c6a-b2d4-85f81b3fdd1b">
</p>

There is a moderate positive correlation between item MRP (the list price) and item sales. 

<p align = "center"> 
  <img src = "https://github.com/Gondram/Prediction-of-Product-Sales/assets/8175014/68852655-7b6d-4994-a929-6a433b9ab844">
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


- The Final Model Chosen was a `Random Forest Regressor Model` with the n_estimators tuned to 10, max_depth tuned to 5, min_samples_leaf tuned to 2, and min_samples_split set to.
- For the testing set on the model, `60%` of the variance in y was explained by x. 
- The Mean Absolute Error was off by about `$731.02`.
- The Mean Squared Error was `$1,102,724.27`.
- The Root Mean Squared Error had a calculation of `$1,050.11`.

Using this model to make predictions about projected sales would only be moderately reliable. The train and test R-squared and RMSE are very similar. This model reliably explains 60% of the sales variance.

## Model Insights

<p align = "center"> 
  <img src = "https://i.imgur.com/DR9El3T.png">
</p>

- The 3 most impactful coefficients are for:
    - "Outlet_Establishment_Year" - The later the outlet establishment year the higher the predicted outlet sales. This implies an early surge in sales when an outlet is newer.
    - "Outlet_Identifier_OUT046" - This specific outlet has significantly higher predicted sales.
    - "Outlet_Size_High" - The largest Outlets have higher predicted sales
    - 
<p align = "center"> 
  <img src = "https://i.imgur.com/ulrdCe3.png">
</p>

- The Five Most Important Features Are: 
 - Item_MRP
 - Outlet_Type_Grocery_Store
 - Item_Visibility
 - Item_Weight
 - Outlet_Identifier_OUT027

An 'Important' feature is one that was used extensively by the model. None of these indicate directionality.

## Recommendation

Model Performance
- Overall, the best model is definitely the tuned Random Forest Regressor Model. The model is neither overly overfit or underfit. The model outperformed the linear regression.

## For Further Information

For any additional questions, please contact: 
- David Atkins (Data Analyst)
- gondram@gmail.com

