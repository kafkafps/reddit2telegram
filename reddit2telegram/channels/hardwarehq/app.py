#encoding:utf-8

subreddit = 'Hardware'
t_channel = '@HardwareHQ'


def send_post(submission, r2t):
    return r2t.send_simple(submission)
