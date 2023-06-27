from task1 import list_transformation, visits_from_Russia, unique_id
# import pytest

def test_list_transformation():
    res = list_transformation()
    assert type(res) == dict

def test_visits_from_Russia():
    res = visits_from_Russia()
    list_country = []
    for item in res:
        for v in item.values():
            list_country.append(v[1])
    set(list_country)
    assert {'Россия'} == set(list_country)

def test_unique_id():
    res = unique_id()
    assert list(set(res)) == res