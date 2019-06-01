import uuid

def generate(countrycode = 'TH'):
    front = 'PAE'
    body = uuid.uuid4().hex
    body = body.upper()[0:8]
    code = front+body+countrycode
    return code

def generate2():
    
    body = uuid.uuid4().hex
    body = body.upper()[0:4]
    return body
