import web
import json
urls = ('/.*', 'hooks')

app = web.application(urls, globals())

class hooks:
    def POST(self):
        data = web.data()
	data = json.loads(web.data())
	print "New commit by: {}".format(data['commits'][0]['author']['name'])
	print "Time: {}".format(data['commits'][0]['timestamp'])
	print "Message: {}".format(data['commits'][0]['message'])
	print data['ref']
        return 'OK'

if __name__ == '__main__':
    app.run()
