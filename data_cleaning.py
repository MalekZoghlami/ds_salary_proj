import pandas as pd

df= pd.read_csv('glassdor_jobs.csv')

#salary parsing

# df['hourly'] = df['Salary Estimate'].apply(lambda x: 1 if 'per hour' in x.lower()else 0)
# df['employer_provided'] = df['Salary Estimate'].apply(lambda x: 1 if 'employer provided salary:' in x.lower()else 0)

df=df[df['Salary Estimate']!= '-1'].reset_index()
df.drop(['index', 'Unnamed: 0'], axis=1, inplace=True)


salary= df['Salary Estimate'].apply(lambda x: x.split('(')[0])
minus_k_d= salary.apply(lambda x :x.replace('K','').replace('$',''))

#minus_hr= minus_kd.apply(lambda x : x.lower(.replace('per hour','').replace('employer provided salary:',''))

df['min_slary']= minus_k_d.apply( lambda x: int(x.split('-')[0] ))
df['max_slary']= minus_k_d.apply( lambda x: int(x.split('-')[1] ))
df['avg_slary']= (df.min_slary+df.max_slary)/2

#company name text only
df['company_txt'] = df.apply(lambda x: x ['Company Name'] if x['Rating']<0 else x ['Company Name'][:-3], axis=1)

#state field
df['job_state']= df['Location'].apply( lambda x: x.split(',')[1] if ',' in x else x)
df.job_state.value_counts()

df.columns
df.drop( ['Competitors','Headquarters'],axis=1, inplace=True)

#age of company
df['age']=df.Founded.apply(lambda x: x if x<0 else 2020-x)

#parsing of jov decription python
df['Job Description'][0]
#python
df['python_yn']= df['Job Description'].apply(lambda x: 1 if 'python' in x.lower() else 0)
#df.python_yn.value_counts()
#spark
df['spark_yn']= df['Job Description'].apply(lambda x: 1 if 'spark' in x.lower() else 0)
df.spark_yn.value_counts()
#aws
df['aws_yn']= df['Job Description'].apply(lambda x: 1 if 'aws' in x.lower() else 0)
df.aws_yn.value_counts()
#excel
df['excel_yn']= df['Job Description'].apply(lambda x: 1 if 'excel' in x.lower() else 0)
df.excel_yn.value_counts()


df.to_csv('salary_data_cleaned.csv', index= False)
