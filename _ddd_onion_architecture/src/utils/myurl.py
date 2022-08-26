from typing import AnyStr
import urllib.parse


def parse_query_parameters(query_parameters: str):
    qs = query_parameters.lstrip('?')
    qs_d = urllib.parse.parse_qs(qs)

    result = {}
    for key in qs_d:
        result[key] = qs_d[key][0]
    return result
