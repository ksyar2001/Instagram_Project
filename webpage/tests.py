from django.test import TestCase
from web_scrape import *
from watson.WatsonAPI import *

class TestWatson(TestCase):

	def test_watson(self):
		account = web_scrape()
		comments = ""

		for photo in account.photo:
			for comment in photo.comments:
				comments += comment

		print comments

		print json.dumps(WatsonAPI().getToneAnalysis(comments), indent=2)




