def parse_parameters(query: str) -> dict:
    return {}


def parse_cookies(query: str) -> dict:
    return {}


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}

    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}

    assert parse_cookies('') == {}
    assert parse_cookies('fruit=apple') == {'fruit': 'apple'}
    
    
    assert parse_cookies('') == {}
    assert parse_cookies('feeling=happiness') == {'feeling': 'happiness'}

    assert parse_cookies('') == {}
    assert parse_cookies('animal=tiger') == {'animal': 'tiger'}

    assert parse_cookies('') == {}
    assert parse_cookies('number=4') == {'number': '4'}

    assert parse_cookies('') == {}
    assert parse_cookies('sport=tennis') == {'sport': 'tennis'}

    assert parse_cookies('') == {}
    assert parse_cookies('job=vet') == {'job': 'vet'}

    assert parse_cookies('') == {}
    assert parse_cookies('nationality=German') == {'nationality': 'German'}

    assert parse_cookies('') == {}
    assert parse_cookies('vehicle=car') == {'vehicle': 'car'}

    assert parse_cookies('') == {}
    assert parse_cookies('city=Paris') == {'city': 'Paris'}

 
