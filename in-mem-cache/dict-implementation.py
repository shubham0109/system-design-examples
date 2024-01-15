import requests

cache = dict()

def get_data_from_url(url):
    print("Getting data from url\n")

    response = requests.get(url)

    return response

def get_data(url):

    print("Inside Cache\n")
    if url not in cache:
        cache[url] = get_data_from_url(url)

    return cache[url]

get_data("https://realpython.com/sorting-algorithms-python/")
get_data("https://realpython.com/sorting-algorithms-python/")
