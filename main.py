# coding=utf-8
from lj import lj as dlj

from codecs import decode
def write_file(c,s,d,i):
    fi = open("input_%s.md" % i, 'w', encoding='utf-8')
    fi.write("title:%s\ndate:%s\n\n\n%s" % (c, s, d))
    fi.close()
    i += 1


def make_list(r):
    i=0
    for key in r['events']:
        try:
            d = (key["event"].data.decode())
        except AttributeError:
            d='no data'
        try:
            c=(key["subject"].data.decode())
        except KeyError:
            c='(no subject)'
        s=key['logtime']
        i+=1
        write_file(c,s,d,i)
def ljj():
    lj = dlj.LJServer("lj-post-grabber", "example.com")
    lj.login("login", "pass")
    r=lj.getevents_lastn(50,'2019-11-20 21:54:00')
    make_list(r)
if __name__ == '__main__':
    ljj()
