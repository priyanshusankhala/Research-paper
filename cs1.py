from webcopy import features
# from web copy import FeatureCreation
import pickle
import pandas
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import joblib



def import_model():
    model_pkl = open('/Users/priyanshusankhala/Documents/rf.pkl', 'rb')
    model = pickle.load(model_pkl)
    return model
def get_score(features):
    model = import_model()
    mdl_pred = model.predict([features])
    mdl_pred_prob = model.predict_proba([features])
    # print(mdl_pred,mdl_pred_prob)
    # return [mdl_pred,mdl_pred_prob]
    return mdl_pred
def import_lg():
    logreg_pkl = open('/Users/priyanshusankhala/Documents/logreg2.pkl', 'rb')
    model_lg = pickle.load(logreg_pkl)
    return model_lg
def get_score_lg(features):
    model_lg = import_lg()
    mdl_pred1 = model_lg.predict([features])
    mdl_pred_prob2 = model_lg.predict_proba([features])
    # print(mdl_pred1,mdl_pred_prob2)
    # return [mdl_pred1,mdl_pred_prob2]
    return mdl_pred1
def import_dt():
    dt_pkl = open('/Users/priyanshusankhala/Documents/dt2.pkl', 'rb')
    model_dt = pickle.load(dt_pkl)
    return model_dt
def get_score_dt(features):
    model_dt = import_dt()
    mdl_pred3 = model_dt.predict([features])
    mdl_pred_prob3 = model_dt.predict_proba([features])
    #print(mdl_pred3,mdl_pred_prob3)
    #return [mdl_pred3,mdl_pred_prob3]
    return mdl_pred3
def max_no_in_list(features):
    # testList = [get_score(),get_score_lg(), get_score_dt()]
    r_f = get_score(features)
    l_g = get_score_lg(features)
    d_t = get_score_dt(features)
    kite = [r_f, l_g, d_t]
    kite = tuple(kite)
    # print(kite)
    print(max(tuple(kite), key = kite.count))
    # # return kite
    #print(max(set(kite), key = kite.count))
    # Takes vote and print max. probalblity  

get_score(features)
get_score_lg(features)
get_score_dt(features)
# ist = [get_score(),get_score_lg(), get_score_dt()]
max_no_in_list(features)