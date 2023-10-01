import matplotlib.pyplot as plt
import datetime
import pandas as pd


def calculate_age(born):
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

try:
    file_path = "employee.csv"
    df = pd.read_csv(file_path,encoding='utf-8-sig',delimiter=";")
except NameError:
    print('cant find csv file')
except:
    print('unable to create xlsx file')


gender_counts = df['Стать'].value_counts()
print(gender_counts)
gender_counts.plot(kind='bar')
plt.show()


df['Дата народження'] = pd.to_datetime(df['Дата народження'], format='%Y-%m-%d')
df['Дата народження']=df['Дата народження'].apply(calculate_age)
#df['Дата народження']=df['Дата народження'].astype(str)

df["Вік"]=""
df.loc[df['Дата народження']<18, "Вік"] = "<18"
df.loc[(df['Дата народження']>=18) & (df['Дата народження']<45), "Вік"] = "18-45"
df.loc[(df['Дата народження']>=45) & (df['Дата народження']<70), "Вік"] = "45-70"
df.loc[df['Дата народження']>=70, "Вік"] = ">70"

age_counts = df['Вік'].value_counts().sort_values()
age_counts.plot(kind='bar')
print(age_counts)
plt.show()


dfg = df.groupby(by=["Стать", "Вік"]).size()
print(dfg)
dfg.plot(kind='bar')
plt.show()