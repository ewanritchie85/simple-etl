import pytest, requests
from utils.extract_utils import get_dict_from_api

@pytest.fixture
def test_url():
    return "https://jsonplaceholder.typicode.com/todos/1"

class TestGetFromApi:
    
    def test_function_returns_dict(TestGetFromApi, test_url):
        response = get_dict_from_api(test_url)
        assert isinstance(response, dict)
        assert response == {
                            "userId": 1,
                            "id": 1,
                            "title": "delectus aut autem",
                            "completed": False
                            }
        
        
    def test_function_raises_request_exception(TestGetFromApi, test_url):
        test_url = 'https://jsonplaceholder.typtricode.com/todos/1'
        with pytest.raises(requests.exceptions.ConnectionError):
            get_dict_from_api(test_url)