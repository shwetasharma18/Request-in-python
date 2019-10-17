import requests

import json

import os

saral_url = "http://saral.navgurukul.org/api/courses"

def fetch_data():

	r = requests.get(saral_url)

	s = r.json()

	with open ("courses.json", "w") as f:
		json.dump(s, f, indent = 4, sort_keys = True)

fetch_data()


def load_data():

	with open ("courses.json", "r") as d:
		
		data = json.load(d)

	return data

load = load_data()

print load

def print_data(data):

	for i in data["availableCourses"]:
		
		print[i][0]["name"]

print_data(load)


def caching():
	 
	 if os.path.exists("Documents/Request/courses.json"):
	 	
	 	data = load_data()
	 	courses = print_data(load)

	 else:
	 	
	 	data = fetch_data()
	 	courses = print_data(load)

caching()

def fetching_id(data):
	user_input = input("enter an id :- ")
	for i in data['availableCourses']:
		if user_input == i['id']:
			return i


print fetching_id(load)
