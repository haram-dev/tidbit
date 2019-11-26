from bs4 import BeautifulSoup
import urllib.request, urllib.parse, re
from .models import Course


def init():
    Course.objects.all().delete()
    # Course.truncate()


def get_courses():
    init()
    # print("category: web-dev, mobile-app, game-dev, data-science, security, blockchain, algorithm, general, server, math, database, automation, programming-tool, framework-library, programming-lang, sample-dev, infra, iot")
    # category = input('category: ')
    # web_url = f"https://www.inflearn.com/courses/it-programming/{category}"
    web_url = f"https://www.inflearn.com/courses/it-programming/web-dev"

    with urllib.request.urlopen(web_url) as response:
        html = str(response.read().decode('utf8'))
        fixed_html = re.sub('</pathg>','</path></svg>', html)
        soup = BeautifulSoup(fixed_html, "html.parser")
        for course in soup.find_all("div", {"class": "card course"}):
            print(f'title: {course.find("div", {"class": "course_title"}).get_text()}')
            print(f'price: {course.find("div", {"class": "price"}).get_text().strip()}')
            # print(f'category: {course.find("div", {"class": "course_cate"}).find("span").get_text().strip()}')
            # print(f'subcategory: {course.find("div", {"class": "course_skills"}).find("span").get_text().strip()}')
            # print(f'description: {course.find("p", {"class": "course_decription"}).get_text()}\n')

            title = course.find("div", {"class": "course_title"}).get_text()
            price_list = course.find("div", {"class": "price"}).get_text().strip().split()
            price = re.sub('\D', '', price_list[1] if len(price_list) > 1 else price_list[0])

            Course.objects.create(title=title, price=int(price if price is not '' else 0))

    return Course.objects.all()
