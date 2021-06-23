from web import FeatureCreation
import pickle
import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import joblib



def import_model():
    model_pkl = open('/Users/priyanshusankhala/Documents/rf.pkl', 'rb')
    model = pickle.load(model_pkl)
    return model
def get_score(v):
    model = import_model()
    mdl_pred = model.predict(v)
    mdl_pred_prob = model.perdict_proba(v)
    return [mdl_pred,mdl_pred_prob]    
    # return model.predict(v)  # To give probablity viz. 1,0
    # return model.perdict_proba(v)  # To give probablity value
def import_lg():
    logreg_pkl = open('/Users/priyanshusankhala/Documents/logreg.pkl', 'rb')
    model_lg = pickle.load(logreg_pkl)
    return model_lg
def get_score_lg(v):
    model_lg = import_lg()
    mdl_pred1 = model_lg.predict(v)
    mdl_pred_prob2 = model_lg.perdict_proba(v)
    
    return [mdl_pred1,mdl_pred_prob2]
def import_dt():
    dt_pkl = open('http://localhost:8888/files/Documents/descisiontress_model.sav', 'rb')
    model_dt = pickle.load(dt_pkl)
    return model_dt
def get_score_dt(v):
    model_dt = import_dt()
    mdl_pred3 = model_dt.predict(v)
    mdl_pred_prob3 = model_dt.perdict_proba(v)
    
    return [mdl_pred3,mdl_pred_prob3]
def max_no_in_list(testList):
    testList = [get_score(),get_score_lg(), get_score_dt()]
    print(max(set(testList), key = testList.count))
    # Takes vote and print max. probalblity

# def import_dt():
#     loaded_model = joblib.load(filename2)
#     result = loaded_model.score(v)
#     return result