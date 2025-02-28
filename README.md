# progzee
Progzee is a Python library for simplifying IP proxy usage in HTTP requests, with proxy rotation. It simplifies handling proxies for web scraping, API interaction, and more.

<div align="center">

![PyPI - Downloads](https://img.shields.io/pypi/dm/progzee?style=for-the-badge&logo=pypi&logoColor=yellow&color=blue)
[![GitHub Repo stars](https://img.shields.io/github/stars/kiselitza/progzee?style=for-the-badge&logo=github&logoColor=EFBF04&color=EFBF04)](https://star-history.com/#kiselitza/progzee)
[![License](https://img.shields.io/github/license/kiselitza/progzee?style=for-the-badge&logo=gitbook&link=https%3A%2F%2Fgithub.com%kiselitza%2Fprogzee%2Fblob%2Fmain%2FLICENSE)](/LICENSE)
</div>

**Key Features**:
- IP Proxy rotation.
- Config file support for easy setup.
- CLI support for quick tasks.

## Installation
Install Progzee using pip:

```bash
pip install progzee
```

Usage with proxies passed in constructor:
```python
from progzee import Progzee

# Initialize with proxies explicitly
proxies = ["http://proxy1:port", "http://proxy2:port"]
pz = Progzee(proxies=proxies)

# Make a request
response = pz.get("https://example.com")
print(response.text)
```
Usage with `config.ini`:
```python
from progzee import Progzee

# Initialize with config file
pz = Progzee(config_file="config.ini")
```

CLI Usage:
```java
# Update proxies from a config file
progzee update-proxies --config "config.ini"

# Fetch data from a URL
progzee fetch --url "https://example.com"
```

An example of a `config.ini` file:
```
[progzee]
proxies = http://proxy1:port, http://proxy2:port
timeout_min = 5
timeout_max = 15
```

## Error handling
Progzee automatically retries failed requests with the next proxy in the rotation.

## Validate your proxies
Make sure that you're using valid proxies that you own, or from trusted vendors. One of the trusted vendors you can use is [ProxyScrape](https://proxyscrape.com/?ref=yzczyjq).

## License
Progzee is licensed under the Apache License 2.0. See [LICENSE](LICENSE) for more details.

## ⚠️ DISCLAIMER ⚠️
This tool is intended for ethical use cases only, including educational purposes, testing, and legitimate API interactions.

The tool is provided as-is, without any warranty. The author is not responsible for any damages or legal issues arising from its use.

Users are responsible for ensuring their usage complies with the Terms of Service of the APIs they interact with. Misuse of this tool, including but not limited to scraping without permission, bypassing rate limits, or engaging in malicious activities, is strictly prohibited.

By using this tool, you agree to use it responsibly and in compliance with all applicable laws and regulations.

## Thanks for the support!
Support this project with the GitHub Star.

Support the project author with a [pizza slice](https://buymeacoffee.com/kiselitza).
