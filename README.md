# Data Scaling Techniques
As the name suggests, data scaling refers to the phenomenon of scaling the data. Scaling here refers to limiting the values constituting the data in a specific range, depending upon the nature of the scaling technique used. Data scaling is usually necessary for the machine learning model to make better, accurate precdictions. Data scaling works effectively when the data comprises values that hold different units (like, distance, time difference, amount in a particular currency, etc.). There are three (03) data scaling techniques I know so far. These techniques are implemented through the popular Scikit-learn machine learning library and are used to scale numeric data.

# StandardScaler
StandardScaler works by removing the mean of the data and scales the data to unit variance (variance = 1). Data with unit variance means that the values constituing the dataset are highly unique (high cardinality). View the API reference guide here: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.StandardScaler.html

# MinMaxScaler
MinMaxScaler simply scales the data values between the range of 0-1. View the API reference guide here: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.MinMaxScaler.html

#RobustScaler
The term 'Robust' is used to define the property of RobustScaler being 'robust to outliers', i.e., it nulls the effect of outliers (numerically-distant data that doesn't seem fit in the dataset) since outliers, in most cases, result in inaccurate predictions. View the API reference guide here: https://scikit-learn.org/stable/modules/generated/sklearn.preprocessing.RobustScaler.html
