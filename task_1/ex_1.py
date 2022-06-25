from urllib.parse import urlparse


def domain_name(url):
    domen = urlparse(url)
    if domen.netloc == "":
        return domen.path.split('.')[1]
    if domen.netloc.split('.')[0] == 'www':
        return domen.netloc.split('.')[1]
    return domen.netloc.split('.')[0]


assert domain_name("http://www.google.com") == "google", print(domain_name("http://google.com"))
assert domain_name("http://google.co.jp") == "google", print(domain_name("http://google.co.jp"))
assert domain_name("www.xakep.ru") == "xakep", print(domain_name("www.xakep.ru"))
assert domain_name("https://youtube.com") == "youtube", print(domain_name("https://youtube.com"))
