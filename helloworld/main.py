def hello_world(request):
    request_args = request.args
    if request.args and 'name' in request_args and 'lastname' in request_args:
        name = request_args['name']
        lastname = request_args['lastname']
    else:
        name = 'world'
        lastname = ''
    return f'Hellow {name} {lastname}'
