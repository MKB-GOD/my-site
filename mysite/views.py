from django.http import HttpResponse
def test_page(requests):
    return HttpResponse("<h1>This is Test</h1>")
