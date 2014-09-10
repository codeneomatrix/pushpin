import sys
import tnetstring
import zmq

if len(sys.argv) < 3:
	print 'usage: %s [channel] [content]' % sys.argv[0]
	sys.exit(1)

channel = sys.argv[1]
content = sys.argv[2]

ctx = zmq.Context()
sock = ctx.socket(zmq.PUSH)
sock.connect('tcp://localhost:5560')

hr = dict()
hr['body'] = content + '\n'
hs = dict()
hs['content'] = content + '\n'
ws = dict()
ws['content'] = content + '\n'
item = dict()
item['channel'] = channel
item['http-response'] = hr
item['http-stream'] = hs
item['ws-message'] = ws

sock.send(tnetstring.dumps(item))

print 'Published'
