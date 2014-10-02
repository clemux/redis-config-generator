#!/usr/bin/env python
# -*- coding:utf-8 -*-

from jinja2 import Environment, PackageLoader
import sys



def render_config(env, port, db_number, db_id, password):
    template = env.get_template('redis.conf')
    return template.render(port = port, db_number = db_number, db_id = db_id, password = password)


def main():
    if len(sys.argv) != 5:
        print ''
        print 'Usage: %s <DB_ID> <PORT> <DB_NUMBER>  <PASSWORD>' % (sys.argv[0],)
        print ''
        print 'DB_ID: ID or name'
        print 'PORT: TCP Port'
        print 'DB_NUMBER: Number of DB'
        print 'PASSWORD: Password'
        print ''
        sys.exit(1)

    env = Environment(loader=PackageLoader('generator', 'templates'))

    db_id = int(sys.argv[1])
    port = sys.argv[2]
    db_number = sys.argv[3]
    password = sys.argv[4]
    filename = "configurations/%i.conf" % db_id

    content = render_config(env, port, db_number, db_id, password)

    try:
        file = open(filename, "w")
        file.write(content)
        file.close()
        print "Your file is generated: %s" % filename
    except IOError as e:
        print e

if __name__ == '__main__':
    main()
