import os
from chalice import Chalice, Response
from chalice import BadRequestError, ChaliceViewError
from faker import Faker
from chalicelib.generator_list import blacklisted_generators, available_generators

fake = Faker()
app = Chalice(app_name='trmpt')
dir_path = os.path.dirname(os.path.realpath(__file__))


@app.route('/', methods=['GET'], cors=True)
def index():
    with open('%s/chalicelib/index.html' % dir_path, 'r') as myfile:
        html=myfile.read().replace('\n', '')
    return Response(
        body=html,
        status_code=200,
        headers={'Content-Type': 'text/html'}
    )


@app.route('/schema', methods=['GET'], cors=True)
def get_schema():
    return {
        'available_generators': available_generators,
        'example_request': '/generator/address?count=5'
    }


@app.route('/generator/{data_type}', methods=['GET'], cors=True)
def get_data(data_type):
    #return app.current_request.to_dict()
    try:
        data_type = data_type if not data_type in blacklisted_generators else ''
        data_generator = getattr(fake, data_type)
        count = 1
        if app.current_request.query_params:
            count = app.current_request.query_params.get('count', 1)
            count = int(count) if str(count).isdigit() else 1
            count = count if count <= 100 else 100
        results = []
        for i in range(0, count):
            data = data_generator()
            results.append(data)
        return {
            'record_count': len(results),
            'data': results
        }
    except AttributeError as e:
        raise BadRequestError("Invalid generator [%s]" % data_type)
    except Exception as e:
        raise ChaliceViewError(e.message)
