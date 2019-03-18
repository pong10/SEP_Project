import aftership
api = aftership.APIv4('270908a6-934b-45cd-bada-b47c2d82792c')
couriers = api.couriers.all.get()
print(couriers)
