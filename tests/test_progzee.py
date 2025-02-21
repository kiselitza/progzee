import unittest
from unittest.mock import patch
from progzee.progzee import Progzee
import requests
import os

class TestProgzee(unittest.TestCase):
    def setUp(self):
        # Set up a list of proxies for testing
        self.proxies = ["http://proxy1:port", "http://proxy2:port"]
        self.config_file = "config.ini"

    def test_initialization_with_explicit_proxies(self):
        """Test initialization with explicit proxies."""
        pz = Progzee(proxies=self.proxies)
        self.assertEqual(pz.proxies, self.proxies)

    def test_initialization_with_config_file(self):
        """Test initialization with a config file."""
        # Mock the config file content
        config_content = "[progzee]\nproxies = http://proxy1:port, http://proxy2:port"
        with open(self.config_file, "w") as f:
            f.write(config_content)

        pz = Progzee(config_file=self.config_file)
        self.assertEqual(pz.proxies, self.proxies)

    @patch("requests.get")
    def test_get_request_with_proxy_rotation(self, mock_get):
        """Test GET request with proxy rotation."""
        # Mock the response from requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "Success"

        pz = Progzee(proxies=self.proxies)
        response = pz.get("https://example.com")

        # Check that the request was made with the first proxy
        mock_get.assert_called_with(
            "https://example.com",
            headers=None,
            proxies={"http": self.proxies[0], "https": self.proxies[0]},
            timeout=10,
        )
        self.assertEqual(response.text, "Success")

    @patch("requests.get")
    def test_get_request_retries_on_failure(self, mock_get):
        """Test that the request retries with the next proxy on failure."""
        # Mock the first request to fail and the second to succeed
        mock_get.side_effect = [
            requests.exceptions.RequestException("Failed"),
            unittest.mock.Mock(status_code=200, text="Success"),
        ]

        pz = Progzee(proxies=self.proxies)
        response = pz.get("https://example.com")

        # Check that the request was retried with the second proxy
        self.assertEqual(mock_get.call_count, 2)
        self.assertEqual(response.text, "Success")

    def test_load_config_with_invalid_file(self):
        """Test loading config from a non-existent file."""
        with self.assertRaises(FileNotFoundError):
            Progzee(config_file="nonexistent.ini")

    def test_load_config_with_missing_section(self):
        """Test loading config with a missing '[progzee]' section."""
        # Create a config file without the '[progzee]' section
        with open(self.config_file, "w") as f:
            f.write("[other_section]\nproxies = http://proxy1:port")

        with self.assertRaises(ValueError):
            Progzee(config_file=self.config_file)

    def tearDown(self):
        # Clean up the config file after each test
        if os.path.exists(self.config_file):
            os.remove(self.config_file)

if __name__ == "__main__":
    unittest.main()