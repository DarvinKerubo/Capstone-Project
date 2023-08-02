# ANALYZING & FORECASTING GROSS DOMESTIC PRODUCT (GDP) TRENDS (Case Study - Kenya)
## Introduction
Kenyan Parliament recently, on the 26th June 2023, passed to law the contentious Finance Bill 2023 proposing a raft of tax policy measures which aim to yield additional revenue and explore more effective measures to enhance Country's revenue collection.

The House argued that, in comparison to other comparable African countries’ Tax revenue as a percentage of Gross Domestic Product (GDP) like Botswana’s 24 percent, Mauritius’ 18 percent and Zambia’s 17 percent, Kenya was falling behind in terms of tax revenue collection at 13 percent as at 2021. The mentioned countries have since managed to achieve higher tax revenue collection rates thus highlighting the need to reassess Country's tax policies and explore more effective measures to enhance revenue collection.

The Government feels the ratio of tax revenue as a percentage of Gross Domestic Product (GDP) being well below acceptable levels to enable spur economic growth & reduce cost of living in the long term. (According to the World Bank, tax revenues above 15% of a country’s GDP are a key ingredient for economic growth and, ultimately, poverty reduction)

Some of the questions a taxpayer might ask based on the proposed bill might include:

Is GDP level growing proportionately to the projected tax revenue collections to enable government meet its target?

Hence GDP becomes a critical factor to explore, predict and assist determine if the country is in line to achieve its bold aspirations within the next 3-4 years.

## Business Understanding
The tax-to-GDP ratio is a measure of a nation's tax revenue relative to the size of its economy. GDP is a vital economic indicator that reflects the overall economic performance of countries and guides policy-making, investment decisions, and strategic planning.

Project shall aim to analyse Country's historical GDP trends and forecast future GDP growth. The analysis shall assist provide insights into economic growth patterns, identify emerging trends, and support evidence-based decision-making for various stakeholders.

## Data Understanding & Preparation
Data downloaded from The World Bank website database (https://datatopics.worldbank.org/world-development-indicators) and saved remotely for preprocessing. Our target variable (GDP) & other features/indicators columns collected over a period of time explained as below: Daily data aggregated (Weighted average aggregation method); annualized & expressed in U.S. Dollars for each period unless stated otherwise.

Year: Annual periodicity (62 year trend analysis obtained between 1960 & 2022)
GDP: Gross Domestic Product
Exports: Total transactions value in goods and services from residents to non-residents
Imports: Total transactions value in goods and services from non-residents to residents.
ExchRate: Exchange Rate - Local currency per U.S. Dollar period average expressed in National Currency Unit
InfRte: Inflation Rate
Population: Total Population of a country
TaxRev: Total tax revenue collected.
LbrFrce: Labor Force
UnEmpRte: Unemployment Rate
EmpRte: Employment Rate
GrossDomSavg: Gross Domestic Savings
GrossConsump: Gross Consumption/Expenditure
IntPen:Individuals using the Internet (% of population): Internet Penetration Rate
AgriOutput: Agriculture, forestry, and fishing, value added; generally focuses on production or manufacturing processes, marketing or services that increase the value of primary agricultural commodities
## Modelling, Prediction & Evaluation
For Evaluating the performance of our chosen model, we can use the following accuracy metrics:

Mean Squared Error (MSE): It measures the average squared difference between the actual and predicted values. The lower the MSE, the better the model's performance.

Root Mean Squared Error (RMSE): It is the square root of the MSE and gives us an idea of how much the predictions deviate from the actual values in the same unit as the target variable.

Mean Absolute Error (MAE): It measures the average absolute difference between the actual and predicted values. It is less sensitive to outliers compared to MSE and RMSE.

Mean Absolute Percentage Error (MAPE): It measures the average percentage difference between the actual and predicted values. It is a relative measure and can be used to compare the performance of models on datasets with different scales.

## Auto-Regressive Model
The equation for the AR model (Yt = C + b1 Yt-1 + b2 Yt-2+……+ bp Yt-p + Ert)
Where: p denotes past values; Yt functions of different past values; Ert Errors in time; C intercept

## ARIMA Model (AutoRegressive Integrated Moving Average)
Time series forecasting model that uses the past values of a time series to predict the future values. ARIMA model has three parameters (p, d, q), where p is the order of the autoregressive (AR) term, d is the degree of differencing required to make the time series stationary, and q is the order of the moving average (MA) term.

Formula: (AR + I + MA = ARIMA);
Where AR Uses past values to predict the future; I Uses the differencing of observation and makes the stationary data & MA Uses past error terms in the given series to predict the future
## SARIMA Model
Optimal parameter selection for the ARIMA Time Series Model.

The first step towards fitting an ARIMA model is to find the values of ARIMA(p,d,q)(P,D,Q)s that produce the desired output. Selection of these parameters requires domain expertise and time. We shall first generate small ranges of these parameters and use a "grid search" to iteratively explore different combinations of parameters. For each combination of parameters, we fit a new seasonal ARIMA model with the SARIMAX() function from the statsmodels library and assess its overall quality.

## CONCLUSION
In this project, we used Kenya's statistics from world bank dataset to build a GDP predictor.

3 different learning regressors (Auto Regressive Model (AR), AutoRegressive Integrated Moving Average (ARIMA); and Seasonal ARIMA (SARIMA)) were tested, and we have acheived the best prediction performance using SARIMA model with least MSE score and less prone to overfitting.

An MSE that is close to 0 indicates that the estimator is predicting observations of the parameter with perfect accuracy, which would be an ideal scenario but it is not typically possible.

## LIMITATIONS
A clear limitation here is the size of the datasets and critical missing values (Tax Revenue Collections most affected column).
