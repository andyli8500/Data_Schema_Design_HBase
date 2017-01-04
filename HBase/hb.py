import os, sys
import happybase as hb


if len(sys.argv) < 3:
    print "Usage: python2 run.py <query action> <input>"
    sys.exit(1)

action = sys.argv[1]
input_ = sys.argv[2]

conn = hb.Connection('soit-hdp-pro-15.ucc.usyd.edu.au',9090)

tb = conn.table('jili2506:index')


if action == 'q1':
    start = "u{}/f00".format(input_)
    end = "u{}/f99".format(input_)

    result = tb.scan(row_start=start, row_stop=end, columns=['c:url', 'c:pictureurl'])
    
    for i, (key, data) in enumerate(result):
        artist = key.split('/')[-1][1:]
        print i, artist, data

elif action == 'q2':
    start = "a{}/r00".format(input_)
    end = "a{}/r99".format(input_)

    d = {}

    result = tb.scan(row_start=start, row_stop=end)

    for key, data in result:
        tag = key.split('/')[-1][1:]
        time = key.split('/')[-2][1:]
        d[tag] = time

    # sort
    sbv = sorted(d.iteritems(), key=lambda (k,v): (v,k), reverse=True)
    for i, (k, v) in enumerate(sbv):
        print i, k, v



elif action == 'q3':
    start = "a{}/c00".format(input_)
    end = "a{}/c99".format(input_)

    d = {}

    result = tb.scan(row_start=start, row_stop=end)

    for key, data in result:
        user = key.split('/')[-1][1:]
        weight = key.split('/')[-2][1:]
        d[user] = int(weight)
    
    # sort
    sbv = sorted(d.iteritems(), key=lambda (k,v): (v,k), reverse=True)
    for i, (k, v) in enumerate(sbv):        
        print i, k, v

elif action == 'q4':
    start = "u{}/r00".format(input_)
    end = "u{}/r99".format(input_)

    d = {}
    info = {}

    result = tb.scan(row_start=start, row_stop=end, columns=['c:url', 'c:pictureurl'])
    for key, data in result:
        artist = key.split('/')[-1][1:]
        time = key.split('/')[-2][1:]
        d[artist] = time
        info[artist] = data

    sbv = sorted(d.iteritems(), key=lambda (k,v): (v,k), reverse=True)
    for i, (k, v) in enumerate(sbv):
        data = info[k]
        print i, k, v, data

else:
    print "Usage: <query action>: q1, q2, q3, q4"
    sys.exit(1)



