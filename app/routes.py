from app import app, db
from json import dumps as json_encode #dumps isn't descriptive enough
from flask import request
from app.models import Post, Comment

def method_not_allowed( ):
	return "<h1>This method is not allowed</h1>"


@app.route( "/api/hello" )
def api_hello( ):
	a = {
		"message":"Hello world"
	}

	return json_encode( a )

@app.route( "/api/make/post", methods=["POST"] )
def api_make_post( ):
	print(request.form.get("content"))
	data = request.values.to_dict( )
	JSON = {
		"status":"",
		"message":""
	}
	#Check that they have submitted the correct data
	try:
		title = data["title"]
		content = data["content"]
	except KeyError:
		return json_encode({"error":"Incorrect POST data submitted"})

	post = Post(title=data['title'], content=data["content"])
	db.session.add(post)
	db.session.commit( )
	
	return json_encode({"message":"Post created successfully"})

@app.route( "/api/get/posts" )
def get_posts( ):
