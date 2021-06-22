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
    return model.predict(v)  # To give probablity viz. 1,0
    return model.perdict_proba(v)  # To give probablity value
def import_lg():
    logreg_pkl = open('/Users/priyanshusankhala/Documents/logreg.pkl', 'rb')
    model_lg = pickle.load(logreg_pkl)
    return model_lg
def get_score_lg(v):
    model_lg = import_lg()
    return model_lg.predict(v)  # To give probablity viz. 1,0
    return model_lg.perdict_proba(v)  # To give probablity value
def import_dt():
    dt_pkl = open('http://localhost:8888/files/Documents/descisiontress_model.sav', 'rb')
    model_dt = pickle.load(dt_pkl)
    return model_dt
def get_score_dt(v):
    model_dt = import_dt()
    return model_dt.predict(v)  # To give probablity viz. 1,0
    return model_dt.perdict_proba(v)  # To give probablity value


# def import_dt():
#     loaded_model = joblib.load(filename2)
#     result = loaded_model.score(v)
#     return result