import shutil
import gzip

def unzipfile(file, name):
	with gzip.open(file, 'r') as tar_ref:
		with open(name, 'wb') as f_out:
			shutil.copyfileobj(tar_ref, f_out)