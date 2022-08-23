import time

from pip._vendor import requests

from pprint import pprint

from datetime import datetime


def data_questions_request():
    datenow = datetime.now()
    timestamp_now = datetime.timestamp(datenow)
    differents_2_days = 172800
    timestamp_2_days = timestamp_now - differents_2_days
    page = 1
    list_pages = []
    while True:
        url = f"https://api.stackexchange.com/2.3/search?page={page}&pagesize=100&fromdate={int(timestamp_2_days)}&todate={int(timestamp_now)}&order=desc&sort=creation&tagged=python&site=stackoverflow"
        page += 1
        response = requests.get(url)
        time.sleep(0.33)
        correct_page = response.json()
        list_pages.append(correct_page)
        if len(correct_page) == 3:
            break
        if correct_page['has_more'] == False:
            return list_pages
        print(correct_page['has_more'])


if __name__ == '__main__':
    list_questions = data_questions_request()
    count = 0
    test = []
    if type(list_questions) == type(test):
        for block_questions in list_questions:
            for correct_question in block_questions['items']:
                count += 1
                print(correct_question['owner']['display_name'])
                print(correct_question['title'])
                print(datetime.fromtimestamp(correct_question['creation_date']))
                print()
        print(count)
    else:
        print('ERROR')