from Employee import *
from Parcel import Parcel
class Driver(Employee):


    state_of_parcel = ['Parcel is in the source branch', 'Parcel Express driver prepare to deliver',
                       'Parcel is at its destination', 'Waiting for receiver', 'Parcel receive']

    Province = ['Chiang_Mai', 'Chiang_Rai', 'Phayao','Nan','Lamphun','Lampang','Phrae','Uttaradit','Tak','Sukhothai','Phitsanulok','Kamphaeng_Phet','Phichit'
    ,'Uthai_Thani','Nakhon_Sawan','Phetchabun','Loei','Udon_Thani','Nongbua_Lumphoo','Nong_Khai','Sakon_Nakhon','Nakhon_Phanom','Mukdahan','Kalasin','Maha Sarakham','Khon Kaen'
    ,'Chaiyaphum','Roi_Et,Nakhon','Ratchasima,Buri_Ram','Surin,Si_Sa_Ket','Ubon_Ratchathani','Umnad_Chareun','Yasothon','Ratchaburi','Phetchaburi', 'Prachuap_Khiri_Khan', 'Chai_Nat'
    ,'Sing_Buri','Lop_Buri', 'Ang_Thong', 'Phra_Nakhon_Si_Ayuttaya', 'Saraburi', 'Pathum_Thani','Nonthaburi','Bangkok','Samut_Prakan','Samut_Songkhram', 'Samut_Sakhon', 'Nakhon_Pathom', 'Nakhon_Nayok'
    ,'Prachin_Buri','Sa_Kaew','Cha_Choeng_Sao','Chon_Buri','Rayong','Chanthaburi','Trat','Chumphon','Ranong', 'Surat_Thani', 'Phang_Nga', 'Phuket', 'Krabi', 'Nakhon_Si_Thammarat'
    ,'Phatthalung','Trang','Satun','Song_Khla','Pattani','Yala','Narathiwat','Suphan_Buri','Kanchanaburi']

    def __init__(self,pick_up,destination,name='',phoneNumber='',email='',province=''):
        super().__init__(name,phoneNumber,email,province)
        self.pickUpAddress=pick_up
        self.Destination=destination
        self.Current_state=-1

    def getState_of_parcel(self):
        return self.Current_state


    def getAllParcelByProvinceOrigin(self,Province):
        Parcel.mycursor.execute("SELECT TrackingNumber,Sender_province from Parcel")
        tracking_number=[]
        myresult = Parcel.mycursor.fetchall()
        for Traking_number,Location in myresult:
            if(Location == Province):
                tracking_number.append(Traking_number)
        return tracking_number

    def getAllParcelByProvinceFinal(self, Province):
        Parcel.mycursor.execute("SELECT TrackingNumber,Receiver_province from Parcel")
        tracking_number = []
        myresult = Parcel.mycursor.fetchall()
        for Traking_number, Location in myresult:
            if (Location == Province):
                tracking_number.append(Traking_number)
        return tracking_number

    def collected(self):
        state=self.state_of_parcel[1]
        Pickup_trackingNumber=self.getAllParcelByProvinceOrigin(self.pickUpAddress)
        for i in Pickup_trackingNumber:
            Parcel.mycursor.execute("UPDATE Parcel SET State = '"+ state +"'where TrackingNumber = '"+str(i)+"';" )
            Parcel.mydb.commit()

    def ReachDestination(self):

        state=self.state_of_parcel[2]
        Reach_trackingNumber=self.getAllParcelByProvinceFinal(self.Destination)
        for i in Reach_trackingNumber:
            print(i)
            Parcel.mycursor.execute("UPDATE Parcel SET State = '"+ state +"'where TrackingNumber = '"+str(i)+"';" )
            Parcel.mydb.commit()



