import pandas as pd
import datetime
pd.options.mode.chained_assignment = None


def calculate_age(born):
    #born = datetime.datetime.strptime(born, "%Y-%m-%d").date()
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


try:
    writer = pd.ExcelWriter('zavd2.xlsx')
    pd.read_csv('employee.csv', encoding='utf-8-sig',delimiter=";").to_excel(writer,'all',index= False)
    writer.close()
except NameError:
    print('cant find csv file')
except:
    print('unable to create xlsx file')


try:
    df_all = pd.read_excel('zavd2.xlsx', sheet_name='all')
    df_all['Дата народження'] = pd.to_datetime(df_all['Дата народження'], format='%Y-%m-%d')
    # df_all = df_all.set_index('Дата народження')
except PermissionError:
    print('permission to open xlsx file is denied')
except:
    print('an error occured while reading xlsx file')

try:
    df_18=df_all
    df_18_45=df_all
    df_45_70=df_all
    df_70=df_all

    df_18['вік']=df_18['Дата народження'].apply(calculate_age)
    df_18_45['вік']=df_18_45['Дата народження'].apply(calculate_age)
    df_45_70['вік']=df_45_70['Дата народження'].apply(calculate_age)
    df_70['вік']=df_70['Дата народження'].apply(calculate_age)


    df_18=df_18[df_18['вік']<18]
    df_18_45=df_18_45[(df_18_45['вік']>18) &
                      (df_18_45['вік']<45)]
    df_45_70=df_45_70[(df_45_70['вік']>45) &
                      (df_45_70['вік']<70)]
    df_70=df_70[df_70['вік']>70]


    df_18.drop(['Стать', 'Посада','Місто проживання','Адреса проживання','Телефон','Email'], axis=1, inplace=True)
    df_18_45.drop(['Стать', 'Посада','Місто проживання','Адреса проживання','Телефон','Email'], axis=1, inplace=True)
    df_45_70.drop(['Стать', 'Посада','Місто проживання','Адреса проживання','Телефон','Email'], axis=1, inplace=True)
    df_70.drop(['Стать', 'Посада','Місто проживання','Адреса проживання','Телефон','Email'], axis=1, inplace=True)

    with pd.ExcelWriter('zavd2.xlsx', engine='openpyxl', mode='a') as writer:
        df_18.to_excel(writer, sheet_name='younger_18', index=False)
        df_18_45.to_excel(writer, sheet_name='18-45',index=False)
        df_45_70.to_excel(writer, sheet_name='45-70',index=False)
        df_70.to_excel(writer, sheet_name='older_70',index=False)
except:
    print('an error occured')
else:
    print("ok")

