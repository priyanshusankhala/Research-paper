from featurextract import FeatureCreation
 
if __name__ == "__main__":
    peag = FeatureCreation()
    features  = peag.feature_extract()
    displayurl = peag.get_url()