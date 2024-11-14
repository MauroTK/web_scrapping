import requests
from bs4 import BeautifulSoup
import pandas


def convert_rating(stars: str):
    """ Converts stars rating to numbers

    Args:
        stars (str): Number of stars to be converted

    Returns:
        full_stars (str): Rating in numbers
    """
    full_stars = stars.count("★")
    if "½" in stars:
        return f"{full_stars}.5"
    else:
        return full_stars


reviews_list = []
base_url = "https://letterboxd.com/reviews/popular/this/week/"
for page in range(1, 4):
    r = requests.get(
        f"https://letterboxd.com/reviews/popular/this/week/page/{page}")
    content = r.content
    doc = BeautifulSoup(content, "html.parser")
    reviews = doc.findAll("div", class_="film-detail-content")

    for review in reviews:
        movie_dict = {}
        movie_dict["Movie Title"] = review.find(
            "h2", class_="headline-2").find("a").getText(strip=True)

        movie_dict["Year"] = review.find(
            "h2", class_="headline-2").find("small", class_="metadata").getText(strip=True)

        movie_dict["Author"] = review.find(
            "strong", class_="name").getText(strip=True)

        movie_dict["Review Date"] = review.find(
            "span", class_="_nobr").getText(strip=True)

        if review.find("span", class_="rating"):
            rating = review.find("span", class_="rating").getText(
                strip=True)
            movie_dict["Rating"] = convert_rating(rating)
        else:
            movie_dict["Rating"] = None

        try:
            movie_dict["Text"] = review.find("div", class_="body-text").find(
                "p").getText(strip=True)
        except:
            movie_dict["Text"] = None

        movie_dict["Likes"] = review.find(
            "p", class_="like-link-target")["data-count"] if review.find(
            "p", class_="like-link-target")["data-count"] else None

        movie_dict["Comments"] = comments = review.find("a", class_="icon-comment").getText(
            strip=True) if review.find("a", class_="icon-comment") else None
        reviews_list.append(movie_dict)

df = pandas.DataFrame(reviews_list)
df.to_csv("Reviews.csv")
