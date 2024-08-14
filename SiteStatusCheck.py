import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict


def check_status(url: str) -> None:
    try:
        response: Response = requests.get(url)

        # Information
        status_code: int = response.status_code
        headers: CaseInsensitiveDict[str] = response.headers
        content_type: str = headers.get('Content-Type', 'Unknown')
        server: str = headers.get('Server', 'Unknown')
        response_time: float = response.elapsed.total_seconds()

        print(f'URL: {url}')
        print(f'Status Code: {status_code}')
        print(f'Content type: {content_type}')
        print(f'Server: {server}')
        print(f'Response time: {response_time}')
    except RequestException as e:
        print(f'Error: {e}')


def check_url() -> None:
    url = input('Enter the URL: ')
    check_status(url)
