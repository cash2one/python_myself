import cookielib;
import urllib2;

    # https: // www.baidu.com /
    # http: // hi.baidu.com / motionhouse

def main():

    loginUrl = "https://www.baidu.com/";
    cj = cookielib.CookieJar();
    opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj));
    urllib2.install_opener(opener);
    resp = urllib2.urlopen(loginUrl);
    for index, cookie in enumerate(cj):
        print '[', index, ']', cookie;

if __name__ == '__main__':
    main()