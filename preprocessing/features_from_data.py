import mat73
import pandas as pd






class GenerateInitialFeatures:#path of the original celebrity celebrity document. "NOTE" I read from local, cause it is too huge to uplaod to github
    def __init__(self, original_path ='/Users/aleksandrsimonyan/Desktop/celebrity.mat'):
        self.path = original_path
        self.data = mat73.loadmat('/Users/aleksandrsimonyan/Desktop/celebrity.mat')


    def generate_csv(self):
        name = [self.data['celebrityImageData']['name'][i][0] for i in range(len( self.data['celebrityImageData']['name']))]
        age = self.data['celebrityImageData']['age']
        dic = {'image_name': name, 'age': age}
        df = pd.DataFrame(dic)
        df.to_csv('imageName_age.csv')



if  __name__=='__main__':
    instance = GenerateInitialFeatures()
    instance.generate_csv()




