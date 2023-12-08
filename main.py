from tmdb_api_client import TMDbApiClient

def main():
    api_key = "3ef749f8c526bc42fb7720f376d78327"
    tmdb_client = TMDbApiClient(api_key)

    # Test the discover_movies endpoint
    movies_data = tmdb_client.discover_movies()
    
    if movies_data:
        print("Top movies:")
        for movie in movies_data.get('results', []):
            print(f"- {movie.get('title')} ({movie.get('release_date')})")
    else:
        print("Failed to retrieve movie data.")

if __name__ == "__main__":
    main()
