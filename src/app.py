import os, sys, json

dir_path = os.path.dirname(os.path.realpath(__file__))
sys.path.append('%s/vendor.zip' % dir_path)

from faker import Faker
from generator_list import blacklisted_generators, available_generators

fake = Faker()


def make_response(code, body):
    return {
        "statusCode": code,
        "headers": {
            "Access-Control-Allow-Origin": "*",
            'Content-Type': 'application/json'
        },
        "body": json.dumps(body)
    }


def get_fake_data(generator, count=1):
    
    try:
        generator = generator if not generator in blacklisted_generators else ''
        data_generator = getattr(fake, generator)
        count = int(count) if str(count).isdigit() else 1
        count = count if count <= 100 else 100
        results = []
        for i in range(0, count):
            data = data_generator()
            results.append(data)
        return make_response(200, {
            'record_count': len(results),
            'data': results
        })
    except Exception as e:
        body = {
            'error': 'Invalid generator or object count specified',
            'available_generators': available_generators,
            'example_request': '?generator=address&count=5'
        }
        return make_response(400, body)


def lambda_handler(event, context):
    method = event.get('httpMethod', 'GET')
    args = event.get('queryStringParameters')
    args = args if args else {} # set to empty dict if missing
    count = args.get('count', 1)
    generator = args.get('generator', '')

    if method == 'OPTIONS':
        return make_response(200, {
            'available_generators': available_generators,
            'example_request': '?generator=address&count=5'
        })
    elif generator == '':
        with open('%s/index.html' % dir_path, 'r') as myfile:
            data=myfile.read().replace('\n', '')
        return {
            "statusCode": 200,
            "headers": {
                'Content-Type': 'text/html'
            },
            "body": data
        }
    else:
        return get_fake_data(generator, count)

    resp = get_fake_data(generator, count)


def main():
    print(lambda_handler({}, {}))


if __name__ =='__main__':
    main()