import gpay

Jananiya=gpay.Google_pay("JananiyaSadasivam@gmail.com","9003085347","jananiya")
Jananiya.open_gpay()
Jananiya.email_verification()
Jananiya.mobile_verification()
Jananiya.name_verification()
Jananiya.otp_verification(15698,15698)
Jananiya.Bank_verification()
Jananiya.PanCard_Verification()
Jananiya.set_Pin("5384")
Jananiya.Enter_your_Pin(3465,3465)

class Phone_pe(gpay.Google_pay):                                                                                          #INHERITANCE
    def __init__(slef,Email_ID,Phone_number,Name):
        super().__init__(Email_ID,Phone_number,Name)

    def open_phonepe(self):
        print("Phone pe")
        
Jananiya=Phone_pe("jan12345@gmail.com","8125467844","janni")
Jananiya.open_phonepe()
Jananiya.mobile_verification()
Jananiya.name_verification()
Jananiya.otp_verification(789564,891456)
Jananiya.Bank_verification()
Jananiya.PanCard_Verification()
Jananiya.set_Pin("678432")
Jananiya.Enter_your_Pin(8745,9087)


        
google_pay=[{"name":"jananiya","gpaynum":9000943786,"type":"personal","transaction":"regular"},                       #DICTIONARY INSIDE LIST
           {"name":"timple","gpaynum":8778132359,"type":"personal","transaction":"regular"},
           {"name":"sneha","gpaynum":8125177356,"type":"personal","transaction":"rare"},
           {"name":"kunal","gpaynum":7358355054,"type":"personal","transaction":"never"},
           {"name":"lokesh","gpaynum":7200636126,"type":"personal","transaction":"rare"},
           {"name":"priya","gpaynum":9597916931,"type":"personal","transaction":"rare"},
           {"name":"gayathri","gpaynum":8056469214,"type":"personal","transaction":"regular"},
           {"name":"takur","gpaynum":9962454833,"type":"personal","transaction":"rare"},
           {"name":"abi","gpaynum":8015341851,"type":"personal","transaction":"rare"},
           {"name":"kamal","gpaynum":7305624091,"type":"personal","transaction":"rare"},
           {"name":"surya","gpaynum":8939509826,"type":"personal","transaction":"rare"},
           {"name":"vijay","gpaynum":6369121983,"type":"personal","transaction":"regular"},
           {"name":"ashwin","gpaynum":9833807044,"type":"personal","transaction":"regular"},
           {"name":"asma","gpaynum":9941297487,"type":"personal","transaction":"rare"},
           {"name":"bagavathi","gpaynum":7200001990,"type":"personal","transaction":"regular"},
           {"name":"balaji","gpaynum":6382880108,"type":"personal","transaction":"rare"},
           {"name":"belgin","gpaynum":9941656319,"type":"personal","transaction":"regular"},
           {"name":"beulah","gpaynum":9500075619,"type":"personal","transaction":"rare"},
           {"name":"bhuvan","gpaynum":8072512570,"type":"personal","transaction":"regular"},
           {"name":"chandru","gpaynum":6382761961,"type":"personal","transaction":"rare"},
           {"name":"chipe","gpaynum":9791045340,"type":"personal","transaction":"regular"},
           {"name":"deen","gpaynum":9841032642,"type":"personal","transaction":"regular"},
           {"name":"deepa","gpaynum":6383908036,"type":"personal","transaction":"regular"},
           {"name":"dharan","gpaynum":8248631340,"type":"personal","transaction":"rare"},
           {"name":"divya","gpaynum":6374339918,"type":"personal","transaction":"regular"},
           {"name":"doss","gpaynum":9840644601,"type":"personal","transaction":"regular"},
           {"name":"durka","gpaynum":6379741175,"type":"personal","transaction":"regular"},
           {"name":"esther","gpaynum":8124252926,"type":"personal","transaction":"regular"},
           {"name":"femila","gpaynum":9176093745,"type":"personal","transaction":"regular"},
           {"name":"gautam","gpaynum":9176358088,"type":"personal","transaction":"regular"},
           {"name":"gayathri","gpaynum":7305331140,"type":"personal","transaction":"rare"},
           {"name":"gomathi","gpaynum":6384316771,"type":"personal","transaction":"regular"},
           {"name":"gracy","gpaynum":9150381712,"type":"personal","transaction":"regular"},
           {"name":"grishma","gpaynum":9003037517,"type":"personal","transaction":"regular"},
           {"name":"hari","gpaynum":9515605233,"type":"personal","transaction":"regular"},
           {"name":"haripriya","gpaynum":9791143754,"type":"personal","transaction":"regular"},
           {"name":"harikrishnan","gpaynum":8056265597,"type":"personal","transaction":"regular"},
           {"name":"hema","gpaynum":7010469081,"type":"personal","transaction":"regular"},
           {"name":"indumathi","gpaynum":6379840455,"type":"personal","transaction":"rare"},
           {"name":"jaya","gpaynum":9791280444,"type":"personal","transaction":"regular"},
           {"name":"jayadev","gpaynum":8667639927,"type":"personal","transaction":"rare"},
           {"name":"jeevitha","gpaynum":8667464628,"type":"personal","transaction":"regular"},
           {"name":"jemima","gpaynum":9962821791,"type":"personal","transaction":"regular"},
           {"name":"jes","gpaynum":9551852580,"type":"personal","transaction":"rare"},
           {"name":"jesintha","gpaynum":8939475795,"type":"personal","transaction":"regular"},
           {"name":"jo","gpaynum":7338935895,"type":"personal","transaction":"rare"},
           {"name":"joel","gpaynum":9444919116,"type":"personal","transaction":"regular"},
           {"name":"jonnah","gpaynum":8531025248,"type":"personal","transaction":"regular"},
           {"name":"josh","gpaynum":9789869415,"type":"personal","transaction":"regular"},
           {"name":"jothika","gpaynum":9677150962,"type":"personal","transaction":"regular"},
           {"name":"julaika","gpaynum":9003899016,"type":"personal","transaction":"rare"},
           {"name":"jv","gpaynum":9361486028,"type":"personal","transaction":"regular"},
           {"name":"kamali","gpaynum":6382826039,"type":"personal","transaction":"regular"},
           {"name":"kamini","gpaynum":9080995159,"type":"personal","transaction":"regular"},
           {"name":"kani","gpaynum":8220584872,"type":"personal","transaction":"rare"},
           {"name":"kannan","gpaynum":9710405288,"type":"personal","transaction":"rare"},
           {"name":"karthi","gpaynum":8778799456,"type":"personal","transaction":"regular"},
           {"name":"kavitha","gpaynum":9840042296,"type":"personal","transaction":"regular"},
           {"name":"keerthi","gpaynum":7305066119,"type":"personal","transaction":"rare"},
           {"name":"kingsley","gpaynum":8754554295,"type":"personal","transaction":"regular"},
           {"name":"kiran","gpaynum":6383634327,"type":"personal","transaction":"rare"},
           {"name":"kiruthika","gpaynum":9789029339,"type":"personal","transaction":"regular"},
           {"name":"kowsalya","gpaynum":7871125838,"type":"personal","transaction":"regular"},
           {"name":"kowsi","gpaynum":7448744931,"type":"personal","transaction":"rare"},
           {"name":"kumar","gpaynum":7358565943,"type":"personal","transaction":"regular"},
           {"name":"lekha","gpaynum":7305772128,"type":"personal","transaction":"regular"},
           {"name":"lokesh","gpaynum":7358479530,"type":"personal","transaction":"regular"}]


for i in google_pay:                                                                                                             #LOOPING
    for j,k in i.items():                                                                                                       #KEY VALUES LOOPING
        print(f"{j}:{k}")
    
