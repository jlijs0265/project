import pandas as pd
import pickle

class Select:
    #생성자
    # data : 초기 데이터
    def __init__(self, input_name):
        self.data = pd.read_csv('~/Documents/jira-repository/project/beer_data_app.csv')
        self.input_name = input_name
        with open('/home/winter/Documents/jira-repository/project/food.data', 'rb') as fp:
            self.food = pickle.load(fp)
    # data 모양
    # 이름 ... X 컬럼,... cluster...

    # 데이터 내에 일치하는 이름이 없다면...(추후개선)

    # 학습
    # 군집화 모델 불러오기
    # 군집화에 따른 분류 모델가져오기(설명위해)
    # X : 입력 데이터
    # y : 결과 데이터

    # 예측
    #

    # 일치하는 군집 찾기
    def find_cluster(self): 
        cluster_num = self.data['label'].loc[self.data['Name']==self.input_name].values[0]
        return  cluster_num

    # 군집중 가장 높은 avgrate인 맥주 이름 찾기
    def select(self, cluster_num):
        beer_name_df = self.data[['Ave Rating','Name']].loc[self.data['label']==cluster_num]
        beer_name = beer_name_df.sort_values('Ave Rating', ascending= False)['Name'].values[0:3]
        return beer_name

    #맥주의 맛 비중 상위 3개 내용 추출
    def flavor(self, beer_name):
        flavor = ['Astringency', 'Body', 'Alcohol','Bitter', 'Sweet', 'Sour', 'Salty', 'Fruits', 'Hoppy', 'Spices','Malty']
        beer_flavor_df = self.data[flavor].loc[self.data['Name']==beer_name]
        beer_flavor_df['sum'] = beer_flavor_df.sum(axis=1)
        beer_flavor = beer_flavor_df.apply(lambda x : round(x/beer_flavor_df['sum'].values,4)*100)
        flavor_df = pd.melt(beer_flavor, id_vars=['Body']).iloc[:,1:]
        flavor= flavor_df.sort_values('value',ascending=False).values[1:4]
        return flavor
    
    #Ave Rating 출력
    def Rating(self, beer_name):
        Ave_Rating = self.data['Ave Rating'].loc[self.data['Name']==beer_name].values
        return Ave_Rating

    #Pairing food 출력
    def Pairing_food(self, beer_name):
        Class_name = self.data['Class'].loc[self.data['Name']==beer_name].values[0]
        food_list = self.food[Class_name]
        return food_list