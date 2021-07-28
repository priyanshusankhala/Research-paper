from webcopy2 import features,displayurl
# from web copy import FeatureCreation
import pickle
import pandas as pd
from sklearn import model_selection
from sklearn.linear_model import LogisticRegression
import joblib
import csv
from scipy.stats import mode
from itertools import chain


def import_model():
    model_pkl = open('/Users/priyanshusankhala/Documents/rf3.pkl', 'rb')
    model = pickle.load(model_pkl)
    return model
def get_score(features):
    scores_rf = []
    model = import_model()
    for i in features:
        scores_rf.append(model.predict([i]))
    
    #mdl_pred_prob = model.predict_proba([features])
    # print(mdl_pred,mdl_pred_prob)
    # return [mdl_pred,mdl_pred_prob]
    return scores_rf
def get_probab_rf(features):
    pro_rf = []
    model = import_model()
    for r in features:
        pro_rf.append(model.predict_proba([r]))
    return pro_rf
# def import_model_all():
#     model_pkl = open('/Users/priyanshusankhala/Documents/rf3.pkl', 'rb')
#     model = pickle.load(model_pkl)
#     return model

# def get_probab_all(features):
#     pro_rf = []
#     model = import_model_all()
    
#     for r in features:
#         pro_rf.append(model.predict_proba([r]))
#     return pro_rf


def import_lg():
    logreg_pkl = open('/Users/priyanshusankhala/Documents/logreg3.pkl', 'rb')
    model_lg = pickle.load(logreg_pkl)
    return model_lg
def get_score_lg(features):
    scores = []
    model_lg = import_lg()
    for i in features:
        scores.append(model_lg.predict([i]))
    # print(scores)
    # df = pandas.DataFrame(features, columns= ['ROP', 'Title', 'TN', 'Meta', 'MN', 'LVTN', 'LVDN', 'Links', 'Word', 'DCNAIH', 'RatioWL'])
    # df['geturl'] = geturl
    # df['score'] = scores
    # print(df)
    return scores
def get_probab_lg(features):
    pro_lg = []
    model_lg = import_lg()
    for r in features:
        pro_lg.append(model_lg.predict_proba([r]))
    
    return pro_lg
    # print(mdl_pred1,mdl_pred_prob2)
    # return [mdl_pred1,mdl_pred_prob2]
    #return mdl_pred1
def import_dt():
    dt_pkl = open('/Users/priyanshusankhala/Documents/dt3.pkl', 'rb')
    model_dt = pickle.load(dt_pkl)
    return model_dt
def get_score_dt(features):
    scores_dt = []
    model_dt = import_dt()
    for i in features:
        scores_dt.append(model_dt.predict([i]))
    return scores_dt
def get_probab_dt(features):
    pro_dt = []
    model_dt = import_dt()
    for r in features:
        pro_dt.append(model_dt.predict_proba([r]))
    return pro_dt
    
    #mdl_pred_prob3 = model_dt.predict_proba([features])
    #print(mdl_pred3,mdl_pred_prob3)
    #return [mdl_pred3,mdl_pred_prob3]
def import_st():
    st_pkl = open('/Users/priyanshusankhala/Documents/clf3.pkl', 'rb')
    model_st = pickle.load(st_pkl)
    return model_st
def get_probab_st(features):
    pro_st = []
    model_st = import_st()
    for r in features:
        pro_st.append(model_st.predict_proba([r]))
    return pro_st

def display_values(features):
    #df = pandas.DataFrame(features, columns= ['ROP'])
    df = pd.DataFrame()
    df['geturl'] = displayurl
    df['score'] = get_score_lg(features)
    df['score_rf'] = get_score(features)
    df['score_dt'] = get_score_dt(features)
    df['Max. Voting'] = max_no_in_list(features)
    df['probability lg'] = get_probab_lg(features)
    df['probability rf'] = get_probab_rf(features)
    df['probability dt'] = get_probab_dt(features)
    df['Max. Confidence'] = get_probab_st(features)
    #df['Max. Voting'] = confidence_range(features)
    df.to_csv('/Users/priyanshusankhala/Downloads/stat_out.csv')
    print(df)
    

def max_no_in_list(features):
    # testList = [get_score(),get_score_lg(), get_score_dt()]
    r_f = get_score(features)
    l_g = get_score_lg(features)
    d_t = get_score_dt(features)
    #kite = [l_g]
    kite = [r_f, l_g, d_t]
    kite = tuple(kite)
    #print(kite)
    m = mode([r_f, l_g, d_t])
    #print(m)
    #print(list(m.mode[0]))
    return list(m.mode[0])
    #return vote
    #print(max(set(kite), key = kite.count))
    # Takes vote and print max. probalblity  
#def confidence_range(features):
    #arr = []
    # arr2 = []
    # arr3 = []
    # rf = get_probab_rf(features)
    # lg = get_probab_lg(features)
    # dt = get_probab_dt(features)
    # dct = {'key1': rf, 'key2': lg,'key3': dt}

    # print([min(i) for i in zip(*dct.values())])
    # print([max(i) for i in zip(*dct.values())])

    #print(arr2,arr3)
    #print(v)
    #return [arr2,arr3]

get_score(features)
get_score_lg(features)
get_score_dt(features)
display_values(features)
# # ist = [get_score(),get_score_lg(), get_score_dt()]
max_no_in_list(features)
#confidence_range(features)