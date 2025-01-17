from imblearn.over_sampling import ADASYN

def synthesized_Data(X_train, y_train, ratio = float):
    ada = ADASYN(sampling_strategy=ratio)
    x_train_resampled, y_train_resampled = adasyn.fit_resample(X_train, y_train)
    return x_train_resampled, y_train_resampled