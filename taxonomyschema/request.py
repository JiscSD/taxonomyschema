import json
import functools
import requests
from time import sleep
from requests.exceptions import ConnectionError, ConnectTimeout


def handle_requests_failures(func):
    '''
    This decorator handles request.exceptions
    '''
    @functools.wraps(func)
    def wrapper(self, *args, **kw):
        '''
        Handle RequestException
        '''
        while self.retries < self.max_retries:
            try:
                return func(self, *args, **kw)
            except (ConnectionError, ConnectTimeout) as e:
                if self.retries >= self.max_retries:
                    print('Cannot request URL:{}'.format(self.url))
                    raise e
                self.retries += 1
                sleep(self.sleep)

    return wrapper


class Requestor:

    """
    Requestor updates the service by POSTing to the API endpoint
    """

    def __init__(self, url, max_retries=3, sleep=5):
        self.url = url
        self.sleep = sleep
        self.retries = 0
        self.max_retries = max_retries

    @handle_requests_failures
    def update_service(self, data):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        res = requests.post(self.url, data=json.dumps(data), headers=headers)
        res.raise_for_status()
        return res
