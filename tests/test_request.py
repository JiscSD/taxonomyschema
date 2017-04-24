import pytest
from taxonomyschema.request import Requestor
from requests.exceptions import HTTPError
import responses


@pytest.mark.parametrize(('url', 'data', 'status', 'body', 'retries'), [
    ('http://example.com/', {'some': 'data'}, 201, 'OK', 3),
    ('http://example.com/', {'bad': 'data'}, 403,
        '{"error": {"code": 123, "message": "fail"}}',
        3)
])
@responses.activate
def test_post(url, data, status, body, retries):
    responses.add(responses.POST, url,
                  body=body, status=status,
                  content_type='application/json')

    r = Requestor(url)

    if status == 201:
        resp = r.update_service(data)
        # successful request
        assert len(responses.calls) == 1
        assert r.retries == 0
        assert resp.status_code == status
        assert responses.calls[0].request.url == url
        assert responses.calls[0].response.text == body

        # test retries
        r = Requestor(url + 'wont-work', max_retries=retries, sleep=0)
        resp = r.update_service(data)
        assert r.retries == retries
    # test 4xx and 5xx HTTP responses
    else:
        with pytest.raises(HTTPError):
            resp = r.update_service(data)
