from django.test import TestCase, Client
from django.urls import reverse
from .models import Comic
# Create your tests here.


def buildComicObject(new_title, new_issue, new_graded, new_key, new_publisher):
    return Comic.objects.create(
        title=new_title,issue=new_issue,graded=new_graded,key=new_key,publisher=new_publisher)


class TestComicsViews(TestCase):
    
    def testNumberOfComics(self):
        print("testNumberOfComics: Check Current Number of Comics")
        comics = Comic.objects.all()
        numComics = len(comics)
        self.assertEqual(numComics,0)

    def testAddingComic(self):
        print("testAddingComic: test adding a new comic to the database")
        newComic = buildComicObject("Uncanny X-Men","94","Not Graded","First Claremont","Marvel")
        comics = Comic.objects.all()
        numComics = len(comics)
        self.assertEqual(numComics, 1)
        url = reverse('comics:comicDetail', args=(newComic.id,))
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
    
    def testAddingComicThroughView(self):
        print("testAddingComicThroughView: test adding a new comic using comics/addComic")
