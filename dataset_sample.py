# imports
import numpy as np
import pandas as pd
import json

# converting json to dataframe
def sample_business(json):
    df = pd.read_json(json, lines=True)
    restaurant = df.dropna(subset=['categories'])
    restaurant = restaurant[restaurant['categories'].str.contains("Restaurants")]
    restaurant = restaurant.sample(n=40000)
    restaurant.to_csv('sample_restaurant.csv')
    return restaurant['business_id']

def sample_review(json, business_id):
    chunks = pd.read_json(json, lines=True, chunksize = 10000)
    reviews = pd.DataFrame()
    for chunk in chunks:
        df = pd.DataFrame(chunk)
        review = pd.merge(df, business_id, left_on='business_id', right_on='business_id')
        # print(review)
        reviews = pd.concat([reviews, review], ignore_index=True)
    reviews = reviews.sample(n=40000)
    reviews.to_csv('sample_review.csv')
    return reviews['user_id']
    
def sample_user(json, user_id):
    chunks = pd.read_json(json, lines=True, chunksize = 10000)
    users = pd.DataFrame()
    for chunk in chunks:
        df = pd.DataFrame(chunk)
        user = pd.merge(df, user_id, left_on='user_id', right_on='user_id')
        users = pd.concat([users, user], ignore_index=True)
    users = users.sample(n=40000)
    users.to_csv('sample_user.csv')
    
def sample_checkin(json, business_id):
    df = pd.read_json(json, lines=True)
    checkin = pd.merge(df, business_id, left_on='business_id', right_on='business_id')
    checkin.to_csv('sample_checkin.csv')

def sample_tip(json, business_id):
    df = pd.read_json(json, lines=True)
    tip = pd.merge(df, business_id, left_on='business_id', right_on='business_id')
    tip.to_csv('sample_tip.csv')



business_id = sample_business("yelp_academic_dataset_business.json")
print("finished business csv")
user_id = sample_review("yelp_academic_dataset_review.json", business_id)
print("finished review csv")
sample_user("yelp_academic_dataset_user.json", user_id)
print("finished user csv")
sample_checkin("yelp_academic_dataset_checkin.json", business_id)
print("finished checkin csv")
sample_tip("yelp_academic_dataset_tip.json", business_id)
print("finished tip csv")
