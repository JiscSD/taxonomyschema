import json
import functools
import requests


def handle_requests_failures(func):
    '''
    This decorator handles request.excptions
    '''
    @functools.wraps(func)
    def wrapper(self, *args, **kw):
        '''
        Handle RequestException
        '''
        try:
            return func(self, *args, **kw)
        except requests.exceptions.RequestException as error:
            print(error)
            if self.retries >= self.max_retries:
                raise Exception('Cannot request URL:{}'.format(self.url))
            self.retries += 1

    return wrapper


class Requestor:

    """
    Requestor updates the service by POSTing to the API endpoint
    """

    def __init__(self, url, max_retries=3):
        self.url = url
        self.retries = 0
        self.max_retries = max_retries

    @handle_requests_failures
    def post(self, data):
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        res = requests.post(self.url, data=json.dumps(data), headers=headers)
        return res
