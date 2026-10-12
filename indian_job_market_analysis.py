Python 3.14.7 (tags/v3.14.7:823f032, Aug  5 2026, 10:51:32) [MSC v.1944 64 bit (AMD64)] on win32
Enter "help" below or click "Help" above for more information.
import pandas as pd

df=pd.read_excel(r"C:\Users\Administrator\Downloads\indian-job-market-dataset-2025.xlsx")
print(df)

df["comapnyName"]=
SyntaxError: invalid syntax
print(df.head())
                                         title  ...  maximumExperience
0                    Sr. HR Recruiter (NON IT)  ...                4.0
1                      Fire And Safety Officer  ...               11.0
2  Opening For Performance Marketing - Chennai  ...               18.0
3                    Medical Billing Executive  ...                3.0
4  Senior Group Product Manager -  CNS Therapy  ...               10.0

[5 rows x 17 columns]
print(df.shape)
(97929, 17)
print(df.columns)
Index(['title', 'jobId', 'currency', 'jobUploaded', 'companyName',
       'tagsAndSkills', 'experience', 'salary', 'location', 'companyId',
       'ReviewsCount', 'AggregateRating', 'jobDescription', 'minimumSalary',
       'maximumSalary', 'minimumExperience', 'maximumExperience'],
      dtype='str')
print(df.columns.tolist())
['title', 'jobId', 'currency', 'jobUploaded', 'companyName', 'tagsAndSkills', 'experience', 'salary', 'location', 'companyId', 'ReviewsCount', 'AggregateRating', 'jobDescription', 'minimumSalary', 'maximumSalary', 'minimumExperience', 'maximumExperience']
df["companyName"]=df["companyName"].fillna("unknown")
df["tagsAndSkills"]=df["tagsAndSkills"].fillna("unknown")
df["experience"]=df["experience"].fillna("unknown")
df["ReviewsCount"]=df["ReviewsCount"].fillna(0)
df["AggregateRating"]=df["AggregateRating"].fillna("unknown")
df=["minimumSalary"]=df["minimumSalary"].fillna("unknown")
SyntaxError: cannot assign to literal
df=["minimumSalary"]=df["minimumSalary"].fillna("unknown")
SyntaxError: cannot assign to literal
df=["minimumSalary"]=df["minimumSalary"].fillna("unknown")
SyntaxError: cannot assign to literal
df=["minimumSalary"]=df["minimumSalary"].fillna("unknown")
SyntaxError: cannot assign to literal
df["minimumSalary"]=df["minimumSalary"].fillna("unknown")
df["maximumSalary"]=df["maximumSalary"].fillna("unknown")
df["minimumExperience"]=df["minimumExperience"].fillna("unknown")
df["maximumExperience"]=df["maximumExperience"].fillna("unknown")
df=df.drop_duplicates()
print(df.isnull().sum().sum())
0
print(df.duplicated().sum())
0
print(df.shape)
(97682, 17)
print("Total jobs:", len(df))
Total jobs: 97682
print("Unique companies:",df["companyName"].nunique())
Unique companies: 18669
print("Unique Job Titles:",df["title"].nunique())
Unique Job Titles: 55104
print(df["title"].value_counts().head(10))
title
Application Developer             2033
Application Lead                  1346
Sales Executive                    576
Software Development Engineer      497
Business Development Executive     456
Trust & Safety New Associate       348
Data Engineer                      338
Business Development Manager       323
Sales Manager                      319
Java Full Stack Developer          282
Name: count, dtype: int64
print(df["location"].value_counts().head(10))
location
Bengaluru      16783
Hyderabad       7657
Pune            6096
Chennai         4418
Gurugram        4226
Mumbai          4149
Noida           2688
Remote          1952
Ahmedabad       1721
Navi Mumbai     1451
Name: count, dtype: int64
print(df["companyName"].value_counts().head(10))
companyName
Accenture                                8193
IDESLABS PRIVATE LIMITED                 2294
Wipro                                    1494
Krazy Mantra HR Solutions Pvt. Ltd       1026
PRO Hr Complete Solutions                 981
Kotak Mahindra Bank                       980
Infosys                                   937
Capgemini                                 698
IBM                                       687
PRADEEPIT CONSULTING SERVICES PVT LTD     615
Name: count, dtype: int64
print(df["currency"].value_counts().head(10))
currency
INR    97553
USD      129
Name: count, dtype: int64
print(pd.to_numeric(df["maximumSalary"].error="corece").mean())
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
print(pd.to_numeric(df["maximumSalary"].error="coerce").mean())
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
print(pd.to_numeric(df["maximumSalary"],error="coerce").mean())
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    print(pd.to_numeric(df["maximumSalary"],error="coerce").mean())
TypeError: to_numeric() got an unexpected keyword argument 'error'. Did you mean 'errors'?
print(pd.to_numeric(df["maximumSalary"],errors="coerce").mean())
318643.9803111903
salary=pd.to_numeric(df["maximumSalary"],errors="coerce")
print(
    df.assign(SalaryNum=salary)
    .groupby("title")["SalaryNum"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
title
Openings For Director (Physical design)at Hyderabad Product company    30000000.0
Chief Executive Officer - API / Pharma (Tamil Nadu/Kerala)             30000000.0
Senior Director AI ML                                                  30000000.0
Director Manufacturing Operations                                      20000000.0
COO, Rural Startup Co, Hybrid , Consulting + Startup & IIM Exp MUST    15000000.0
AVP/VP- HR                                                             15000000.0
Chief Executive Officer (Nutraceuticals / Bio Sciences)                15000000.0
Head Project Planning & Control                                        15000000.0
Urgent Requirement Medical Oncologist Doctors                          15000000.0
Interventional Cardiologist For a Hospital in Punjab                   12500000.0
Name: SalaryNum, dtype: float64
salary=pd.to_numeric(df["maximumSalary"],errors="coerce")
print(
    df.assign(SalaryNum=salary)
    .groupby("title")["SalaryNum"]
    .mean()
    .sort_values()
    .head(10)
    )
title
SAP SuccessFactors RCM/RMK Consultant                                    0.0
SAP SuccessFactors Onboarding                                            0.0
SAP SuccessFactors Integration Designer- Senior Functional Consultant    0.0
SAP SuccessFactors Employee Central Consultant                           0.0
SAP SuccessFactors EC -Implementation                                    0.0
SAP SuccessFactors Consultant(Succession & development)                  0.0
SAP SuccessFactors Consultant - EC and TimeOff                           0.0
SAP SuccessFactors Consultant                                            0.0
stibo mdm-AB PAN INDIA                                                   0.0
sous chef                                                                0.0
Name: SalaryNum, dtype: float64
salary=pd.to_numeric["maximumSalary"],errors="coerce")
SyntaxError: unmatched ')'
salary=pd.to_numeric(df["maximumSalary"],errors="coerce")
print(
    df.assign(SalaryNum=salary)
    .groupby("companyName")["SalaryNum"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    )
companyName
Cambio Consulting              30000000.0
European Company               30000000.0
Holistic Solutions India       15000000.0
Sigma Placement Consultancy    12500000.0
Smartfoodsafe India            12000000.0
Inframart Realtech India       10800000.0
Filmy Gags Media               10125000.0
Mavenhasten Consulting         10000000.0
Multiple                       10000000.0
Netfreak Digital Media         10000000.0
Name: SalaryNum, dtype: float64
salary=pd.to_numeric(df["maximumSalary"],errors="coerce")

print(df["experience"].value_counts().head(10))
experience
5-10 Yrs    6433
3-8 Yrs     5746
1-3 Yrs     3904
2-5 Yrs     3767
1-6 Yrs     3620
2-7 Yrs     3606
0-5 Yrs     3286
3-5 Yrs     3283
5-8 Yrs     3264
4-9 Yrs     2868
Name: count, dtype: int64
salary=pd.to_numeric(df["maximumSalary"],errors="coerce")
result=
SyntaxError: invalid syntax
salary=pd.to_numeric(df["maximumSalary"],errors="coerce")
result=df.assign(SalaryNum=salary).groupby("location")["SalaryNum"].mean()
print(result.sort_values(ascending=False).head(10))
location
Tamil Nadu, Kerala                                30000000.0
Kashipur, Dhanbad, Ajmer                          15000000.0
Hyderabad, Kakinada                               15000000.0
Indore, Chennai, Bengaluru                        10000000.0
Sirsa, Kolhapur, Moradabad                        10000000.0
Ambikapur, Raigarh, Raipur                        10000000.0
Jabalpur, Central African Republic, Aurangabad    10000000.0
Khambhat, Anand, Vadodara                         10000000.0
Indore, Bhandara, Durgapur                        10000000.0
Pune, Central African Republic, Vadodara           9500000.0
Name: SalaryNum, dtype: float64
print(
    df.groupby("comapnyName")["ReviewsCount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    )
Traceback (most recent call last):
  File "<pyshell#75>", line 2, in <module>
    df.groupby("comapnyName")["ReviewsCount"]
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\util\_decorators.py", line 336, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 10835, in groupby
    return DataFrameGroupBy(
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\groupby\groupby.py", line 1095, in __init__
    grouper, exclusions, obj = get_grouper(
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\groupby\grouper.py", line 901, in get_grouper
    raise KeyError(gpr)
KeyError: 'comapnyName'
print(
    df.groupby("companyName")["ReviewsCount"]
    .sum()
    .sort_values(ascending=False)
    .head(10)
    )
companyName
Accenture                    546688069.0
Wipro                         89367019.0
Infosys                       41970108.0
Capgemini                     33981436.0
Tata Consultancy Services     24440808.0
Kotak Mahindra Bank           19515556.0
IBM                           16701657.0
Axis Bank                     16328745.0
Teleperformance (TP)          11309681.0
Tech Mahindra                  8158572.0
Name: ReviewsCount, dtype: float64
ratings=pd.to_numeric("AggregateRating"],errors="coerce")
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
ratings=pd.to_numeric(df["AggregateRating"],errors="coerce")
print(ratings.mean())
3.679016907401187
ratings=pd.to_numeric(df["AggregateRating"],errors="coerce")
print(
    df.assign(Rating=ratings)
    .groupby("companyName")["Rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10))
companyName
Gkr Constructions              5.0
Echopeak Solutions             5.0
Pracemo Global Solutions       5.0
Spotmies Llp                   5.0
Spiderhit Infotech             5.0
Immigration Hotspot            5.0
Haatch Interactive             5.0
V Sparkel Welness Center       5.0
Centuria Skills Development    5.0
Ekhande Agro Fertilizers       5.0
Name: Rating, dtype: float64
print(df["tagsAndSkils"].value.counts().head(10))
  
Traceback (most recent call last):
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'tagsAndSkils'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    print(df["tagsAndSkils"].value.counts().head(10))
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'tagsAndSkils'
print(df["tagsAndSkills"].value.counts().head(10))
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    print(df["tagsAndSkills"].value.counts().head(10))
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6194, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'value'. Did you mean: 'values'?
print(df["tagsAndSkills"].value_counts().head(10))
tagsAndSkills
unknown                                                                                                                                          571
Retail,Lead generation,Forex,Investment products,Sales,Customer satisfaction,Business Development Associate,Financial services                   115
bde,cold calling,business development,business development management,financial services,corporate sales,sales,marketing                         110
Loans,Networking,Branch banking,Relationship building,Anti money laundering,Customer service,Customer engagement,Internet banking                 77
customer service,creative writing,moderation,content writing,stress analysis,digital marketing,market research,content management                 77
customer service,moderation,content writing,stress analysis,business process outsourcing,non voice process,market research,content management     74
business loan,business development,sales,marketing,direct selling,channel sales,team handling,loan against property                               58
Object Oriented technology,TOGAF,J2EE technology,OBRM,Service-Oriented Architecture,C/C++,SOA,E-TOM Architecture                                  52
Medical Coding,HCPCS,Clinical Research,CPT,Medical Transcription,CPC,ICD,Cpt Coding                                                               43
SAP ABAP,OData,SAP FICA,Adobe Forms,Smart Forms,collections,invoicing,SAP S/4HANA                                                                 42
Name: count, dtype: int64
top10=df["title"].value_counts().head(10).sum()
total=len(df)
print(round((top10/total)*100,2),"%")
6.67 %
print(df["location"].value_counts().head(5))
location
Bengaluru    16783
Hyderabad     7657
Pune          6096
Chennai       4418
Gurugram      4226
Name: count, dtype: int64
import matplotlib.pyplot as plt

top_jobs=
import matplotlib.pyplot as plt
top_jobs=df["title"].value_counts().head(10)
plt.figure(figsize=10,5))
SyntaxError: unmatched ')'
plt.figure(figsize=(10,5))
<Figure size 1000x500 with 0 Axes>
plt.bar(top_jobs.index,top_jobs.values)
<BarContainer object of 10 artists>
plt.title("Top 10 Job Titles by Job Postings")
Text(0.5, 1.0, 'Top 10 Job Titles by Job Postings')
plt.xlabel("Job Title")
Text(0.5, 0, 'Job Title')
plt.ylabel("Number of job postings")
Text(0, 0.5, 'Number of job postings')
plt.xticks(rotation=45, ha="right")
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [Text(0, 0, 'Application Developer'), Text(1, 0, 'Application Lead'), Text(2, 0, 'Sales Executive'), Text(3, 0, 'Software Development Engineer'), Text(4, 0, 'Business Development Executive'), Text(5, 0, 'Trust & Safety New Associate'), Text(6, 0, 'Data Engineer'), Text(7, 0, 'Business Development Manager'), Text(8, 0, 'Sales Manager'), Text(9, 0, 'Java Full Stack Developer')])
plt.tight_layout()
plt.show()
top_locations=df["location"].value_counts().head(10)
plt.figure(figsize=(10,5))
<Figure size 1000x500 with 0 Axes>
ptl.bar(top_location.index,top_location.values)
Traceback (most recent call last):
  File "<pyshell#108>", line 1, in <module>
    ptl.bar(top_location.index,top_location.values)
NameError: name 'ptl' is not defined
plt.bar(top_location.index,top_location.values)
Traceback (most recent call last):
  File "<pyshell#109>", line 1, in <module>
    plt.bar(top_location.index,top_location.values)
NameError: name 'top_location' is not defined. Did you mean: 'top_locations'?
plt.bar(top_locations.index,top_locations.values)
<BarContainer object of 10 artists>
plt.title("Top 10 Locations by job postings")
Text(0.5, 1.0, 'Top 10 Locations by job postings')
plt.xlabel("location")
Text(0.5, 0, 'location')
plt.ylabel("Number of job postings")
Text(0, 0.5, 'Number of job postings')
plt.xticks(rotation=45, ha="right")
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [Text(0, 0, 'Bengaluru'), Text(1, 0, 'Hyderabad'), Text(2, 0, 'Pune'), Text(3, 0, 'Chennai'), Text(4, 0, 'Gurugram'), Text(5, 0, 'Mumbai'), Text(6, 0, 'Noida'), Text(7, 0, 'Remote'), Text(8, 0, 'Ahmedabad'), Text(9, 0, 'Navi Mumbai')])
plt.tight_layout()
plt.show()

top_companies=df["companyName"].value.counts().head(10)
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    top_companies=df["companyName"].value.counts().head(10)
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 6194, in __getattr__
    return object.__getattribute__(self, name)
AttributeError: 'Series' object has no attribute 'value'. Did you mean: 'values'?
top_companies=df["companyName"].value_counts().head(10)
plt.figure(figsize=(10,5))
<Figure size 1000x500 with 0 Axes>
plt.bar(top_companies.index,top_companies.values)
<BarContainer object of 10 artists>
plt.title("Top 10 companies by job postings")
Text(0.5, 1.0, 'Top 10 companies by job postings')
plt.xlabel("company")
Text(0.5, 0, 'company')
plt.ylabel("Number of job postings")
Text(0, 0.5, 'Number of job postings')
plt.xticks(rotation=45,ha="right")
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [Text(0, 0, 'Accenture'), Text(1, 0, 'IDESLABS PRIVATE LIMITED'), Text(2, 0, 'Wipro'), Text(3, 0, 'Krazy Mantra HR Solutions Pvt. Ltd'), Text(4, 0, 'PRO Hr Complete Solutions'), Text(5, 0, 'Kotak Mahindra Bank'), Text(6, 0, 'Infosys'), Text(7, 0, 'Capgemini'), Text(8, 0, 'IBM'), Text(9, 0, 'PRADEEPIT CONSULTING SERVICES PVT LTD')])
plt.tight_layout()
plt.show()

salary=pd.to_numeric(df["maximumSalary"],errors="coerce")
top_salary_jobs=(
    df.assign(SalaryNum=salary)
    .groupby("title")["SalaryNum"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
plt.figure(figsize=(10,5))
<Figure size 1000x500 with 0 Axes>
plt.bar(top_salary_jobs.index,top_salary_jobs.values)
<BarContainer object of 10 artists>
plt.title("Top 10 Job title by average maximum salary")
Text(0.5, 1.0, 'Top 10 Job title by average maximum salary')
plt.xlabel("Job title")
Text(0.5, 0, 'Job title')
plt.ylabel("Average maximum salary")
Text(0, 0.5, 'Average maximum salary')
plt.xticks(rotation=45, ha="right")
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [Text(0, 0, 'Openings For Director (Physical design)at Hyderabad Product company'), Text(1, 0, 'Chief Executive Officer - API / Pharma (Tamil Nadu/Kerala)'), Text(2, 0, 'Senior Director AI ML'), Text(3, 0, 'Director Manufacturing Operations'), Text(4, 0, 'COO, Rural Startup Co, Hybrid , Consulting + Startup & IIM Exp MUST'), Text(5, 0, 'AVP/VP- HR'), Text(6, 0, 'Chief Executive Officer (Nutraceuticals / Bio Sciences)'), Text(7, 0, 'Head Project Planning & Control'), Text(8, 0, 'Urgent Requirement Medical Oncologist Doctors'), Text(9, 0, 'Interventional Cardiologist For a Hospital in Punjab')])
plt.tight_layout()
plt.show()

Experience=df["experience"].value_counts().head(10)
plt.figure(figsize=(10,5))
<Figure size 1000x500 with 0 Axes>
plt.bar(experience.index,experience.values)
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    plt.bar(experience.index,experience.values)
NameError: name 'experience' is not defined. Did you mean: 'Experience'?
plt.bar(Experience.index,Experience.values)
<BarContainer object of 10 artists>
plt.title("Experience")
Text(0.5, 1.0, 'Experience')
plt.title("Job postings by experience level")
Text(0.5, 1.0, 'Job postings by experience level')
plt.xlabel("Experience")
Text(0.5, 0, 'Experience')
plt.ylabel("Number of job postings")
Text(0, 0.5, 'Number of job postings')
plt.xticks(rotation=45, ha="right")
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [Text(0, 0, '5-10 Yrs'), Text(1, 0, '3-8 Yrs'), Text(2, 0, '1-3 Yrs'), Text(3, 0, '2-5 Yrs'), Text(4, 0, '1-6 Yrs'), Text(5, 0, '2-7 Yrs'), Text(6, 0, '0-5 Yrs'), Text(7, 0, '3-5 Yrs'), Text(8, 0, '5-8 Yrs'), Text(9, 0, '4-9 Yrs')])
plt.tight_layout()
plt.show()

Currency=df["currency"].value_counts().head(10)

plt.figure(figsize=(10,5))
<Figure size 1000x500 with 0 Axes>
plt.bar(Currency.index,Currency.values)
<BarContainer object of 2 artists>
plt.title("Job postings by currency")
Text(0.5, 1.0, 'Job postings by currency')
plt.xlabel("Currency")
Text(0.5, 0, 'Currency')
plt.ylable("Number of job postings")
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    plt.ylable("Number of job postings")
AttributeError: module 'matplotlib.pyplot' has no attribute 'ylable'. Did you mean: 'table'?
plt.ylabel("Number of job postings")
Text(0, 0.5, 'Number of job postings')
plt.xticks(rotation=45,ha="right")
([0, 1], [Text(0, 0, 'INR'), Text(1, 0, 'USD')])
pltplt.xticks(rotation=45)
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    pltplt.xticks(rotation=45)
NameError: name 'pltplt' is not defined

plt.xticks(rotation=45)
([0, 1], [Text(0, 0, 'INR'), Text(1, 0, 'USD')])
plt.tight_layout()
plt.show()

min_salary=pd.to_numeric(df["minimumSalary"],errors="coerce").mean()
max_salary=pd.to_numeric(df["maximumSalary"].errors="coerce").mean()
SyntaxError: expression cannot contain assignment, perhaps you meant "=="?
max_salary=pd.to_numeric(df["maximumSalary"],errors="coerce").mean()
salary_types=["Minimum Salary","Maximum Salary"]
salary_values=[min_salary,max_salary]

plt.figure(figsize=(10,5))
<Figure size 1000x500 with 0 Axes>
plt.bar(salary_types,salary_values)
<BarContainer object of 2 artists>
plt.title("Average Minimum vs Maximum Salary")
Text(0.5, 1.0, 'Average Minimum vs Maximum Salary')
plt.ylabel("Average Salary")
Text(0, 0.5, 'Average Salary')
plt.tight_layout()
plt.show()

salary = pd.to_numeric(df["maximumSalary"], errors="coerce")

company_salary = (
    df.assign(SalaryNum=salary)
      .groupby("Companyname")["SalaryNum"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)

plt.figure(figsize=(10, 5))
plt.bar(company_salary.index, company_salary.values)
plt.title("Top 10 Companies by Average Maximum Salary")
plt.xlabel("Company")
plt.ylabel("Average Maximum Salary")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
SyntaxError: multiple statements found while compiling a single statement
salary=pd.to_numeric(df["maximumSalary"],errors="coerce")
company_salary =(
    df.assign(SalaryNum=salary)
    .groupby("Companyname")["SalaryNum"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    )
Traceback (most recent call last):
  File "<pyshell#195>", line 3, in <module>
    .groupby("Companyname")["SalaryNum"]
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\util\_decorators.py", line 336, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 10835, in groupby
    return DataFrameGroupBy(
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\groupby\groupby.py", line 1095, in __init__
    grouper, exclusions, obj = get_grouper(
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\groupby\grouper.py", line 901, in get_grouper
    raise KeyError(gpr)
KeyError: 'Companyname'
company_salary =(
    df.assign(SalaryNum=salary)
    .groupby("CompanyName")["SalaryNum"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    )
Traceback (most recent call last):
  File "<pyshell#196>", line 3, in <module>
    .groupby("CompanyName")["SalaryNum"]
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\util\_decorators.py", line 336, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 10835, in groupby
    return DataFrameGroupBy(
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\groupby\groupby.py", line 1095, in __init__
    grouper, exclusions, obj = get_grouper(
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\groupby\grouper.py", line 901, in get_grouper
    raise KeyError(gpr)
KeyError: 'CompanyName'
company_salary =(
    df.assign(SalaryNum=salary)
    .groupby("companyName")["SalaryNum"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
    )
plt.figure(figsize=(10, 5))
<Figure size 1000x500 with 0 Axes>
KeyboardInterrupt
plt.bar(company_salary.index, company_salary.values)
<BarContainer object of 10 artists>
plt.title("Top 10 Companies by Average Maximum Salary")
Text(0.5, 1.0, 'Top 10 Companies by Average Maximum Salary')
plt.xlabel("Company")
Text(0.5, 0, 'Company')
plt.ylabel("Average Maximum Salary")
Text(0, 0.5, 'Average Maximum Salary')
plt.xticks(rotation=45, ha="right")
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [Text(0, 0, 'Cambio Consulting'), Text(1, 0, 'European Company'), Text(2, 0, 'Holistic Solutions India'), Text(3, 0, 'Sigma Placement Consultancy'), Text(4, 0, 'Smartfoodsafe India'), Text(5, 0, 'Inframart Realtech India'), Text(6, 0, 'Filmy Gags Media'), Text(7, 0, 'Mavenhasten Consulting'), Text(8, 0, 'Multiple'), Text(9, 0, 'Netfreak Digital Media')])
plt.tight_layout()
plt.show()
rating = pd.to_numeric(df["AggregateRating"], errors="coerce")


company_rating = (
    df.assign(Rating=rating)
      .groupby("Companyname")["Rating"]
      .mean()
      .sort_values(ascending=False)
      .head(10)
)


plt.figure(figsize=(10, 5))
plt.bar(company_rating.index, company_rating.values)
plt.title("Top 10 Companies by Average Rating")
plt.xlabel("Company")
plt.ylabel("Average Rating")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
  
SyntaxError: multiple statements found while compiling a single statement
rating = pd.to_numeric(df["AggregateRating"], errors="coerce")
company_rating = (
    df.assign(Rating=rating)
    .groupby("Companyname")["Rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
Traceback (most recent call last):
  File "<pyshell#214>", line 3, in <module>
    .groupby("Companyname")["Rating"]
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\util\_decorators.py", line 336, in wrapper
    return func(*args, **kwargs)
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 10835, in groupby
    return DataFrameGroupBy(
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\groupby\groupby.py", line 1095, in __init__
    grouper, exclusions, obj = get_grouper(
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\groupby\grouper.py", line 901, in get_grouper
    raise KeyError(gpr)
KeyError: 'Companyname'
company_rating = (
    df.assign(Rating=rating)
    .groupby("companyName")["Rating"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)
plt.figure(figsize=(10, 5))
<Figure size 1000x500 with 0 Axes>
plt.bar(company_rating.index, company_rating.values)
<BarContainer object of 10 artists>
plt.title("Top 10 Companies by Average Rating")
Text(0.5, 1.0, 'Top 10 Companies by Average Rating')
plt.xlabel("Company")
Text(0.5, 0, 'Company')
plt.ylabel("Average Rating")
Text(0, 0.5, 'Average Rating')
KeyboardInterrupt
plt.xticks(rotation=45, ha="right")
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [Text(0, 0, 'Gkr Constructions'), Text(1, 0, 'Echopeak Solutions'), Text(2, 0, 'Pracemo Global Solutions'), Text(3, 0, 'Spotmies Llp'), Text(4, 0, 'Spiderhit Infotech'), Text(5, 0, 'Immigration Hotspot'), Text(6, 0, 'Haatch Interactive'), Text(7, 0, 'V Sparkel Welness Center'), Text(8, 0, 'Centuria Skills Development'), Text(9, 0, 'Ekhande Agro Fertilizers')])
plt.tight_layout()
plt.show()
skills = (
    df["Tag and skills"]
      .fillna("")
      .str.split(",")
      .explode()
      .str.strip()
      .str.lower()
)

top_skills = skills[skills != ""].value_counts().head(10)

plt.figure(figsize=(10, 5))
plt.bar(top_skills.index, top_skills.values)
plt.title("Top 10 Skills in Job Postings")
plt.xlabel("Skill")
plt.ylabel("Number of Job Postings")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()
  
SyntaxError: multiple statements found while compiling a single statement
skills = (
    df["Tag and skills"]
    .fillna("")
    .str.split(",")
    .explode()
    .str.strip()
    .str.lower()
)
Traceback (most recent call last):
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Tag and skills'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#232>", line 2, in <module>
    df["Tag and skills"]
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Tag and skills'
skills = (
    df["tagsAndSkills"]
    .fillna("")
    .str.split(",")
    .explode()
    .str.strip()
    .str.lower()
)
plt.figure(figsize=(10, 5))
<Figure size 1000x500 with 0 Axes>
plt.bar(top_skills.index, top_skills.values)
Traceback (most recent call last):
  File "<pyshell#235>", line 1, in <module>
    plt.bar(top_skills.index, top_skills.values)
NameError: name 'top_skills' is not defined
top_skills = skills[skills != ""].value_counts().head(10)
plt.bar(top_skills.index, top_skills.values)
<BarContainer object of 10 artists>
plt.title("Top 10 Skills in Job Postings")
Text(0.5, 1.0, 'Top 10 Skills in Job Postings')
plt.xlabel("Skill")
Text(0.5, 0, 'Skill')
plt.ylabel("Number of Job Postings")
Text(0, 0.5, 'Number of Job Postings')
plt.xticks(rotation=45, ha="right")
([0, 1, 2, 3, 4, 5, 6, 7, 8, 9], [Text(0, 0, 'sales'), Text(1, 0, 'python'), Text(2, 0, 'project management'), Text(3, 0, 'customer service'), Text(4, 0, 'sap'), Text(5, 0, 'management'), Text(6, 0, 'css'), Text(7, 0, 'java'), Text(8, 0, 'sql'), Text(9, 0, 'business development')])
plt.tight_layout()
plt.show()


import pandas as pd

min_salary = pd.to_numeric(df["minimumsalary"], errors="coerce")
max_salary = pd.to_numeric(df["maximumSalary"], errors="coerce")
rating = pd.to_numeric(df["AggregateRating"], errors="coerce")

print("========== JOB MARKET KPIs ==========")

print("Total Job Postings:", len(df))
print("Unique Companies:", df["Companyname"].nunique())
print("Unique Job Titles:", df["title"].nunique())

print("Average Minimum Salary:", round(min_salary.mean(), 2))
print("Average Maximum Salary:", round(max_salary.mean(), 2))

print("Average Company Rating:", round(rating.mean(), 2))

print("Top Job Title:", df["title"].value_counts().idxmax())
print("Top Location:", df["Location"].value_counts().idxmax())
print("Top Company:", df["Companyname"].value_counts().idxmax())
SyntaxError: multiple statements found while compiling a single statement
import pandas as pd
min_salary = pd.to_numeric(df["minimumsalary"], errors="coerce")
Traceback (most recent call last):
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'minimumsalary'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#248>", line 1, in <module>
    min_salary = pd.to_numeric(df["minimumsalary"], errors="coerce")
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'minimumsalary'
import pandas as pd
min_salary = pd.to_numeric(df["minimumSalary"], errors="coerce")
max_salary = pd.to_numeric(df["maximumSalary"], errors="coerce")
rating = pd.to_numeric(df["AggregateRating"], errors="coerce")

print("========== JOB MARKET KPIs ==========")
========== JOB MARKET KPIs ==========
print("Total Job Postings:", len(df))
Total Job Postings: 97682
print("Unique Companies:", df["companyName"].nunique())
Unique Companies: 18669
print("Unique Job Titles:", df["title"].nunique())
Unique Job Titles: 55104
print("Average Minimum Salary:", round(min_salary.mean(), 2))
Average Minimum Salary: 198325.87
print("Average Maximum Salary:", round(max_salary.mean(), 2))
Average Maximum Salary: 318643.98
print("Top Job Title:", df["title"].value_counts().idxmax())
Top Job Title: Application Developer
print("Top Location:", df["Location"].value_counts().idxmax())
Traceback (most recent call last):
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3641, in get_loc
    return self._engine.get_loc(casted_key)
  File "pandas/_libs/index.pyx", line 168, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/index.pyx", line 197, in pandas._libs.index.IndexEngine.get_loc
  File "pandas/_libs/hashtable_class_helper.pxi", line 7668, in pandas._libs.hashtable.PyObjectHashTable.get_item
  File "pandas/_libs/hashtable_class_helper.pxi", line 7676, in pandas._libs.hashtable.PyObjectHashTable.get_item
KeyError: 'Location'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "<pyshell#261>", line 1, in <module>
    print("Top Location:", df["Location"].value_counts().idxmax())
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\frame.py", line 4378, in __getitem__
    indexer = self.columns.get_loc(key)
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\indexes\base.py", line 3648, in get_loc
    raise KeyError(key) from err
KeyError: 'Location'
print("Top Location:", df["location"].value_counts().idxmax())
Top Location: Bengaluru
print("Top Company:", df["companyName"].value_counts().idxmax())
Top Company: Accenture
df.to_excel("C:Users/Manoj/Downloads/cleaned_idian_jon_market.xlsx", index=False)
Traceback (most recent call last):
  File "<pyshell#264>", line 1, in <module>
    df.to_excel("C:Users/Manoj/Downloads/cleaned_idian_jon_market.xlsx", index=False)
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 2300, in to_excel
    formatter.write(
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\formats\excel.py", line 1003, in write
    writer = ExcelWriter(
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\excel\_openpyxl.py", line 62, in __init__
    super().__init__(
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\excel\_base.py", line 1281, in __init__
    self._handles = get_handle(
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\common.py", line 797, in get_handle
    check_parent_directory(str(handle))
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\common.py", line 656, in check_parent_directory
    raise OSError(rf"Cannot save file into a non-existent directory: '{parent}'")
OSError: Cannot save file into a non-existent directory: 'C:Users\Manoj\Downloads'
>>> import os
>>> print(os.path.expanduser("~"))
C:\Users\Administrator
>>> import os
>>> save_path=os.path.join(
...     os.path.expanduser("~"),
...     "Desktop",
...     "cleaned_indian_job_market.xlsx")
>>> df.to_excel(save_path, index=False)
Traceback (most recent call last):
  File "<pyshell#272>", line 1, in <module>
    df.to_excel(save_path, index=False)
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\core\generic.py", line 2300, in to_excel
    formatter.write(
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\formats\excel.py", line 1003, in write
    writer = ExcelWriter(
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\excel\_openpyxl.py", line 62, in __init__
    super().__init__(
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\excel\_base.py", line 1281, in __init__
    self._handles = get_handle(
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\common.py", line 797, in get_handle
    check_parent_directory(str(handle))
  File "C:\Users\Administrator\AppData\Local\Python\pythoncore-3.14-64\Lib\site-packages\pandas\io\common.py", line 656, in check_parent_directory
    raise OSError(rf"Cannot save file into a non-existent directory: '{parent}'")
OSError: Cannot save file into a non-existent directory: 'C:\Users\Administrator\Desktop'
>>> import as os
SyntaxError: invalid syntax
>>> import os
>>> 
>>> save_path=os.path.join(os.getcwd( ),
...  "cleaned_indian_job_market.xlsx")
>>> df.to_excel(save_path, index=False)

... print("Saved successfully at:", save_path)
... 
... 
>>> print(save_path)
C:\Users\Administrator\OneDrive\Documents\cleaned_indian_job_market.xlsx
>>> import os
>>> print(os.path.exists(save_path))
True
