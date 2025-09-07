import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('F:\Personal\Projects\Student Performance Analyzer\Data\student-scores.csv')

data = data.drop(['email', 'part_time_job', 'absence_days', 'career_aspiration'], axis=1, inplace=False)

# print(data)

stats = data.describe().to_dict()

total_stu = data['id'].count()

math_avg = data['math_score'].mean()
history_avg = data['history_score'].mean()
physics_avg = data['physics_score'].mean()
chemistry_avg = data['chemistry_score'].mean()
biology_avg = data['biology_score'].mean()
english_avg = data['english_score'].mean()
geography_avg = data['geography_score'].mean()

total_avg = round((math_avg + history_avg + physics_avg + chemistry_avg + biology_avg + english_avg + geography_avg)/7,2)

data["full_name"] = (data["first_name"].str.strip() + " " + data["last_name"].str.strip()).str.lower()

data['score'] = ((data['math_score'] + data['history_score'] + data['physics_score'] + data['chemistry_score'] + data['biology_score'] + data['english_score'] + data['geography_score']) / 7).round(2)

toppers = data.sort_values(by='score', ascending=False).head(3)[['first_name', 'last_name', 'score']]
