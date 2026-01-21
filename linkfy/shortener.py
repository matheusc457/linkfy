import requests
from urllib.parse import urlparse

class URLShortener:
    def __init__(self):
        """Initialize the URL shortener"""
        self.api_url = "http://tinyurl.com/api-create.php"
    
    def validate_url(self, url):
        """
        Validates if the URL has correct format
        
        Args:
            url (str): URL to validate
            
        Returns:
            bool: True if valid, False otherwise
        """
        try:
            result = urlparse(url)
            return all([result.scheme, result.netloc])
        except:
            return False
    
    def shorten(self, url):
        """
        Shortens a URL using TinyURL API
        
        Args:
            url (str): Original URL to shorten
            
        Returns:
            str: Shortened URL or None in case of error
        """
        # Validate URL first
        if not self.validate_url(url):
            raise ValueError("Invalid URL. Make sure to include http:// or https://")
        
        try:
            # Make request to TinyURL API
            response = requests.get(
                self.api_url,
                params={'url': url},
                timeout=10
            )
            
            # Check if request was successful
            if response.status_code == 200:
                shortened_url = response.text.strip()
                
                # Validate if received a valid shortened URL
                if shortened_url and shortened_url.startswith('http'):
                    return shortened_url
                else:
                    raise Exception("Invalid API response")
            else:
                raise Exception(f"API error: Status {response.status_code}")
                
        except requests.exceptions.Timeout:
            raise Exception("Request timeout. Please try again.")
        except requests.exceptions.ConnectionError:
            raise Exception("Connection error. Check your internet connection.")
        except Exception as e:
            raise Exception(f"Error shortening URL: {str(e)}")
    
    def add_protocol(self, url):
        """
        Adds http:// if URL doesn't have a protocol
        
        Args:
            url (str): URL without protocol
            
        Returns:
            str: URL with protocol
        """
        if not url.startswith(('http://', 'https://')):
            return f'https://{url}'
        return url
