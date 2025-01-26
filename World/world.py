# Import Libraries 
import pandas as pd #used for data manipulation and analysis 
import numpy as np #used for numerical operations
import matplotlib.pyplot as plt 
import seaborn as sns 

individuals_using_internet = open("World/individuals_using_internet.csv", "r")
individuals_using_internet.read()

fixed_broadband_subscriptions= open("World/fixed_broadband_subscriptions.csv", "r")
fixed_broadband_subscriptions.read()

mobile_data_and_voice_low_consumption_baskets = open("World/mobile_data_and_voice_low_consumption_basket.csv", "r")
mobile_data_and_voice_low_consumption_baskets.read()

broadband_services_are_part_of_universal_service_access_scheme = open("World/broadband_services_are_part_of_universal_service_access_scheme.csv", "r")
broadband_services_are_part_of_universal_service_access_scheme.read()

regulatory_authority_decision_making = open("World/regulatory_authority_decision_making.csv", "r")
regulatory_authority_decision_making.read()

level_of_competition = open("World/level_of_competition.csv", "r")
level_of_competition.read()

digital_development_strategies = open("World/digital_development_strategies.csv", "r")
digital_development_strategies.read()


publicly_available_information = open("World/publicly_available_information.csv", "r")
publicly_available_information.read()

taxation_policies = open("World/taxation_policies.csv", "r")
taxation_policies.read()

cybersecurity_framework_and_mandates = open("World/cybersecurity_framework_and_mandates.csv", "r")
cybersecurity_framework_and_mandates.read()

# Scatterplot Showing Relation Between The Series Name & the Entity Name 

final_df = pd.read_csv('World/cybersecurity_framework_and_mandates.csv')
series_count_df = final_df.groupby('seriesName')['entityName'].nunique().reset_index()
series_count_df.columns = ['seriesName', 'CountryCount']

sns.set(style='whitegrid')
plt.figure(figsize = (10,6))
sns.barplot(
    series_count_df, 
    x = 'seriesName',
    y = 'CountryCount',
    hue = 'seriesName', 
    palette = 'Set2',
    legend = False)
plt.title('Number of Countries in Each Cybersecurity Policy Category')
plt.xlabel('Cybersecurity Policy Series', fontsize = 12)
plt.ylabel('Number of Countries', fontsize = 12)
plt.tight_layout()
plt.show()








