import pandas as pd

df = pd.read_excel("challenge.xlsx")

formInfo = []
for index, row in df.iterrows():
    formInfo.append([
      {
        "xpath": '//*[@ng-reflect-name="labelPhone"]',
        "value": row['phoneNumber'],
        "printMsg": "Clicou no Phone Number",
        "error_msg": "Error to interact with PhoneNumber"
      },
      {
        "xpath": '//*[@ng-reflect-name="labelAddress"]',
        "value": row['address'],
        "printMsg": "Clicou no Address",
        "error_msg": "Error to interact with Address"
      },
      {
        "xpath": '//*[@ng-reflect-name="labelFirstName"]',
        "value": row['firstName'],
        "printMsg": "Clicou no FirstName",
        "error_msg": "Error to interact with FirstName"
      },
      {
        "xpath": '//*[@ng-reflect-name="labelLastName"]',
        "value": row['lastName'],
        "printMsg": "Clicou no LastName",
        "error_msg": "Error to interact with LastName"
      },
      {
        "xpath": '//*[@ng-reflect-name="labelCompanyName"]',
        "value": row['companyName'],
        "printMsg": "Clicou no CompanyName",
        "error_msg": "Error to interact with CompanyName"
      },
      {
        "xpath": '//*[@ng-reflect-name="labelEmail"]',
        "value": row['email'],
        "printMsg": "Clicou no Email",
        "error_msg": "Error to interact with Email"
      },
      {
        "xpath": '//*[@ng-reflect-name="labelRole"]',
        "value": row['roleCompany'],
        "printMsg": "Clicou no Role",
        "error_msg": "Error to interact with Role"
      },
    ])
