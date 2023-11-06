#!/usr/bin/env python
# coding: utf-8


import requests
url = 'http://0.0.0.0:9696/predict'


student={
    "marital_status": 2, 
    "application_mode": 6, 
    "application_order": 5, 
    "course": 12,
    "daytime/evening_attendance": 1, 
    "previous_qualification": 1,
    "mother\'s_occupation": 4, 
    "father\'s_occupation": 2, 
    "displaced": 1, 
    "debtor": 0,
    "tuition_fees_up_to_date": 1, 
    "gender": 0, 
    "scholarship_holder": 0, 
    "age": 30,
    "curricular_units_1st_sem_(credited)": 0,
    "curricular_units_1st_sem_(enrolled)": 6,
    "curricular_units_1st_sem_(evaluations)": 9,
    "curricular_units_1st_sem_(approved)": 6,
    "curricular_units_1st_sem_(grade)": 20,
    "curricular_units_2nd_sem_(credited)": 0,
    "curricular_units_2nd_sem_(enrolled)": 6,
    "curricular_units_2nd_sem_(evaluations)": 10,
    "curricular_units_2nd_sem_(approved)": 5,
    "curricular_units_2nd_sem_(grade)": 10,
    "curricular_units_2nd_sem_(without_evaluations)": 0, 
    "gdp": 1.74 
          }

headers = {'Content-Type': 'application/json'}


response = requests.post(url, json=student, headers=headers).json()
print(response)






