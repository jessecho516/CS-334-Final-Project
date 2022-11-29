# imports
import numpy as np
import pandas as pd
import json

# converting json to dataframe
def sample_business(json):
    df = pd.read_json(json, lines=True)
    restaurant = df.dropna(subset=['categories'])
    restaurant = restaurant[restaurant['categories'].str.contains("Restaurants")]
    df.to_csv('sample_restaurant.csv')
    return restaurant['business_id']

def sample_review(json, business_id):
    chunks = pd.read_json(json, lines=True, chunksize = 10000)
    reviews = []
    for chunk in chunks:
        df = pd.DataFrame(chunk)
        review = df.loc[df['business_id'].isin(business_id)]
        reviews.append(review)
    reviews = pd.DataFrame(reviews)
    reviews.to_csv('sample_review.csv')
    return reviews['user_id']
    
def sample_user(json, user_id):
    chunks = pd.read_json(json, lines=True, chunksize = 10000)
    users = []
    for chunk in chunks:
        df = pd.DataFrame(chunk)
        user = df.loc[df['user_id'].isin(user_id)]
        users.append(user)
    users.to_csv('sample_user.csv')
    
def sample_checkin(json, business_id):
    df = pd.read_json(json, lines=True)
    checkin = df.loc[df['business_id'].isin(business_id)]
    checkin.to_csv('sample_checkin.csv')

def sample_tip(json, business_id):
    df = pd.read_json(json, lines=True)
    tip = df.loc[df['business_id'].isin(business_id)]
    tip.to_csv('sample_tip.csv')



business_id = sample_business("yelp_academic_dataset_business.json")
user_id = sample_review("yelp_academic_dataset_review.json", business_id)
sample_user("yelp_academic_dataset_user.json", user_id)
sample_checkin("yelp_academic_dataset_checkin.json", business_id)
sample_tip("yelp_academic_dataset_tip.json", business_id)