# -*- coding: utf-8 -*-

import oss2


def upload(access_key, secret_key, end_point, bucket_name, prefix, image_path):
    auth = oss2.Auth(access_key, secret_key)
    bucket = oss2.Bucket(auth, end_point, bucket_name, enable_crc=False)

    index = image_path.rfind('/')
    if index == -1:
        index = image_path.rfind('\\')

    key = prefix + '/' + image_path[index + 1:]

    bucket.put_object_from_file(key, image_path)

    return key