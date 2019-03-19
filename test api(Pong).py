import aftership
api = aftership.APIv4('95ce5ddb-72f6-4e0c-9114-a185374ec85d')
couriers = api.couriers.all.get()
#print(couriers)
#slug = 'thailand-post'
slug = 'thailand-post'
#number = 'EW332041693TH'
number ='EW332041693TH'
detail=api.last_checkpoint.get(slug, number, fields=['title', 'created_at','customer_name','checkpoint_time','city','country_iso3','tag'])
print(detail)
id=detail['id']
tracking_number=detail['tracking_number']
#<<<<<<< HEAD


print(id)
#=======
print(id)
#>>>>>>> 0fc988d5dff5ae7a836162baee8b0de8ecd76667

#Find last checkpoint
#api.last_checkpoint.get(slug, number, fields=[])

#Find all checkpoint
#api.trackings.get(slug,number,fields=['checkpoints'])
