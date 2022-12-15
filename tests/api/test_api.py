def test_api_fixture_get(api):
    response = api.get("https://reqres.in/api/users?page=2")
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200


def test_api_fixture_post(api):
    payload = {}
    payload["email"] = "eve.holt@reqres.in"
    payload["password"] = "pistol"
    url = "https://reqres.in/api/register"
    response = api.post(url=url, json=payload)
    print(response.json())
    print(response.status_code)
    assert response.status_code == 200



