from tmdb_api_client import TMDbApiClient

class MovieRecommendation:
    def __init__(self, api_key):
        self.tmdb_client = TMDbApiClient(api_key)

    def calculate_similarity(self, movie_genres1, movie_genres2):
        intersection = set(movie_genres1).intersection(set(movie_genres2))
        union = set(movie_genres1).union(set(movie_genres2))

        if not union:
            return 0.0  # If genre information is not available, assume no similarity

        similarity_score = len(intersection) / len(union)
        return similarity_score

    def recommend_movies(self, movie_title, num_recommendations=10, similarity_threshold=0.9):
        movie_id = self.tmdb_client.search_movie_id(movie_title)
        if movie_id is not None:
            movie_genres = self.tmdb_client.get_movie_genres(movie_id)

            # Calculate similarity scores for all movies
            movie_similarities = []
            for other_movie_id, other_genres in self.tmdb_client.get_movie_genres().items():
                if other_movie_id != movie_id:  # Exclude the input movie itself
                    similarity = self.calculate_similarity(movie_genres, other_genres)
                    if similarity > similarity_threshold:
                        movie_similarities.append((other_movie_id, similarity))

            # Sort by similarity
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
