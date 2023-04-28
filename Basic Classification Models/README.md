# Function: run_basic_classification_models

The `run_basic_classification_models` function trains and evaluates multiple machine learning models, such as LogisticRegression, GradientBoostingClassifier, RandomForestClassifier, and XGBClassifier, on a given dataset. It takes in the following arguments:

- `X_train`: a pandas dataframe of training features
- `y_train`: a pandas series of training labels
- `X_test`: a pandas dataframe of test features
- `y_test`: a pandas series of test labels
- `models` (optional): dictionary for models that need to be fitted. Defaults to `None`, which means the models specified in the function will be used.
- `hyperparams` (optional): dictionary of hyperparameters for each model. Defaults to `None`, which means the parameters specified in the function will be used.
- `model_type` (optional): a string indicating the type of dataset. Defaults to 'Non-balanced'.
- `roc_plot` (optional): boolean parameter to plot roc curve for all the models.

The function returns two values:

- `models_report`: a pandas dataframe with evaluation metrics for each model, such as matthews_corrcoef, roc_auc_score, precision_score, recall_score, and f1_score.
- `conf_matrix`: a dictionary containing the confusion matrix for each model.

Note: The function uses the following modules:

- `pandas`: A data manipulation library that is used to handle data in the form of dataframes.
- `matplotlib`: A data visualization library that is used to plot ROC curves.
- `sklearn`: A machine learning library that is used to import machine learning algorithms and evaluation metrics.
- `xgboost`: A machine learning library that is used to import the XGBClassifier algorithm.
