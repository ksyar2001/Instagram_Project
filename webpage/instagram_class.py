class InstagramAccount(object):
	def __init__(self, username, account_photo):
		self.username = username
		# list of photo class
		self.photo = account_photo


class AccountPhoto(object):
	def __init__(self, url, likes, postnote=None, comments=[], tags=[]):
		self.link = url
		self.postnote = postnote
		self.likes = likes
		self.comments = comments
		self.tags = tags