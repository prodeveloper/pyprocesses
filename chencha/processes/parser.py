#!/usr/bin/env python
# encoding: utf-8

import importlib


def run(data, file_path, function_name):
        file_data = file_import(file_path)
        listeners = get_listeners(file_data)
        for listener in listeners:
            getattr(listener, function_name)(data)


def file_import(file_path):
    with open(file_path) as data_file:
        data = data_file.read().splitlines()
    return data


def get_listeners(file_data):
    results = []
    for item in file_data:
        parts = item.split(":")
        m = importlib.import_module(parts[0])
        c = getattr(m, parts[1])
        results.append(c)
    return results
