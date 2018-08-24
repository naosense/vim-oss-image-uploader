# -*- coding: utf-8 -*-

import nos


def upload(access_key, secret_key, end_point, bucket_name, prefix, image_path):
    client = nos.Client(access_key, secret_key, end_point=end_point)

    index = image_path.rfind('/')
    if index == -1:
        index = image_path.rfind('\\')

    key = prefix + '/' + image_path[index + 1:]

    client.put_object(bucket_name, key, open(image_path, "rb"))

    return key
