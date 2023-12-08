import requests

class TMDbApiClient:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.themoviedb.org/3"

    def discover_movies(self, sort_by='popularity.desc', page=1):
        endpoint = "/discover/movie"
        url = f"{self.base_url}{endpoint}"

        params = {
            'api_key': self.api_key,
            'language': 'en-US',
            'sort_by': sort_by,
            'include_adult': False,
            'include_video': False,
            'page': page
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an error for bad responses
            return response.json()
        except requests.exceptions.RequestException as e:
            print(f"Error making API request: {e}")
            return None

# Usage example
if __name__ == "__main__":
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
