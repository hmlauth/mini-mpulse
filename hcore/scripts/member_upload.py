import json
import requests
import pandas as pd

from mini_mpulse.settings import AUTH_TOKEN_URL, MEMBER_CREATE_URL, CHUNKSIZE, SEPARATOR
from mini_mpulse.sensitive_settings import USERNAME, PASSWORD


def generate_request_body(row, columns):
    member = {}
    for column in columns:
        member[column] = row[column]
    return member


def get_auth_token():
    data = {
        "username": USERNAME,
        "password": PASSWORD
    }
    response = requests.post(
        url=AUTH_TOKEN_URL,
        headers={"Content-Type": "application/json"},
        json=data
    )
    print(f"Response Status Code: {response.status_code} | Response Content: {response.content}")
    if not response.status_code == 200:
        return response.content

    response_content = json.loads(response.content)
    return response_content['auth_token']


def process_file(auth_token, csv_file):
    for chunk in pd.read_csv(
            csv_file,
            dtype=object,
            sep=SEPARATOR,
            chunksize=CHUNKSIZE
    ):
        print(chunk)
        for column in chunk.columns:
            chunk[column] = chunk[column].apply(lambda i: str(int(i)) if isinstance(i, float) else str(i))

        member_list = chunk.astype(str).apply(
            generate_request_body, args=(chunk.columns,), axis=1
        ).to_list()

        request_body = json.dumps({"members": member_list})
        print(f'Request Body: {request_body}')
        response = requests.post(
            url=MEMBER_CREATE_URL,
            headers={
                "Authorization": f"Token {auth_token}",
                "Content-Type": "application/json"
            },
            data=request_body
        )
        print(f"Response Status Code: {response.status_code} | Response Content: {response.content}")

        return True
