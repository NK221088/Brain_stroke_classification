from Loaded_data import features_df, encoded_data
from sklearn.model_selection import train_test_split

X = features_df.to_numpy()
y = encoded_data["stroke"].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(
    X, y, 
    test_size=0.2, 
    random_state=99,
    stratify=y
)