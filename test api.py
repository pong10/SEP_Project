import aftership
api = aftership.APIv4('95ce5ddb-72f6-4e0c-9114-a185374ec85d')
couriers = api.couriers.all.get()
print(couriers)
#slug = 'thailand-post'
slug = 'kerry-logistics'
#number = 'EW332041693TH'
number ='SMMS000109643'
detail=api.last_checkpoint.get(slug, number, fields=['title', 'created_at','customer_name','checkpoint_time','city','country_iso3','tag'])
print(detail)
id=detail['id']
tracking_number=detail['tracking_number']
print(id)