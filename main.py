import pandas as pd
import numpy as np
import difflib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
movies_data = pd.read_csv('movies.csv')
movies_data.shape
selected_features = ['genres', 'keywords', 'popularity', 'tagline', 'cast', 'director']
for feature in selected_features:
  movies_data[feature] = movies_data[feature].fillna('')
combined_features = movies_data['genres']+''+movies_data['keywords']+''+movies_data['tagline']+''+movies_data['cast']+''+movies_data['director']
vectorizer = TfidfVectorizer()
feature_vectors = vectorizer.fit_transform(combined_features)
similarity = cosine_similarity(feature_vectors)
list_of_all_titles = movies_data['title'].tolist()
# print(list_of_all_titles)Movies_names=[]
class Movies:
    title=""
    path=""
    overview=""
Save_Movies=[]
import json
import requests
def get_Movies(movie):
  try:
    movie_name = movie
    list_of_all_titles = movies_data['title'].tolist()
    find_close_match = difflib.get_close_matches(movie_name, list_of_all_titles)
    close_match= find_close_match[0]
    index_of_the_movie = movies_data[movies_data.title == close_match]['index'].values[0]
    similarity_score = list(enumerate(similarity[index_of_the_movie]))
    sorted_simlar_movies = sorted(similarity_score, key = lambda x:x[1], reverse=True)
    print("Movies Suggested Movies for you: ")
    i = 1
    for movie in sorted_simlar_movies:
      index = movie[0]
      title_from_index = movies_data[movies_data.index==index]['title'].values[0]
      Movies_names.append(title_from_index)
      if (i<10):
        #print(i, '.', title_from_index)
        i+=1
  except:
    print("Please Enter a Correct Input: ")

  for i in Movies_names[:10]:
      title_from_index = i
      print(title_from_index)
      data = requests.get("https://api.themoviedb.org/3/search/movie?api_key=41390bd35466b5e7721cfae486de6748&language=en-US&page=1&query=" + title_from_index)
      movie_data = json.loads(data.text)
      mov=Movies()
      mov.path='https://image.tmdb.org/t/p/original'+movie_data["results"][0]["poster_path"]
      mov.title=movie_data["results"][0]["original_title"]
      mov.overview=movie_data["results"][0]["overview"]
      Save_Movies.append(mov)
      '''imagelink = "https://image.tmdb.org/t/p/original" + movie_data["results"][0]["poster_path"]
      res = requests.get(imagelink)
      with open(f".\images\{i}.jpg", "wb") as f:
          f.write(res.content)'''
