import uuid
def generate(countrycode = 'TH'):
    front = 'ABC'
    body = uuid.uuid4().hex
    body = body.upper()[0:8]
    code = front+body+countrycode
    return code

