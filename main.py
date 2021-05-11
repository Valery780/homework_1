from urllib.parse import urlsplit, parse_qs
from http.cookies import SimpleCookie


def parse_parameters(url: str) -> dict:
    query = urlsplit(url).query
    params = parse_qs(query)
    return {k: v[0] for k, v in params.items()}


def parse_cookies(query: str) -> dict:
    cookie = SimpleCookie()
    cookie.load(query)
    cookies = {}
    for key, morsel in cookie.items():
        cookies[key] = morsel.value
    return cookies


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret',
                                                                                             'color': 'purple'}

    assert parse_parameters('https://www.youtube.com/watch?v=Wx5h0EI3nqg&ab_channel=Channel') == {'v': 'Wx5h0EI3nqg',
                                                                                                  'ab_channel': 'Channel'}

    assert parse_parameters('https://freelancehunt.com/project/lab-po-komp-diskretnoy-matematike/topic=math&type=441249.html') == \
           {'topic': 'math',
                                                                                                  'type': '441249.html'}

    assert parse_parameters('www.yoursite.com?myparam1=123&myparam2=abc') == {'myparam1': '123',
                                                                              'myparam2': 'abc'}

    # Tests for function "parse_cookies"
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
    assert parse_cookies('name=Dima; surname=Smirnov;') == {'name': 'Dima', 'surname': 'Smirnov'}
    assert parse_cookies('CUSTOMER=DIMA; PART_NUMBER=ROCKET_LAUNCHER_0001; SHIPPING=FEDEX') \
           == {'CUSTOMER': 'DIMA', 'PART_NUMBER': 'ROCKET_LAUNCHER_0001', 'SHIPPING': 'FEDEX'}
    assert parse_cookies('usernamefield=username, passwordfield=password, otherfield=othervalue') \
           == {'usernamefield': 'username,', 'passwordfield': 'password,', 'otherfield': 'othervalue'}
    assert parse_cookies('baz=42; Domain=example.com; Expires=Fri, 12-Jan-2017 13:55:08 GMT; Path=/, dir=75') \
           == {'baz': '42', 'dir': '75'}
    assert parse_cookies('DOMAIN=domain_name;') == {'DOMAIN': 'domain_name'}
    assert parse_cookies('tasty_cookie=happiness;') == {'tasty_cookie': 'happiness'}

 
