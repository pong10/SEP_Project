import uuid

def generate(countrycode = '--'):
    front = 'ABC'
    body = uuid.uuid4().hex
    body = body.upper()[0:8]
    code = front+body+countrycode
    return code

#just enter country code

if __name__ == "__main__":
    a = "TH"
    print(generate(a))
    
