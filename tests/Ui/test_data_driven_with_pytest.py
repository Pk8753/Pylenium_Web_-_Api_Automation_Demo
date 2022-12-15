import pytest

@pytest.mark.parametrize("input_values", [
    # "cypress.io",
    "pylenium.io",
])
def test_google_search_puppies(py,input_values):
    py.visit('https://google.com')
    py.get("[name='q']").type(input_values)
    py.get("[name='btnK']").submit()
    assert py.should().contain_title(input_values)
