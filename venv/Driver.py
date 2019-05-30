from Employee import *
class Driver(Employee):

    state_of_parcel=['Parcel is in the source branch','Parcel Express prepare to deliver','Parcel is at its destination','Waiting for receiver','Parcel receive']

    Province = ['Chiang_Mai', 'Chiang_Rai', 'Phayao','Nan','Lamphun','Lampang','Phrae','Uttaradit','Tak','Sukhothai','Phitsanulok','Kamphaeng_Phet','Phichit'
    ,'Uthai_Thani','Nakhon_Sawan','Phetchabun','Loei','Udon_Thani','Nongbua_Lumphoo','Nong_Khai','Sakon_Nakhon','Nakhon_Phanom','Mukdahan','Kalasin','Maha Sarakham','Khon Kaen'
    ,'Chaiyaphum','Roi_Et,Nakhon','Ratchasima,Buri_Ram','Surin,Si_Sa_Ket','Ubon_Ratchathani','Umnad_Chareun','Yasothon','Ratchaburi','Phetchaburi', 'Prachuap_Khiri_Khan', 'Chai_Nat'
    ,'Sing_Buri','Lop_Buri', 'Ang_Thong', 'Phra_Nakhon_Si_Ayuttaya', 'Saraburi', 'Pathum_Thani','Nonthaburi','Bangkok','Samut_Prakan','Samut_Songkhram', 'Samut_Sakhon', 'Nakhon_Pathom', 'Nakhon_Nayok'
    ,'Prachin_Buri','Sa_Kaew','Cha_Choeng_Sao','Chon_Buri','Rayong','Chanthaburi','Trat','Chumphon','Ranong', 'Surat_Thani', 'Phang_Nga', 'Phuket', 'Krabi', 'Nakhon_Si_Thammarat'
    ,'Phatthalung','Trang','Satun','Song_Khla','Pattani','Yala','Narathiwat','Suphan_Buri','Kanchanaburi']

    def __init__(self, name, address, phone, email):
        super().__init__(name,address,phone,email)

    def update(self,provinceReach):


