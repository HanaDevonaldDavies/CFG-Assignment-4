import requests

BASE_URL = 'http://localhost:3306'

def test_get_books():
    response = requests.get(f'{BASE_URL}/books')
    print('Books:', response.json())

def test_add_book():
    new_book = {
        'title': 'Pride and Prejudice',
        'author': 'Jane Austin',
        'price': 7.99,
        'published_date': '28-01-1813'
    }
    response = requests.post(f'{BASE_URL}/books', json=new_book)
    print('Add Book:', response.json())

def test_get_authors():
    response = requests.get(f'{BASE_URL}/authors')
    print('Authors:', response.json())

if __name__ == '__main__':
    test_get_books()
    test_add_book()
    test_get_authors()