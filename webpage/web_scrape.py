from selenium import webdriver
import time
from instagram_class import *
from models import *
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

username = "mrbookieboo"


def get_tags(driver):

	tag_list = []
	
	comment_div = driver.find_element_by_css_selector("._es1du._rgrbt")
	comments = comment_div.find_elements_by_tag_name("li")

	tags = comments[0].find_element_by_tag_name("span").find_elements_by_tag_name("a")

	for tag in tags:
		try:
			tag_list.append(tag.text)

		except:
			continue

	return tag_list


def get_comments(driver):

	comments_list = []
	
	comment_div = driver.find_element_by_css_selector("._es1du._rgrbt")
	comments = comment_div.find_elements_by_tag_name("li")

	for comment in comments[1:]:
		try:
			comments_list.append(comment.find_element_by_tag_name("span").text)
		except:
			continue

	return comments_list


def get_photo(driver):
	return driver.find_element_by_tag_name("img").get_attribute("src")

def get_time(driver):
	div = driver.find_element_by_css_selector("._es1du._rgrbt")
	date = div.find_element_by_tag_name("time").get_attribute("datetime")

	return date


def get_like_number(driver):
	try:
		div = driver.find_element_by_css_selector("._es1du._rgrbt")
		like = (div.find_element_by_class_name("_tf9x3").find_element_by_tag_name("span")).text

	except:
		try:
			div = driver.find_element_by_css_selector("._iuf51._oajsw")
			like = len(div.find_elements_by_tag_name("a"))
		except:
			div = driver.find_element_by_css_selector("._tfkbw._d39wz")
			like = (div.find_element_by_class_name("_9jphp").find_element_by_tag_name("span")).text

	return like


def web_scrape():
	account_object = InstagramAccount(username=username)
	account_object.save()

	driver = webdriver.Chrome()
	driver.get("https://www.instagram.com/{}/?hl=en".format(username))
	load_button = driver.find_element_by_link_text("Load more")
	load_button.click()

	for i in range(1):
		driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
		time.sleep(2)

	images_row = driver.find_elements_by_class_name("_myci9")

	links = []
	photos = []

	for image_col in images_row:
		images = image_col.find_elements_by_tag_name("a")
		for image in images:
			links.append(image.get_attribute("href"))

	for link in links[:3]:

		driver.get(link)

		photo = get_photo(driver)
		likes = get_like_number(driver)
		if "," in likes:
			likes = likes.replace(',','')
		upload_time = get_time(driver)

		photo_object = Photo.objects.create(link=photo, likes=int(likes), time=upload_time)

		tags = get_tags(driver)

		for tag in tags:
			tag_object = Tags.objects.create(tag=tag)
			photo_object.tag.add(tag_object)

		comments = get_comments(driver)

		for comment in comments:
			comment_object = Comment.objects.create(comment=comment)
			photo_object.comments.add(comment_object)

		account_object.photo.add(photo_object)

		photo = AccountPhoto(photo, likes, comments=comments, tags=tags)
		photos.append(photo)

	account = InstagramAccount(username, photos)

	# return account

web_scrape()


