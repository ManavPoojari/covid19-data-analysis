# Project: COVID-19 Data Analysis and Visualization
# Author: Manav Poojari

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:\\Users\\Manav\\Downloads\\archive (1)\\covid_19_data.csv")

# Show first 5 rows
print("Top 5 rows of the dataset:")
print(df.head())

# Rename columns
df.rename(columns={
    'ObservationDate': 'Date',
    'Country/Region': 'Country',
    'Province/State': 'State'
}, inplace=True)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Fill missing values
df['Recovered'] = df['Recovered'].fillna(0)
df['State'] = df['State'].fillna("")

# Group by Date and Country
grouped = df.groupby(['Date', 'Country'])[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()

# Get latest date
latest_date = grouped['Date'].max()

# Filter data for latest date
latest_data = grouped[grouped['Date'] == latest_date]

# Get top 5 countries by confirmed cases
top_countries = latest_data.sort_values(by='Confirmed', ascending=False).head(5)['Country'].tolist()

# Plot confirmed cases over time for top 5 countries
plt.figure(figsize=(12, 6))
for country in top_countries:
    country_data = grouped[grouped['Country'] == country]
    plt.plot(country_data['Date'], country_data['Confirmed'], label=country)

plt.title('COVID-19 Confirmed Cases Over Time (Top 5 Countries)')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Get top 10 countries by confirmed cases
top10_latest = latest_data.sort_values(by='Confirmed', ascending=False).head(10)

# Plot deaths vs recovered# Project: COVID-19 Data Analysis and Visualization
# Author: Manav Poojari

# Import required libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("C:\\Users\\Manav\\Downloads\\archive (1)\\covid_19_data.csv")

# Show first 5 rows
print("Top 5 rows of the dataset:")
print(df.head())

# Rename columns
df.rename(columns={
    'ObservationDate': 'Date',
    'Country/Region': 'Country',
    'Province/State': 'State'
}, inplace=True)

# Convert 'Date' column to datetime
df['Date'] = pd.to_datetime(df['Date'])

# Fill missing values
df['Recovered'] = df['Recovered'].fillna(0)
df['State'] = df['State'].fillna("")

# Group by Date and Country
grouped = df.groupby(['Date', 'Country'])[['Confirmed', 'Deaths', 'Recovered']].sum().reset_index()

# Get latest date
latest_date = grouped['Date'].max()

# Filter data for latest date
latest_data = grouped[grouped['Date'] == latest_date]

# Get top 5 countries by confirmed cases
top_countries = latest_data.sort_values(by='Confirmed', ascending=False).head(5)['Country'].tolist()

# Plot confirmed cases over time for top 5 countries
plt.figure(figsize=(12, 6))
for country in top_countries:
    country_data = grouped[grouped['Country'] == country]
    plt.plot(country_data['Date'], country_data['Confirmed'], label=country)

plt.title('COVID-19 Confirmed Cases Over Time (Top 5 Countries)')
plt.xlabel('Date')
plt.ylabel('Confirmed Cases')
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()
plt.show()

# Get top 10 countries by confirmed cases
top10_latest = latest_data.sort_values(by='Confirmed', ascending=False).head(10)

# Plot deaths vs recovered
plt.figure(figsize=(10, 6))
plt.bar(top10_latest['Country'], top10_latest['Deaths'], label='Deaths', color='red')
plt.bar(top10_latest['Country'], top10_latest['Recovered'], bottom=top10_latest['Deaths'], label='Recovered', color='green')
plt.title('Deaths and Recoveries by Country (Latest Date)')
plt.ylabel('Count')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calculate mortality rate
top10_latest['MortalityRate'] = (top10_latest['Deaths'] / top10_latest['Confirmed']) * 100

# Plot mortality rate
plt.figure(figsize=(10, 6))
sns.barplot(x='MortalityRate', y='Country', data=top10_latest.sort_values('MortalityRate', ascending=False), palette='magma')
plt.title('Top 10 Countries by COVID-19 Mortality Rate')
plt.xlabel('Mortality Rate (%)')
plt.tight_layout()
plt.show()

# Save final summary to CSV
top10_latest.to_csv('covid_final_summary.csv', index=False)
print("Final summary saved as 'covid_final_summary.csv'")

plt.figure(figsize=(10, 6))
plt.bar(top10_latest['Country'], top10_latest['Deaths'], label='Deaths', color='red')
plt.bar(top10_latest['Country'], top10_latest['Recovered'], bottom=top10_latest['Deaths'], label='Recovered', color='green')
plt.title('Deaths and Recoveries by Country (Latest Date)')
plt.ylabel('Count')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# Calculate mortality rate
top10_latest['MortalityRate'] = (top10_latest['Deaths'] / top10_latest['Confirmed']) * 100

# Plot mortality rate
plt.figure(figsize=(10, 6))
sns.barplot(x='MortalityRate', y='Country', data=top10_latest.sort_values('MortalityRate', ascending=False), palette='magma')
plt.title('Top 10 Countries by COVID-19 Mortality Rate')
plt.xlabel('Mortality Rate (%)')
plt.tight_layout()
plt.show()

# Save final summary to CSV
top10_latest.to_csv('covid_final_summary.csv', index=False)
print("Final summary saved as 'covid_final_summary.csv'")