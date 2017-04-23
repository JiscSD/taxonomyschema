# import pytest
# # import json
# from taxonomyschema.request import Requestor


# # @pytest.fixture(params=[(True, 0), (False, 10000)])
# @pytest.fixture(params=[(True, 0)])
# def recurse(request):
#     return request.param


# @pytest.mark.parametrize(('data', 'retries'), [
#     ([{'some': 'data'}], 0),
# ])
# def test_run(path, links_all, links_unvisited, httpbin, recurse):
#     r = Requestor(httpbin.url)
#     r.update_service(url=path)
