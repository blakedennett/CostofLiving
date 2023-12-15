import polars as pl
import plotly.express as px
import streamlit as st

apt = pl.read_csv(r'C:\Users\Blake Dennett\Downloads\CostofLiving\apartment.csv')
car_sales = pl.read_csv(r'C:\Users\Blake Dennett\Downloads\CostofLiving\car_sales_tax.csv')
food = pl.read_csv(r'C:\Users\Blake Dennett\Downloads\CostofLiving\food.csv')
heal_ins = pl.read_csv(r'C:\Users\Blake Dennett\Downloads\CostofLiving\health_insurance.csv')
sq_f = pl.read_csv(r'C:\Users\Blake Dennett\Downloads\CostofLiving\house_square_footage.csv')
homes = pl.read_csv(r'C:\Users\Blake Dennett\Downloads\CostofLiving\houses.csv')
income_tax = pl.read_csv(r'C:\Users\Blake Dennett\Downloads\CostofLiving\income_tax.csv')
income = pl.read_csv(r'C:\Users\Blake Dennett\Downloads\CostofLiving\income.csv')
auto = pl.read_csv(r'C:\Users\Blake Dennett\Downloads\CostofLiving\insurance.csv')
sales_tax = pl.read_csv(r'C:\Users\Blake Dennett\Downloads\CostofLiving\sales_tax.csv')
property_tax = pl.read_csv(r'C:\Users\Blake Dennett\Downloads\CostofLiving\property_tax.csv')

names = pl.read_csv('https://raw.githubusercontent.com/blakedennett/LoanApprovalProject/main/data/fips2county.tsv', separator='\t') \
        .select('StateName', 'StateAbbr') \
        .unique(subset=["StateName","StateAbbr"]) \
        .rename({'StateName':'state', 'StateAbbr':'state_abbr'})
names.limit(3)

df = apt.join(car_sales, on='state', how='inner') \
        .join(heal_ins, on='state', how='inner') \
        .join(sq_f, on='state', how='inner') \
        .join(homes, on='state', how='inner') \
        .join(income_tax, on='state', how='inner') \
        .join(income, on='state', how='inner') \
        .join(auto, on='state', how='inner') \
        .join(sales_tax, on='state', how='inner') \
        .join(names, on='state', how='inner') \
        .join(property_tax, on='state', how='inner')


conv = {'Apartment Size':'Average_Apartment_Size', 'Rent':'Average_Rent','Car Sales Tax':'car_sales_tax',
        'Health Insurance':'health_insurance_yearly_avg','Home Size':'avg_home_sq_feet',
        'Home Price per Square Foot':'median_home_price_per_square_foot','House Prices':'house_price',
        'Income Tax':'income_tax','Income':'income_2021','Property Tax':'annual_property_tax_median_value',
        'Full Auto Insurance':'auto_insurance_full','Minimum Auto Insurance':'auto_insurance_minimum',
        'Sales Tax':'State_Tax_Rate'}

options = []
for key, value in conv.items():
    options.append(key)


feature = st.selectbox("Select a feature", options=(options))

named_colorscales = px.colors.named_colorscales()

# color = st.selectbox("Select a feature", options=(named_colorscales))

fig = px.choropleth(df, locations="state_abbr",
                    color=conv[feature],
                    hover_name="state",
                    locationmode='USA-states',
                    color_continuous_scale=px.colors.sequential.Oranges,
                    scope="usa")

fig.update_layout(
    geo_scope='usa'
)

st.plotly_chart(fig)