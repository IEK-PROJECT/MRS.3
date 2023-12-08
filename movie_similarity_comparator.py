# movie_similarity_comparator.py
from tmdb_api_client import TMDbApiClient

class MovieSimilarityComparator:
    def __init__(self, api_key):
        self.tmdb_client = TMDbApiClient(api_key)
        self.movies_data = self.tmdb_client.discover_movies()
        self.genre_id_to_name = self.tmdb_client.get_movie_genres()
        self.movie_genres = self._extract_genres()

    def _extract_genres(self):
        genres = {}
        for movie in self.movies_data.get('results', []):
            movie_id = movie.get('id')
            genre_ids = movie.get('genre_ids', [])
            movie_genres = [self.genre_id_to_name.get(genre_id, "") for genre_id in genre_ids]
            genres[movie_id] = movie_genres
        return genres

    def _get_movie_genres(self, movie_id):
        return self.movie_genres.get(movie_id, [])

    def compare_similarity(self, movie1_title, movie2_title):
        # Search for movie IDs based on user-inputted titles
        movie1_id = self.tmdb_client.search_movie_id(movie1_title)
        movie2_id = self.tmdb_client.search_movie_id(movie2_title)

        if movie1_id is not None and movie2_id is not None:
            # Calculate Jaccard similarity
            genres_movie1 = self._get_movie_genres(movie1_id)
            genres_movie2 = self._get_movie_genres(movie2_id)

            intersection = set(genres_movie1).intersection(set(genres_movie2))
            union = set(genres_movie1).union(set(genres_movie2))

            if not union:
                return 0.0  # If genre information is not available, assume no similarity

            similarity_score = len(intersection) / len(union)
            return similarity_score
        else:
            print("Unable to compare similarity. Check the movie titles.")
            return None

    def recommend_movies(self, movie_title, num_recommendations=10):
        movie_id = self.tmdb_client.search_movie_id(movie_title)
        if movie_id is not None:
            movie_genres = self._get_movie_genres(movie_id)

            # Calculate similarity scores for all movies and sort by similarity
            movie_similarities = []
            for other_movie_id, other_genres in self.movie_genres.items():
                if other_movie_id != movie_id:  # Exclude the input movie itself
                    similarity = len(set(movie_genres).intersection(set(other_genres))) / len(set(movie_genres).union(set(other_genres)))
                    movie_similarities.append((other_movie_id, similarity))

            movie_similarities.sort(key=lambda x: x[1], reverse=True)

            # Get the top recommended movies with similarity scores
            recommended_movies = []
            for i in range(min(num_recommendations, len(movie_similarities))):
                recommended_movie_id, similarity_score = movie_similarities[i]
                recommended_movie_title = self.tmdb_client.get_movie_title(recommended_movie_id)
                recommended_movies.append((recommended_movie_title, similarity_score))

            return recommended_movies
        else:
            print("Unable to recommend movies. Check the movie title.")
            return None
