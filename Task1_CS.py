#Import the dataset and inspect its structure

import pandas as pd
df=pd.read_csv(r"C:\Users\harsh\OneDrive\Desktop\only hars\Task_1.csv")
print(df.head())
print(df.tail())
print(df.shape)
print(df.info())
print(df.columns)

#Identify missing values
print(df.isnull().sum())

#Identify duplicate records
print("Duplicate Records:",df.duplicated().sum())

#Identify inconsistent data entries
for col in ["Gender", "City", "Payment_Method"]:
    print(col)
    print(df[col].unique())
#Correct inconsistent values

df["Gender"]= (
    df["Gender"]
    .astype("string")
    .str.strip()
    .str.lower()
    .map({
       "male":"Male",
        "female":"Female"
        }))

df["City"]=df["City"].astype("string").str.strip().str.title()

df["Payment_Method"]=(
    df["Payment_Method"]
    .astype("string")
    .str.strip()
    .str.lower() 
    .map({
        "upi" : "UPI" ,
        "credit card" : "Credit Card" ,
        "debit card" : "Debit Card" ,
        "cash" : "Cash"
        })
    )


#Correct data types

df["Age"] = pd.to_numeric(df["Age"], errors = "coerce")

df["Purchase_Amount"]=pd.to_numeric(df["Purchase_Amount"],errors="coerce")

df["Purchase_Date"]=pd.to_datetime(df["Purchase_Date"],format = "%d-%m-%Y" , errors = "coerce")

#Handle missing numerical values

df["Age"]=df["Age"].fillna(df["Age"].median()).astype(int)
df["Purchase_Amount"] = df["Purchase_Amount"].fillna(df["Purchase_Amount"].median())

#Handle missing categorical values

for col in ["Gender", "City", "Payment_Method"]:
    df[col] = df[col].fillna(df[col].mode()[0])

#Remove duplicate records

df=df.drop_duplicates().reset_index(drop =True)

#Verify the cleaned dataset
print("Missing values:")
print(df.isnull().sum())

print("Duplicates:")
print(df.duplicated().sum())

print("Data types:")
print(df.dtypes)

print("Cleaned dataset:")
print(df.head())

#Save the cleaned dataset in new csv file
df.to_csv(r"C:\Users\harsh\OneDrive\Desktop\only hars\Task1_cleaned.csv",index=False)
print("Cleaned dataset successfully stored in new csv file ")




















