import pandas as pd
from sklearn.preprocessing import OneHotEncoder
import matplotlib.pyplot as plt
import numpy as np
from sklearn.preprocessing import StandardScaler
import seaborn as sns

# Loading data and column names
data = pd.read_csv(r"C:\Users\NTres\OneDrive\Documents\GitHub\Brain_stroke_classification\brain_stroke.csv")
column_names = data.columns.tolist()

# Checking number of missing data and data types in columns
for column in column_names:
    Sum = data[column].isna().sum()
    if Sum > 0:
        print("Column {} contains {} Nan values.".format(column, Sum))
    print("Column {} consists of {}".format(column, data[column].dtype))


data.describe()

pd.set_option('display.max_columns', None)
# Use pd.get_dummies to perform one-hot-encoding
encoded_data = pd.get_dummies(data, columns=["gender", "ever_married", "work_type", "Residence_type", "smoking_status"],dtype='int')
column_names = encoded_data.columns.tolist() #Updating column names
# Extracting features (excluding target variable):
features = encoded_data.drop(columns=['stroke'])
# Inspecting data:
encoded_data.describe()

# Visualizing the avg. glucose levels to try determine whether there are outliers or not. 

sns.histplot(features["avg_glucose_level"], kde=True)
plt.title("Distribution of Avg. Glucose Level")
plt.show()

sns.boxplot(features["avg_glucose_level"])
plt.title("Boxplot of Avg. Glucose Level")
plt.show()


features["avg_glucose_level"].describe()

# Standardizing columns:

#Defining scaler
scaler = StandardScaler()

# Convert scaled features back to DataFrame
binary_features = features[["hypertension", "heart_disease", "gender_Female", "gender_Male", "ever_married_No", "ever_married_Yes",	"work_type_Govt_job", "work_type_Private", "work_type_Self-employed", "work_type_children",	"Residence_type_Rural",	"Residence_type_Urban",	"smoking_status_Unknown", "smoking_status_formerly smoked",	"smoking_status_never smoked",	"smoking_status_smokes"]]
continuous_features = features[["age", "avg_glucose_level", "bmi"]]
scaled_continuous = scaler.fit_transform(continuous_features)
scaled_continuous_df = pd.DataFrame(scaled_continuous, columns=continuous_features.columns, index=features.index)

#Combine continuous and discrete features:
features_df = pd.concat([scaled_continuous_df, binary_features], axis=1)
features_df.describe()

fig = plt.figure(figsize=(10,10))
plt.matshow(features_df.corr(), fignum=fig.number)

# Colorbar
cb = plt.colorbar(pad=0.1)
cb.ax.tick_params(labelsize=10)

# Set x-tick locations and labels
num_columns = len(features_df.columns)  # Get the number of columns in the data
xticks_locations = np.arange(num_columns)  # X-axis positions (range from 0 to number of columns)
plt.xticks(xticks_locations, features_df.columns, rotation=45, ha='left', va='bottom')  # Set the column names as labels

# Set y-tick locations and labels (similar to xticks)
yticks_locations = np.arange(num_columns)  # Y-axis positions
plt.yticks(yticks_locations, features_df.columns)  # Set the column names as labels for the y-axis

# Set the title
plt.title('Correlation Matrix', fontsize=16)

# Show the plot
plt.show()