#same automation in Pylenium

def test_carlos_is_on_leadership(py):
    py.visit('https://www.paloaltonetworks.com/')
    py.get('a[id="nav_solutions"]').hover()
    py.get('a[href="/get-started"]').click()
    assert py.contains("Future-proof your security with reliable solutions, today")