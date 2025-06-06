import random
import csv
import string

ids = ['958049', '348729', '348729', '441062', '441062', '246025', '246025', '866152', '866152', '558064', '558064', '894681', '220994', '220994', '220994', '551151', '551151', '551151', '737970', '861665', '861665', '343891', '343891', '275861', '275861', '589650', '589650', '589650', '284894', '284894', '284894', '929240', '243001', '243001', '243001', '688513', '688513', '688513', '442899', '935656', '715512', '141384', '141384', '578082', '506670', '506670', '506670', '673770', '673770', '673770', '788678', '999527', '999527', '999527', '418651', '418651', '418651', '243344', '489244', '489244', '489244', '272500', '272500', '340876', '340876', '340876', '894667', '894667', '480944', '480944', '480944', '951318', '951318', '312548', '312548', '312548', '750802', '750802', '750802', '958191', '958191', '958191', '135182', '135182', '135182', '456267', '978891', '978891', '978891', '138628', '180595', '180595', '180595', '376943', '279976', '367620', '367620', '706002', '706002', '368083', '368083', '368083', '609826', '609826', '503311', '503311', '779396', '779396', '441942', '441942', '441942', '143499', '143499', '143499', '463765', '146691', '202967', '202967', '202967', '402036', '402036', '613983', '613983', '613983', '720274', '720274', '876071', '833142', '833142', '833142', '284007', '284007', '284007', '755011', '755011', '755011', '669718', '551346', '551346', '551346', '857621', '527420', '527420', '527420', '500169', '500169', '538810', '538810', '538810', '827187', '827187', '827187', '728435', '751731', '751731', '751731', '588164', '237813', '237813', '566301', '566301', '566301', '560637', '560637', '469525', '406479', '204279', '502004', '502004', '749146', '749146', '749146', '951211', '951211', '438767', '438767', '581458', '415983', '415983', '415983', '669680', '669680', '362975', '362975', '643444', '643444', '590951', '455219', '101856', '101856', '376456', '376456', '401467', '401467', '311732', '311732', '487625', '487625', '373436', '373436', '373436', '841425', '841425', '841425', '261755', '261755', '261755', '297606', '283881', '283881', '283881', '272000', '272000', '806928', '806928', '806928', '228181', '692673', '692673', '132342', '132342', '132342', '466552', '207226', '207226', '207226', '869662', '869662', '869662', '984736', '984736', '984736', '815652', '815652', '462139', '462139', '462139', '478958', '882187', '882187', '697089', '697089', '368594', '368594', '368594', '424682', '424682', '682574', '362470', '362470', '362470', '522580', '522580', '443151', '443151', '893911', '893911', '871237', '871237', '871237', '240111', '796973', '598993', '692734', '995566', '780771', '780771', '129145', '129145', '129145', '873868', '873868', '722272', '722272', '722272', '785311', '785311', '396285', '653090', '653090', '653090', '330563', '330563', '434706', '434706', '673409', '673409', '281253', '281253', '281253', '717113', '114865', '114865', '114865', '963305', '963305', '742607', '742607', '742607', '513598', '513598', '160263', '160263', '160263', '159834', '159834', '159834', '501233', '501233', '501233', '756613', '115298', '706259', '706259', '706259', '369760', '369760', '843131', '843131', '843131', '195705', '490637', '490637', '409024', '535788', '535788', '535788', '971145', '102511', '102511', '102511', '518187', '518187', '518187', '577993', '577993', '535010', '230610', '230610', '230610', '816739', '816739', '816739', '436998', '436998', '359895', '961855', '961855', '873825', '873825', '873825', '297783', '297783', '474647', '474647', '474647', '474640', '474640', '474640', '614828', '614828', '614828', '636258', '636258', '764400', '192723', '762770', '762770', '487173', '487173', '487173', '225275', '225275', '423642', '423642', '546669', '546669', '546669', '183269', '183269', '836482', '836482', '310159', '310159', '310159', '772553', '772553', '772553', '893568', '893568', '893568', '335894', '335894', '406526', '406526', '614818', '614818', '482837', '593477', '593477', '593477', '146769', '975194', '927596', '927596', '927596', '436181', '436181', '436181', '373807', '373807', '245831', '827626', '827626', '827626', '583750', '583750', '583750', '653646']

def get_rand_date():
    months = ["01","02","03","04","05","06","07","08","09","10","11","12"]
    days = ["01","02","03","04","05","06","07","08","09","10","11","12","13","14","15","16","17","18","19","20","21","22","23","24"]
    years = ["2022","2023","2024"]

    return str(random.choice(months)) +"/"+ str(random.choice(days)) +"/"+ str(random.choice(years))

def get_division():
    div = ["IT","Sales","Marketing","Development","HR"]
    return random.choice(div)

def y_n():
    val = random.randint(0,1)
    if val == 0:
        return "N"
    return "Y"

def indiv_info():
    id = ids
    csv_full = []

    for i in id:
        csv_full.append([
        # ID
        i,

        # Messages/Week
        random.randint(0,30),

        # Date last promoted
        get_rand_date(),

        # PTO days
        random.randint(5,20),

        # Performance avg
        random.randint(5,10),

        # Years at company
        random.randint(5,10),

        # Prev companies (count)
        random.randint(0,4),


        # Deadlines missed
        random.randint(0,3),

        # hours late this year
        random.randint(0,5),


        # project count
        random.randint(3,10),
        ])

    print(csv_full)
    return csv_full

def gen_last_promo():
    list=[]
    id = ids

    for i in id:
        if i==1:
            list.append([i,str(random.randint(1,12)) +"/"+ str(random.randint(1,28) +"/"+ "2015")])
        elif i==2:
            list.append([i, str(random.randint(1, 12)) + "/" + str(random.randint(1, 28) + "/" + "2017")])
        else:
            list.append([i,get_rand_date()])

    return list


def gen_hr_data(count):
    list = []
    i = ids
    for x in range(count):
        list.append([i,

            # Throwaway date
            get_rand_date(),

            # Turnover Rate
            random.randint(1, 40),

            # Mgmt Roles
            random.randint(0, 15),

            # division
            get_division(),

            # Rate of Promotions
            random.randint(5, 25),

            # Training Hours
            random.randint(5, 10),

            # peers promoted
            random.randint(3, 10),

         ])

def recent_raises_bonus():
    id = ids

    list = []

    for i in id:
        list.append([i,random.randint(0,25)/10,y_n(),get_rand_date()])

    return list



def gen_pos_data(count):


    return

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    full_file = indiv_info()

    # create csv
    # headers = ("Employee ID,Turnover Rate,Recent Raise,Messages per Week,Number of Mgmt Roles,"
    #            "Rate of Promotions,Training Hours this Year,Date of last Promotion,PTO Days,Work "
    #            "Performance Avg,Total Years at Company,Previous Companies,Business Division,Number of "
    #            "Deadlines Missed,Hours Late this Year,Number of Peers Promoted,Number of High Profile "
    #            "Projects,Bonus Last Year")

    role_headers = ("Employee ID,Turnover Rate,Recent Raise,Number of Mgmt Roles,PTO Days")

    with open("role.csv", 'w') as csvfile:
        csvfile.write(role_headers+"\n")
        for row in full_file:
            # write row to file
            temp = ",".join(str(val) for val in row)
            csvfile.write(temp+"\n")

    with open("role.csv", "r") as csvfile:
        content = csvfile.read()
        print(content)


    indiv_headers = "Employee ID,"
    indiv_file = indiv_info()
    with open("indiv.csv", 'w') as csvfile:
        csvfile.write(indiv_headers+"\n")
        for row in indiv_file:
            # write row to file
            temp = ",".join(str(val) for val in row)
            csvfile.write(temp+"\n")

    last_promo_headers = "Employee ID,Date"
    promo_file = gen_last_promo()
    with open("promo.csv", 'w') as csvfile:
        csvfile.write(last_promo_headers+"\n")
        for row in promo_file:
            # write row to file
            temp = ",".join(str(val) for val in row)
            csvfile.write(temp+"\n")

    hr_headers = "Employee ID,Date,Turnover,Manamegent Roles,Division,Promotion Rate,Training Hours,Peers Prommoted"
    hr_file = gen_hr_data(len(ids))
    with open("hr.csv", 'w') as csvfile:
        csvfile.write(hr_headers+"\n")
        for row in hr_file:
            # write row to file
            temp = ",".join(str(val) for val in row)
            csvfile.write(temp+"\n")

    recent_raises_bonus_headers = "Employee ID,Bonus,Raise Date"
    raise_file = recent_raises_bonus()
    with open("raisebonus.csv", 'w') as csvfile:
        csvfile.write(recent_raises_bonus_headers+"\n")
        for row in raise_file:
            # write row to file
            temp = ",".join(str(val) for val in row)
            csvfile.write(temp+"\n")
