from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

data = {
    'title': ['Inception', 'The Matrix', 'Interstellar', 'The Dark Knight', 'Avengers', 'Titanic'],
    'genre': ['Sci-Fi', 'Sci-Fi', 'Sci-Fi', 'Action', 'Action', 'Romance']
}

df = pd.DataFrame(data)

vectorizer = TfidfVectorizer()
genre_matrix = vectorizer.fit_transform(df['genre'])

cosine_sim = cosine_similarity(genre_matrix, genre_matrix)

def recommend(movie_title):
    if movie_title not in df['title'].values:
        return "Movie not found in database!"
    
    idx = df[df['title'] == movie_title].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    
    recommended = []
    for i in sim_scores[1:4]:  
        recommended.append(df.iloc[i[0]]['title'])
    return recommended

print("Recommendations for Inception:")
print(recommend("Inception"))

print("\nRecommendations for Titanic:")
print(recommend("Titanic"))
