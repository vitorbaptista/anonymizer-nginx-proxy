import os
import subprocess
import pytest
import requests
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry


@pytest.fixture(scope='session')
def server():
    current_path = os.path.dirname(os.path.realpath(__file__))
    test_compose_path = os.path.join(current_path, 'docker-compose.yml')
    command = [
        'docker-compose',
        '--file',
        test_compose_path,
        'up',
        '--build',
    ]

    with subprocess.Popen(command) as compose:
        yield compose
        compose.terminate()


@pytest.fixture
def server_url(server):
    url = 'http://localhost:9000'
    session = _requests_retry(retries=5, backoff_factor=0.5)
    session.get(url).raise_for_status()
    return url


def _requests_retry(
    retries=3,
    backoff_factor=0.3,
    status_forcelist=(500, 502, 504),
    session=None,
):
    session = session or requests.Session()
    retry = Retry(
        total=retries,
        read=retries,
        connect=retries,
        backoff_factor=backoff_factor,
        status_forcelist=status_forcelist,
    )
    adapter = HTTPAdapter(max_retries=retry)
    session.mount('http://', adapter)
    session.mount('https://', adapter)
    return session
