import unittest
from unittest.mock import patch
from click.testing import CliRunner
from progzee.cli import cli
import os
import requests

class TestCLI(unittest.TestCase):
    def setUp(self):
        self.runner = CliRunner()
        self.config_file = "config.ini"

    @patch("progzee.progzee.requests.get")
    def test_fetch_with_explicit_proxies(self, mock_get):
        """Test the fetch command with explicit proxies."""
        # Mock the response from requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "Success"

        result = self.runner.invoke(
            cli,
            ["fetch", "--url", "https://example.com", "--proxies", "http://proxy1:port,http://proxy2:port"],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Success", result.output)

    @patch("progzee.progzee.requests.get")
    def test_fetch_with_config_file(self, mock_get):
        """Test the fetch command with a config file."""
        # Mock the response from requests.get
        mock_get.return_value.status_code = 200
        mock_get.return_value.text = "Success"

        # Create a config file for testing
        with open(self.config_file, "w") as f:
            f.write("[progzee]\nproxies = http://proxy1:port, http://proxy2:port")

        result = self.runner.invoke(
            cli,
            ["fetch", "--url", "https://example.com", "--config", self.config_file],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Success", result.output)

    def test_update_proxies(self):
        """Test the update-proxies command."""
        # Create a config file for testing
        with open(self.config_file, "w") as f:
            f.write("[progzee]\nproxies = http://proxy1:port, http://proxy2:port")

        result = self.runner.invoke(
            cli,
            ["update-proxies", "--config", self.config_file],
        )
        self.assertEqual(result.exit_code, 0)
        self.assertIn("Loaded 2 proxies from config.ini", result.output)

    @patch("progzee.progzee.requests.get")
    def test_fetch_with_invalid_url(self, mock_get):
        """Test the fetch command with an invalid URL."""
        # Mock the response to raise an exception
        mock_get.side_effect = requests.exceptions.RequestException("Failed")

        result = self.runner.invoke(
            cli,
            ["fetch", "--url", "invalid-url", "--proxies", "http://proxy1:port,http://proxy2:port"],
        )
        self.assertNotEqual(result.exit_code, 0)
        self.assertIn("Request failed", result.output)

    def tearDown(self):
        # Clean up the config file after each test
        if os.path.exists(self.config_file):
            os.remove(self.config_file)

if __name__ == "__main__":
    unittest.main()