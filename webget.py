import shutil
import urllib.request as urlreq
from urllib.parse import urlparse

def download(url, to=None):
	if to == None:
		file_name = urlparse(url).path.split('/')[-1]
	else:
		file_name = to + urlparse(url).path.split('/')[-1]
	with urlreq.urlopen(url) as response, open(file_name, 'wb') as out_file:
		shutil.copyfileobj(response, out_file)
	return file_name