import requests

token_YA = ""
path = 'New_folder_for_test'
def new_folder(token_YA, path):
    url = 'https://cloud-api.yandex.net/v1/disk/resources'
    res = requests.put(
        url,
        headers = {"Authorization": token_YA},
        params={'path': path}
    )
    return res

print(new_folder(token_YA, path).status_code)