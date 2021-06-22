from web import FeatureCreation


class Classifier:

    def __init__(self,name_comp):
        self.name_comp = name_comp
    
    def geturl():
        ''' get url for company name and assign it to self.url
        '''

    def get_feature(self):
        feature_obj = FeatureCreation(self.url,self.name_comp)
        features_extract = feature_obj.feature_extract() # get values for 1 url
        self.feature_extract = features_extract

    def classification_model():
        prob_score1 = #call random forest
        #prob_Score1 = #logistic regression
        #prob_score2 = #decision_tree

        # create a list which stores RV [ 1,0,1]
        #maximum number of 1 > maaximum of 0 
         # rv= 1
         #esle
         #  rv =0
        
        #take votes

    def classify_start(self) :
        self.geturl()
        self.get_feature()
        self. classifier()


#if name == "__main__":
name_comp = <str> #argument
classify_obj = Classifier(name_comp) # name of the company
classify_obj.classify_start()
