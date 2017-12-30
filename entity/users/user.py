#! /usr/bin/env python
# -*- coding: utf-8 -*-

class User(object):
    #Gmail account
    # email - genchevskiy.test@gmail.com
    # password - s.g19021992

    def __init__(self, first, last):
        self.first = first
        self.last = last

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    @property
    def email(self):
        return '{}.{}@gmail.com'.format(self.first, self.last)

    @property
    def password(self):
        return 'retail.buyer19021992qa'