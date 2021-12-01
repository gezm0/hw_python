# with .. as
import csv
import redis

csv_file  = 'topic_5/endpoints.csv'
#rconn = redis.Redis(host='127.0.0.1', port='6379', db=5)
# for decoding response from bytes to string
rconn = redis.Redis(host='127.0.0.1', port='6379', db=5, decode_responses=True)

def readcsv():

    data_csv = []

    with open(csv_file, 'r') as file:
#    for line in file:
#        print(line)
        line = csv.DictReader(file, delimiter=',', fieldnames=['country', 'url', 'username', 'passwd'])
        for data in line:
           data_csv.append(data)
    return data_csv


def payload_gen(data):
    payload = []
    payload.append([data['country'], data['url']])
    return payload

def to_redis(payload):
    for pair in payload:
        rconn.rpush(pair[0], pair[1])

for raw_dict in readcsv():
    to_redis(payload_gen(raw_dict))

# get an information from database
# for range from 0 to 1000 and print it
for i in rconn.lrange('NL', 0, 1000):
    print(i)
