from faker import Faker
import pandas as pd
import numpy as np
from datetime import datetime
import random


def faker_categorical(num=1, seed=None):
    np.random.seed(seed)
    fake.seed_instance(seed)


fake = Faker(locale='uk_UA')

male_patronymics = ["Іванович", "Петрович", "Олександрович", "Володимирович", "Євгенович", "Михайлович", "Андрійович", "Сергійович", "Юрійович", "Аркадійович", "Вікторович", "Анатолійович", "Дмитрович", "Тимофійович", "Васильович", "Кузьмич", "Федорович", "Георгійович", "Ярославович", "Борисович"]
female_patronymics = ["Іванівна", "Петрівна", "Олександрівна", "Володимирівна", "Євгенівна", "Михайлівна", "Андріївна", "Сергіївна", "Юріївна", "Аркадіївна", "Вікторівна", "Анатоліївна", "Дмитрівна", "Тимофіївна", "Василівна", "Кузьмівна", "Федорівна", "Георгіївна", "Ярославівна", "Борисівна"]


def create_employees(num):
    employee_list=[]
    for i in range (1, num+1):
        gender = np.random.choice(["Ч", "Ж"], p=[0.6, 0.4])
        address = fake.address()
        asplit=address.split(",")
        city=asplit[2]


        employee={}
        employee['Прізвище'] = fake.last_name_male() if gender=="Ч" else fake.last_name_female()
        employee['Ім\'я'] = fake.first_name_male() if gender=="Ч" else fake.first_name_female()
        employee['По-батькові'] = random.choice(male_patronymics) if gender=="Ч" else random.choice(female_patronymics)
        employee['Стать'] = gender
        employee['Дата народження'] = fake.date_between_dates(date_start=datetime(1939,1,1), date_end=datetime(2008,12,31))
        employee['Посада'] = fake.job()
        employee['Місто проживання'] = city
        employee['Адреса проживання'] = address
        employee['Телефон'] = fake.phone_number()
        employee['Email'] = fake.email()
        employee_list.append(employee)
    return pd.DataFrame(employee_list)

n=2000
data = create_employees(n)
try:
    data.to_csv('employee.csv',sep=";",  encoding='utf-8-sig', index= False)
except:
    print("en error occured while creating csv file")
else:
    print("file created successfully, ",n, " rows has been generated")
