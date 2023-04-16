import pandas as pd
movies=pd.read_csv("tmdb_5000_movies.csv")
credits = pd.read_csv("tmdb_5000_credits.csv")
credits.columns=['id', 'title', 'cast', 'crew']
mv_rec=movies.merge(credits,on='id')
C= mv_rec['vote_average'].mean()
m= mv_rec['vote_count'].quantile(0.9) 
voted_movies = mv_rec.copy().loc[mv_rec['vote_count'] >= m]
def weighted_rating(x, m=m, C=C):
    v = x['vote_count']
    R = x['vote_average']
    return (v/(v+m) * R) + (m/(m+v) * C) 
voted_movies['score'] = voted_movies.apply(weighted_rating, axis=1)
weighted_movies = voted_movies.sort_values('score', ascending=False)
from sklearn.feature_extraction.text import TfidfVectorizer

tfidf = TfidfVectorizer(stop_words='english')

movies['overview'] = movies['overview'].fillna('')

tfidf_matrix = tfidf.fit_transform(movies['overview'])

from sklearn.metrics.pairwise import linear_kernel

cosine_sim = linear_kernel(tfidf_matrix)
indices = pd.Series(movies.index, index=movies['original_title']).drop_duplicates()

def get_recommendations(title, cosine_sim=cosine_sim):

    idx = indices[title]

    sim_scores = list(enumerate(cosine_sim[idx]))
        
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)

    sim_scores = sim_scores[1:11]

    movie_indices = [i[0] for i in sim_scores]

    return movies['id'].iloc[movie_indices]
import pickle
pickling_on = open("data.pickle","wb")
pickle.dump(get_recommendations,pickling_on)
pickling_on.close()