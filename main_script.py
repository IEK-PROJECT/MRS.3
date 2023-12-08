# main_script.py
from movie_recommendation import MovieRecommendation

def main():
    # Replace this with your actual TMDb API key
    api_key = "3ef749f8c526bc42fb7720f376d78327"

    # Instantiate the MovieRecommendation class
    movie_recommendation = MovieRecommendation(api_key)

    # Get user input for a movie title
    movie_title = input("Enter the title of a movie: ")

    # Recommend movies with high similarity scores
    recommended_movies = movie_recommendation.recommend_movies(movie_title, num_recommendations=10, similarity_threshold=0.9)

    # Print the recommendations
    if recommended_movies:
        print(f"\nTop 10 recommended movies based on high similarity to '{movie_title}':")
        for i, (recommended_movie_title, similarity_score) in enumerate(recommended_movies, start=1):
            print(f"{i}. {recommended_movie_title} (Similarity: {similarity_score:.4f})")
    else:
        print("Unable to provide recommendations.")

if __name__ == "__main__":
    main()
