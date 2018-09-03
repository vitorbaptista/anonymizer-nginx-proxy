import requests
import pytest


class TestPrivacy(object):
    @pytest.mark.parametrize('header', (
        'User-Agent',
        'Accept-Language',
        'Referer',
        'X-Real-IP',
        'X-Forwarded-For',
        'From',
    ))
    def test_removes_header(self, server_url, header):
        res = requests.get(
            server_url + '/get',
            headers={
                header: 'should be removed',
            }
        )
        data = res.json()
        assert header not in data['headers']
