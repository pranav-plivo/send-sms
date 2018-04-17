# -*- coding: utf-8 -*-
from flask import Flask, request, make_response, Response, Flask, flash, redirect, render_template, request, session, abort
import plivo
import json
import jsonify

app = Flask(__name__, static_url_path='')


@app.route('/send_sms/')# methods=['POST'])
def outbound_sms():

	from_number= request.form.get("123456789")
	to_number= request.form.get("918827932461")
	content= request.form.get("text")

	client = plivo.RestClient('MAZWU5OWM4YTK3ZJAXMG', 'NmE5M2I4NDFkYWUxZjNjOTU0NjM4ZjNlNWZhMzQ2')
	try:
		resp = client.messages.create(
			src=from_number, # Sender's phone number with country code
			dst=to_number, # Receiver's phone Number with country code
			text=content,
		)
		# print(response)
		return str(resp)
	except plivo.exceptions.PlivoRestError as e:
		print(e)

@app.route('/send_message/', methods=['GET'])    
def outbound_sms_template():
	return render_template('test_sms_flask.html')

if __name__ == "__main__":
    app.run(debug=True)
