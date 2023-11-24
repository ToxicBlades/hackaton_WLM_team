import csv
import random

def generate_data(n):

    def generate_gender():
        r = random.randint(1, 30000)
        if 1 <= r <= 20000:
            return "Female"
        elif 20000 < r < 29000:
            return "Male"
        else:
            return "Other"

    # Заголовки столбцов
    headers = [
        'yearOfRegistration', 'gender', 'ageBroad', 'majorityStatusAtExploit', 'traffickMonths',
        'citizenship', 'CountryOfExploitation', 'meansOfControlDebtBondage', 'meansOfControlTakesEarnings',
        'meansOfControlThreats', 'meansOfControlPsychologicalAbuse', 'meansOfControlPhysicalAbuse',
        'meansOfControlSexualAbuse', 'meansOfControlFalsePromises', 'meansOfControlPsychoactiveSubsta',
        'meansOfControlRestrictsMovement', 'meansOfControlRestrictsMedicalCa', 'meansOfControlExcessiveWorkingHo',
        'meansOfControlThreatOfLawEnforce', 'meansOfControlWithholdsNecessiti', 'meansOfControlWithholdsDocuments',
        'meansOfControlOther', 'isForcedLabour', 'isSexualExploit', 'isOtherExploit', 'typeOfLabourAgriculture',
        'typeOfLabourConstruction', 'typeOfLabourDomesticWork', 'typeOfLabourHospitality', 'typeOfLabourOther',
        'typeOfSexProstitution', 'typeOfSexPornography', 'typeOfSexOther', 'recruiterRelationIntimatePartner',
        'recruiterRelationFriend', 'recruiterRelationFamily', 'recruiterRelationOther',
        'typeOfTraffickingForcedLabour', 'typeOfTraffickingSexualExploit', 'typeOfTraffickingOtherExploit'
    ]

    # Список трёхбуквенных кодов стран
    countries = ['USA', 'RUS', 'POL','KAZ', 'IDN', 'LBY', 'TUR', 'MYS', 'MGD',
                 'PHL', 'LBN', 'UKR','CHN','SAU','EGY','KHM','ARE','THA','HTI',
                 'MLI','SRB','JOR','ITA','ARG','BLR','SEN','ZAF','PHL','KEN',
                 'UGA','BIH','MKD','GHA','ROU','JPN','DEU','UZB',
                 'NGA','ALB','AFG','IND','BGR','TJK','KWT','QAT','OMN','HKG',
                 'IRQ','CZE','MDA','MAR','PRT','SDN','GRC','MEX','ETH','VNM','ESP',
                 'TUN','CIV','TKM','GEO','SLE','TTO','SGP','NER','BDI','GBR','TZA',
                 'DNK','SYR','AUT','SWE','TWN','ZMB','ECU','CHE','BHR','IRL','KGZ',
                 'MWI','KOR','FRA','DOM','COL','MDG','CYP','BFA','VUT','NLD','ISR','TKL','SOM','GAB','MOZ','TCD','DZA','DJI','BEL','GTM','MUS','CMR','PRK','BRN','LTU','SVK','MRT','ARM','PAK','GUY','PNG','GIN','HND','NPL','NOR','FIN','PER','BHS'
                 ]
    # Группы возрастов
    age_groups = ['0--8', '09--17', '18--20', '21--23', '24--26', '27--29', '30--38', '39--47', '48+']

    # Пропорции распределения возрастов
    age_distribution = [5, 10, 40, 20, 30, 30, 40, 5, 10]

    # Генерация данных для 10 записей
    data_rows = []

    for i in range(n):
        age_broad = random.choices(age_groups, weights=age_distribution)[0]
        majority_status = "Minor" if age_broad in ['0--8', '09--17'] else "Adult"

        years1 = random.randint(0, 5)
        years2 = random.randint(years1 + 1, 6)
        traffick_months = f"{years1 * 12}--{years2 * 12} ({years1}-{years2} yrs)"

        registration_year = random.randint(2002, 2021)

        type_of_labour_values = [0, 0, 0, 0, 0]
        random_index = random.randint(0, 4)
        type_of_labour_values[random_index] = 1

        # Подсчет количества единиц в последних 4 столбцах
        last_4_columns = [random.randint(0, 1) for _ in range(4)]
        while sum(last_4_columns) != 1:
            last_4_columns = [random.randint(0, 1) for _ in range(4)]

        data_row = [
            registration_year, generate_gender(),
            age_broad, majority_status, traffick_months,
            random.choice(countries), random.choice(countries),
            *random.choices([0, 1], k=20),
            *type_of_labour_values,
            *last_4_columns
        ]
        data_rows.append(data_row)

    with open('generated_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data_rows)

    print("Сгенерированные данные записаны в файл 'generated_data.csv'")

generate_data(1000)