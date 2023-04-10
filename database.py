# -*- coding: utf-8 -*-
"""
Created on Sun Apr  9 13:22:23 2023

@author: Hp
"""
import os
from deta import Deta
from dotenv import load_dotenv

load_dotenv(".env")
DETA_KEY="d0cq2iaqzhb_SxEW2sg373eRi7rnbZeqTj2YV18tDY4e"

#Initialize with a project key
deta = Deta(DETA_KEY)

#This is how we create/connect to a database
db=deta.Base("monthly_reports")

def insert_period(period,incomes,expenses,comment):
    """Returns the report on a successful creation, otherwise raises an error"""
    return db.put({"key":period,"incomes":incomes,"expenses":expenses,"comment":comment})

def fetch_all_periods():
    """Returns a dict of all the periods"""
    res=db.fetch()
    return res.items

def get_period(period):
    """If not found, the function will return None"""
    return db.get(period)