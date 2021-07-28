from featurecreation import FeatureCreation
 
if __name__ == "__main__":
    arr1 = []
    arr2 = []
    arr3 = []
    fc_obj = FeatureCreation()
    url = fc_obj.getURLForQuery()

    for i in url:
        try:
            fc_obj.crawl(i)
            arr1.append(len(external_urls))
            arr2.append(len(internal_urls))
            arr3.append(len(external_urls) + len(internal_urls))
            internal_urls = set()
            external_urls = set()
        except:
            #array.append([0,0,0])
            arr1.append(0)
            arr2.append(0)
            arr3.append(0)
            internal_urls = set()
            external_urls = set()
    # arr1 = list(filter('[]', arr1))
    # arr2 = list(filter('[]', arr2))
    # arr3 = list(filter([], arr3))
    #print(arr1,arr2)
    self.external = arr1
    self.internal = arr2
    return self.external,self.internal