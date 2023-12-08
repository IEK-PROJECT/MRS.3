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

def search_movie_id(self, movie_title):
        search_endpoint = "/search/movie"
        url = f"{self.base_url}{search_endpoint}"

        params = {
            'api_key': self.api_key,
            'language': 'en-US',
            'query': movie_title,
            'page': 1
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            results = response.json().get('results', [])

            if results:
                # Return the ID of the first result (assuming it's the most relevant)
                return results[0]['id']
            else:
                print(f"No results found for movie title: {movie_title}")
                return None

        except requests.exceptions.RequestException as e:
            print(f"Error searching for movie ID: {e}")
            return None
