import pandas as pd
import matplotlib.pyplot as plt
from sklearn.metrics import roc_curve, roc_auc_score, matthews_corrcoef, precision_score, recall_score, f1_score
from sklearn.ensemble import GradientBoostingClassifier, RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from xgboost import XGBClassifier

def run_basic_classification_models(X_train, y_train, X_test, y_test, models=None, hyperparams=None,model_type='Non-balanced', roc_plot=True):
    """
    Train and evaluate LogisticRegression, GradientBoostingClassifier, 
    RandomForestClassifier, XGBClassifier models on the given dataset. 
    
    Arguments:
    X_train -- a pandas dataframe of training features
    y_train -- a pandas series of training labels
    X_test -- a pandas dataframe of test features
    y_test -- a pandas series of test labels
    models -- dictionary for models which needs to be fitted, Defaults to None --> models specified in function
    hyperparameters -- dictionary of hyperparameters as per the models, Defaults to None --> parameters specified in function
    model_type -- a string indicating the type of dataset, Defaults to 'Non-balanced'
    roc_plot -- boolean parameter to plot roc curve for all the models
    
    Returns:
    models_report -- a pandas dataframe with evaluation metrics for each model
    conf_matrix -- a dictionary containing the confusion matrix for each model
    """

    if not models:
        models = {'GradientBoosting': GradientBoostingClassifier(),
                  'LogisticRegression' : LogisticRegression(),
                  'RandomForestClassifier': RandomForestClassifier(),
                  'XGBClassifier': XGBClassifier()
                 }
        
    if not hyperparams:
        hyperparams = {'GradientBoosting': {'max_depth': 6, 'n_estimators': 100, 'max_features': 0.3},
                       'LogisticRegression': {'C': 1.0},
                       'RandomForestClassifier': {'n_estimators': 10},
                       'XGBClassifier': {}
                      }
    
    cols = ['model', 'matthews_corrcoef', 'roc_auc_score', 'precision_score', 'recall_score', 'f1_score']
    models_report = pd.DataFrame(columns=cols)
    conf_matrix = {}
    for clf_name, clf in models.items():
        try:
            hyperparams_clf = hyperparams.get(clf_name, {})
            clf.set_params(**hyperparams_clf)
            
            clf.fit(X_train, y_train)

            y_pred = clf.predict(X_test)
            y_score = clf.predict_proba(X_test)[:,1]

            print('computing {} - {} '.format(clf_name, model_type))

            tmp = pd.Series({
                'model_type': model_type,
                'model': clf_name,
                'roc_auc_score': roc_auc_score(y_test, y_score),
                'matthews_corrcoef': matthews_corrcoef(y_test, y_pred),
                'precision_score': precision_score(y_test, y_pred),
                'recall_score': recall_score(y_test, y_pred),
                'f1_score': f1_score(y_test, y_pred)
            })

            models_report = models_report.append(tmp, ignore_index=True)
            conf_matrix[clf_name] = pd.crosstab(y_test, y_pred, rownames=['True'], colnames=['Predicted'], margins=False)
            
            fpr, tpr, thresholds = roc_curve(y_test, y_score, drop_intermediate=False, pos_label=1)

            if roc_plot:
                plt.figure(1, figsize=(6, 6))
                plt.xlabel('false positive rate')
                plt.ylabel('true positive rate')
                plt.title('ROC curve - {}'.format(model_type))
                plt.plot(fpr, tpr, label=clf_name)
                plt.legend(loc=2, prop={'size': 11})
                
        except Exception as e:
            print(f"Error occurred while computing {clf_name} - {model_type}: {e}")
            continue
    
        else:
            if roc_plot:
                plt.plot([0,1], [0,1], color='black')
            return models_report, conf_matrix
