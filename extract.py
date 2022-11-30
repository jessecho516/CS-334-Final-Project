import pandas as pd
from sklearn.model_selection import train_test_split


def encode(df, feat):
    dummies = pd.get_dummies(df[feat])
    res = pd.concat([df, dummies], axis=1)
    res = res.drop([feat], axis=1)
    return res

def main():
    path = 'restaurant_businesses.csv'
    restaurants = pd.read_csv(path)
    #drop attributes that are not useful
    restaurants.drop(columns=['Unnamed: 0', 'business_id', 'name', 'attributes', 'categories', 'hours', 'address'], inplace=True)
    restaurants.dropna(inplace=True)

    #creating labels from star rating reviews
    restaurants['starsBin'] = restaurants['stars'].apply(lambda x: 1 if x>=4 else 0)

    #keep cities that occur over 1k times
    #print(restaurants['latitude'].value_counts())
    # cities = restaurants['city'].value_counts()
    # cities = cities.loc[:,] > 1000
    # cities = cities[cities]

    # drop states that only have one restaurant rating
    #one hot encoding state
    # restaurants = encode(restaurants, 'state')
    # restaurants.drop(columns=['NC', 'CO', 'HI', 'MT', 'XMS', 'AB'], inplace=True)

    restaurants.drop(columns=['postal_code', 'latitude', 'longitude', 'state'], inplace=True)

    #create train test split
    train, test = train_test_split(restaurants, test_size = .3)

    xTrain = train.drop(['stars', 'starsBin'], axis=1)
    yTrain = train[['stars', 'starsBin']]

    xTest = test.drop(['stars', 'starsBin'], axis=1)
    yTest = test[['stars', 'starsBin']]

    #create csv
    xTrain.to_csv('xTrain.csv', index=False)
    yTrain.to_csv('yTrain.csv', index=False)

    xTest.to_csv('xTest.csv', index=False)
    yTest.to_csv('yTest.csv', index=False)

    #names = restaurants['name'].str.split(' ', expand=False)
    #print(restaurants)

if __name__ == "__main__":
    main()