from datetime import datetime
from app import db
import os

class Post(db.Model):
	id 		  = db.Column(db.Integer, primary_key=True)
	title 	  = db.Column(db.String(31), index=True, default="title")
	content   = db.Column(db.String(255))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	likes 	  = db.Column(db.Integer, default=0)
	dislikes  = db.Column(db.Integer, default=0)
	img_path  = db.Column(db.String(100))

	def __repr__(self):
		return "<Post: title={}, id={}>".format(self.title, self.id)

	def should_hide(self, hide_at=-10):
		return self.likes-self.dislikes>=hide_at

	def image_exists(self):
		return os.path.isfile(self.image_loaction)

class Comment(db.Model):
	id        = db.Column(db.Integer, primary_key=True)
	title     = db.Column(db.String(31), index=True, default="title")
	content   = db.Column(db.String(127))
	timestamp = db.Column(db.DateTime, index=True, default=datetime.utcnow)
	likes 	  = db.Column(db.Integer, default=0)
	dislikes  = db.Column(db.Integer, default=0)
	img_path  = db.Column(db.String(100))
	post_id   = db.Column(db.Integer, db.ForeignKey("post.id"))

	def __repr__(self):
		return "<Comment: title={}, id={}, post={}>".format(self.title, self.id, self.post_id)

	def should_hide(self, hide_at=-10):
		return self.likes-self.dislikes>=hide_at

	def image_exists(self):
		return os.path.isfile(self.image_location)

if __name__=='__main__':
	print(Comment)