import csv
import random

'''This function generates simulated human trafficking data and writes it to a CSV file.'''
def generate_data():
    def generate_gender():
        r = random.randint(1, 30000)
        if 1 <= r <= 20000:
            return "Male"
        elif 20000 < r < 29000:
            return "Female"
        else:
            return "Other"

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
        'recruiterRelationFriend', 'recruiterRelationFamily', 'recruiterRelationOther'
    ]

    countries = ['USA', 'RUS', 'CHN', 'GBR', 'IND', 'FRA', 'CAN', 'AUS', 'DEU', 'BRA', 'JPN', 'ITA', 'ESP', 'MEX']

    age_groups = ['0--8', '09--17', '18--20', '21--23', '24--26', '27--29', '30--38', '39--47', '48+']

    age_distribution = [5, 10, 10, 40, 40, 20, 30, 30, 15]

    data_rows = []
    total_records = 30

    for i in range(total_records):
        age_broad = random.choices(age_groups, weights=age_distribution)[0]
        majority_status = "Minor" if age_broad in ['0--8', '09--17'] else "Adult"

        years1 = random.randint(0, 5)
        years2 = random.randint(years1 + 1, 6)
        traffick_months = f"{years1 * 12 + 1}--{years2 * 12} ({years1}-{years2} yrs)"

        registration_year = random.randint(2002, 2021)

        means_of_control_values = [random.choice([0, 1]) for _ in range(19)]
        type_of_labour_values = [random.choice([0, 1]) for _ in range(5)]
        type_of_sex_values = [random.choice([0, 1]) for _ in range(3)]
        recruiter_relation_values = [random.choice([0, 1]) for _ in range(4)]

        data_row = [
            registration_year, generate_gender(),
            age_broad, majority_status, traffick_months,
            random.choice(countries), random.choice(countries),
            *means_of_control_values,
            *type_of_labour_values,
            *type_of_sex_values,
            *recruiter_relation_values
        ]
        data_rows.append(data_row)

    with open('generated_data.csv', mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow(headers)
        writer.writerows(data_rows)

    print("Generated data written to 'generated_data.csv' file")
