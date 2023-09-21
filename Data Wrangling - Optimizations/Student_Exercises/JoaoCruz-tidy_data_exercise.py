#Import
import pandas as pd

# Load dataset from seaborn
base_url = "https://github.com/byuidatascience/data4python4ds/raw/master/data-raw/"
table1 = pd.read_csv("{}table1/table1.csv".format(base_url))
table2 = pd.read_csv("{}table2/table2.csv".format(base_url))
table3 = pd.read_csv("{}table3/table3.csv".format(base_url))
table4a = pd.read_csv("{}table4a/table4a.csv".format(base_url))
table4b = pd.read_csv("{}table4b/table4b.csv".format(base_url))
table5 = pd.read_csv("{}table5/table5.csv".format(base_url), dtype = 'object')

# Table 2
print("Table 2\n", table2)
table2_pivot = table2.pivot_table(
    index=["country", "year"], #The values we do not want to change
    columns= "type", #the columns with the values that we want to form a new column out of
    values="count" #the values of the new columns
).reset_index() #remove the index
print("Table 2 tidy")
print(table2_pivot)

# Table 3
print("Table 2\n", table3)
new_columns = table3.rate.str.split("/", expand=True).rename(columns={0: "cases", 1: "population"}) #somehow expand=True converts the array into a dataframe
table3_split = pd.concat([table3.drop(columns="rate"), new_columns], axis=1)
print("Table 3 tidy")
print(table3_split)

# Tables 4
print("Table 4a\n", table4a)
print("Table 4b\n",table4b)

new_colums_a = table4a.melt(id_vars=["country"], var_name="year", value_name="cases")
new_colums_b = table4b.melt(id_vars=["country"], var_name="year", value_name="population")

print("Table 4 tidy")
print(new_colums_a.set_index(["country", "year"]).join(new_colums_b.set_index(["country", "year"]), how="inner").reset_index())

# Table 5
print("Table 5\n",table5)
cent_year = pd.DataFrame(table5["century"] + table5["year"]).rename(columns={0: "year"})
new_columns_5 = table5.rate.str.split("/", expand=True).rename(columns={0:"cases", 1:"population"})

tidy_table5 = pd.concat([table5.drop(columns=["rate", "century", "year"]), cent_year, new_columns_5], axis=1)
print("Table 5 tidy\n", tidy_table5)











