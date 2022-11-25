# imports
import numpy as np
import pandas as pd
import json

# converting json to dataframe
def sample_business(json):
    df = pd.read_json(json, lines=True)
    df = df.sample(n=40000)
    print(df.head)
    df.to_csv('sample_business.csv')

def sample_checkin(json):
    df = pd.read_json(json, lines=True)
    df = df.sample(n=40000)
    print(df.head)
    df.to_csv('sample_checkin.csv')

def sample_review(json):
    df = pd.read_json(json, lines=True, nrows = 1000000)
    df = df.sample(n=40000)
    print(df.head)
    df.to_csv('sample_review.csv')

def sample_tip(json):
    df = pd.read_json(json, lines=True)
    df = df.sample(n=40000)
    print(df.head)
    df.to_csv('sample_tip.csv')

def sample_user(json):
    df = pd.read_json(json, lines=True, nrows = 1000000)
    df = df.sample(n=40000)
    print(df.head)
    df.to_csv('sample_user.csv')

sample_business("yelp_academic_dataset_business.json")
sample_checkin("yelp_academic_dataset_checkin.json")
sample_review("yelp_academic_dataset_review.json")
sample_tip("yelp_academic_dataset_tip.json")
sample_user("yelp_academic_dataset_user.json")