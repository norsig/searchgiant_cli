__author__ = 'aurcioli'
import urllib
from urllib import parse
import urllib.request
from urllib import error

def hashfile(file, hasher, blocksize=65536):
    buf = file.read(blocksize)
    while len(buf) > 0:
        hasher.update(buf)
        buf = file.read(blocksize)
    return hasher.hexdigest()

def safefilename(f):
    f = f.replace('\\', '_')
    f = f.replace('/', '_')
    f = f.replace('..','_')
    if len(f) > 100:
        f = f[:50] + '_'
    return f

def webrequest(url, headers, http_intercept, data=None, binary=False):

    try:
        headers['user-agent'] = "searchgiant forensic cli"
        print("url=" + url + "\n" + "headers=" + str(headers) + "\n" + "data=" + str(data) + "\n")
        if not data:
            # GET
            req = urllib.request.Request(url, None, headers)
            response = urllib.request.urlopen(req)
            if binary:
                return response.read()
            return response.read().decode('utf-8')
        else:
            # POST
            req = urllib.request.Request(url, data.encode('utf-8'), headers)
            response = urllib.request.urlopen(req)
            if binary:
                return response.read()
            return response.read().decode('utf-8')

    except urllib.error.HTTPError as err:

        http_intercept(err)
        webrequest(url, headers, http_intercept, data, binary)


def joinurl(b, p):
    if not b.endswith("/"):
        return urllib.parse.urljoin(b + "/", p)
    else:
        return urllib.parse.urljoin(b, p)



