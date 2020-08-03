from pandas import read_csv, DataFrame
from sklearn.preprocessing import RobustScaler

# Load the data
df = read_csv('https://raw.githubusercontent.com/jbrownlee/Datasets/master/oil-spill.csv',
              header=None,)

# Show the first 5 rows of the data
df.head()

# Define X (Predictor variables) and y (Target variable)
dt = df.values
ix = [i for i in range(dt.shape[1]) if i != 49]
X, y = dt[:, ix], dt[:, 49]

# Scale the data
scaler = RobustScaler()

# Reshaping the variables from 2D to 1D is required before scaling
X = X.reshape(-1, 1)

# Fit and transform scaler on the dataset
X = scaler.fit_transform(X)

# Fit and transform scaler on the dataset
Xtrans = scaler.fit_transform(X)

# Convert NumPy array to Pandas DataFrame
Xtrans = DataFrame(data=Xtrans)

# Show the first 5 rows of the data with scaled values
Xtrans.head()
