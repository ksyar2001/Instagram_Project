from django.test import TestCase
from web_scrape import *
from watson.WatsonAPI import *
from models import *

class TestWatson(TestCase):

	def test_watson(self):
		web_scrape()
		# comments = ""

		print InstagramAccount.objects.all()

		for photo in InstagramAccount.objects.get(username="mrbookieboo").photo.all():
			print photo.comments.all().count()

		for photo in InstagramAccount.objects.get(username="mrbookieboo").photo.all():
			print photo.pk
			print "=============================="
			print photo.tag.all().count()


		# for photo in account.photo:
		# 	for comment in photo.comments:
		# 		comments += comment

		# print comments

		# print json.dumps(WatsonAPI().getToneAnalysis(comments), indent=2)




