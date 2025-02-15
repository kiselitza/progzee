import requests
from typing import List, Dict, Optional

class Progzee:
    def __init__(
        self,
        proxies: Optional[List[str]] = None,
        config_file: Optional[str] = None,
    ):
        """
        Initialize Progzee with proxies.
        
        :param proxies: List of proxies in the format 'http://ip:port'.
        :param config_file: Path to a config file containing proxies.
        """
        self.proxies = proxies or []
        self.current_proxy_index = 0

        if config_file:
            self.load_config(config_file)

    def load_config(self, config_file: str):
        """
        Load proxies from a config file.
        
        :param config_file: Path to the config file.
        """
        try:
            with open(config_file, 'r') as file:
                self.proxies = [line.strip() for line in file if line.strip()]
        except FileNotFoundError:
            raise FileNotFoundError(f"Config file '{config_file}' not found.")

    def get_proxy_config(self) -> Optional[Dict[str, str]]:
        """
        Get the next proxy in the rotation.
        
        :return: Proxy config in the format {'http': 'http://ip:port', 'https': 'http://ip:port'}.
        """
        if not self.proxies:
            return None

        proxy = self.proxies[self.current_proxy_index]
        self.current_proxy_index = (self.current_proxy_index + 1) % len(self.proxies)
        return {"http": proxy, "https": proxy}

    def get(self, url: str, headers: Optional[Dict[str, str]] = None, retries: int = 3) -> requests.Response:
        """
        Make a GET request with proxy rotation.
        
        :param url: The URL to fetch.
        :param headers: Optional headers for the request.
        :param retries: Number of retries if the request fails.
        :return: The response object.
        """
        for _ in range(retries):
            try:
                proxy_config = self.get_proxy_config()
                response = requests.get(
                    url,
                    headers=headers,
                    proxies=proxy_config,
                    timeout=10,  # 10-second timeout
                )
                return response
            except requests.exceptions.RequestException as e:
                print(f"Request failed with proxy {proxy_config}: {e}. Retrying...")
        raise requests.exceptions.RequestException("Max retries reached.")
    
    def post(self, url: str, data: Optional[Dict] = None, headers: Optional[Dict[str, str]] = None, retries: int = 3) -> requests.Response:
        """
        Make a POST request with proxy rotation.
        
        :param url: The URL to send the POST request to.
        :param data: Optional data to send in the request body.
        :param headers: Optional headers for the request.
        :param retries: Number of retries if the request fails.
        :return: The response object.
        """
        for _ in range(retries):
            try:
                proxy_config = self.get_proxy_config()
                response = requests.post(
                    url,
                    data=data,
                    headers=headers,
                    proxies=proxy_config,
                    timeout=10,  # 10-second timeout
                )
                return response
            except requests.exceptions.RequestException as e:
                print(f"Request failed with proxy {proxy_config}: {e}. Retrying...")
        raise requests.exceptions.RequestException("Max retries reached.")

    def put(self, url: str, data: Optional[Dict] = None, headers: Optional[Dict[str, str]] = None, retries: int = 3) -> requests.Response:
        """
        Make a PUT request with proxy rotation.
        
        :param url: The URL to send the PUT request to.
        :param data: Optional data to send in the request body.
        :param headers: Optional headers for the request.
        :param retries: Number of retries if the request fails.
        :return: The response object.
        """
        for _ in range(retries):
            try:
                proxy_config = self.get_proxy_config()
                response = requests.put(
                    url,
                    data=data,
                    headers=headers,
                    proxies=proxy_config,
                    timeout=10,  # 10-second timeout
                )
                return response
            except requests.exceptions.RequestException as e:
                print(f"Request failed with proxy {proxy_config}: {e}. Retrying...")
        raise requests.exceptions.RequestException("Max retries reached.")

    def delete(self, url: str, headers: Optional[Dict[str, str]] = None, retries: int = 3) -> requests.Response:
        """
        Make a DELETE request with proxy rotation.
        
        :param url: The URL to send the DELETE request to.
        :param headers: Optional headers for the request.
        :param retries: Number of retries if the request fails.
        :return: The response object.
        """
        for _ in range(retries):
            try:
                proxy_config = self.get_proxy_config()
                response = requests.delete(
                    url,
                    headers=headers,
                    proxies=proxy_config,
                    timeout=10,  # 10-second timeout
                )
                return response
            except requests.exceptions.RequestException as e:
                print(f"Request failed with proxy {proxy_config}: {e}. Retrying...")
        raise requests.exceptions.RequestException("Max retries reached.")