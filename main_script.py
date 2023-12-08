from tmdb_api_client import TMDbApiClient
from movie_similarity_comparator import MovieSimilarityComparator

def main():
    api_key = "3ef749f8c526bc42fb7720f376d78327"

    comparator = MovieSimilarityComparator(api_key)
    
    # Get user input for two movie titles
    movie1_title = input("Enter the title of the first movie: ")
    movie2_title = input("Enter the title of the second movie: ")

    # Search for movie IDs based on user-inputted titles
    movie1_id = comparator.tmdb_client.search_movie_id(movie1_title)
    movie2_id = comparator.tmdb_client.search_movie_id(movie2_title)

    if movie1_id is None or movie2_id is None:
        print("Error: Unable to find movie information.")
        return

    # Compare similarity between the two movies
    similarity_score = comparator.compare_similarity(movie1_id, movie2_id)

    # Print the results
    print(f"Similarity score between movies {movie1_title} and {movie2_title}: {similarity_score}")

if __name__ == "__main__":
    main()
