import urllib2

def executeHttpRequest(url, agent, **extras):
    request = urllib2.Request('http://127.0.0.1:45749/' + url)
    request.add_header('User-Agent', 'TTU-' + agent)
    request.add_header('Secret-Key', '1X5oN69^#0^fCw7s#uyQTWYJ!8m9z!6Midphf90gMQYl*L5Uy!Ri5KTP6@BbZ5#Tlm37bJAI')
    for k, v in extras.items():
        request.add_header(k, v)
    try:
        return urllib2.urlopen(request).read()
    except:
        return None

print executeHttpRequest('ban', 'Game', username='dev', enddate=1428408418062, comment='asshole')