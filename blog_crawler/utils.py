#!/usr/bin/env python
# coding=utf-8

from datetime import datetime

__author__ = 'hbprotoss'


def join_text(parts):
    return ''.join((p for p in parts if p.strip()))


def str_from_xpath(selector, xpath):
    return join_text(selector.xpath(xpath).extract())


def set_from_xpath(selector, xpath):
    return set(selector.xpath(xpath).extract())


def standard_time(ts):
    datetime.fromtimestamp(ts).strftime('%Y-%m-%d %H:%M:%S')
