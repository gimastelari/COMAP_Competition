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
bplot = sns.barplot(
    series_count_df, 
    x = 'seriesName',
    y = 'CountryCount',
    hue = 'seriesName', 
    palette = 'Set2')

plt.title('Number of Countries in Each Cybersecurity Policy Category')
plt.xlabel('Cybersecurity Policy Series', fontsize = 8)
plt.ylabel('Number of Countries', fontsize = 12)

plt.xticks(fontsize=8)
plt.xticks(rotation=10) 
plt.show()

regions_countries = {
    "Africa": [
        "Angola", "Benin", "Botswana", "Burkina Faso", "Burundi", "Cameroon", "Cabo Verde", 
        "Central African Rep.", "Chad", "Congo (Rep. of the)", "Côte d'Ivoire", 
        "Dem. Rep. of the Congo)", "Equatorial Guinea", "Eritrea", "Eswatini", "Ethiopia", 
        "Gabon", "Gambia", "Ghana", "Guinea", "Guinea-Bissau", "Kenya", "Lesotho", 
        "Liberia", "Madagascar", "Malawi", "Mali", "Mauritius", "Mozambique", 
        "Namibia", "Niger", "Nigeria", "Rwanda", "Sao Tome and Principe", "Senegal", 
        "Seychelles", "Sierra Leone", "South Africa", "South Sudan", "Tanzania", 
        "Togo", "Uganda", "Zambia", "Zimbabwe"
    ],
    "The Americas": [
        "Antigua and Barbuda", "Argentina", "Bahamas", "Barbados", "Belize", 
        "Bolivia (Plurinational State of)", "Brazil", "Canada", "Chile", "Colombia", 
        "Costa Rica", "Cuba", "Dominica", "Dominican Rep.", "Ecuador", "El Salvador", 
        "Grenada", "Guatemala", "Guyana", "Haiti", "Honduras", "Jamaica", "Mexico", 
        "Nicaragua", "Panama", "Paraguay", "Peru", "Saint Kitts and Nevis", 
        "Saint Lucia", "Saint Vincent and the Grenadines", "Suriname", 
        "Trinidad and Tobago", "United States", "Uruguay", "Venezuela"
    ],
    "Arab States": [
        "Algeria", "Bahrain", "Comoros", "Djibouti", "Egypt", "Iraq", "Jordan", 
        "Kuwait", "Lebanon", "Libya", "Mauritania", "Morocco", "Oman", "Palestine*", 
        "Qatar", "Saudi Arabia", "Somalia", "Sudan", "Syrian Arab Republic", 
        "Tunisia", "United Arab Emirates", "Yemen"
    ],
    "Asia and the Pacific": [
        "Afghanistan", "Australia", "Bangladesh", "Bhutan", "Brunei Darussalam", 
        "Cambodia", "China", "Dem. People’s Rep. of Korea", "Fiji", "Hong Kong, China​", 
        "India", "Indonesia", "Iran (Islamic Republic of)", "Japan", "Kiribati", 
        "Korea (Rep. of)", "Lao P.D.R", "Macao, China", "Malaysia", "Maldives", 
        "Marshall Islands", "Micronesia", "Mongolia", "Myanmar", "Nauru", 
        "Nepal (Republic of)", "New Zealand", "Pakistan", "Palau​", "Papua New Guinea", 
        "Philippines", "Samoa", "Singapore", "Solomon Islands", "Sri Lanka", 
        "Thailand", "Timor-Leste", "Tonga", "Tuvalu", "Vanuatu", "Viet Nam"
    ],
    "CIS": [
        "Armenia", "Azerbaijan", "Belarus", "Kazakhstan", "Kyrgyzstan", 
        "Russian Federation", "Tajikistan", "Turkmenistan", "Uzbekistan"
    ],
    "Europe": [
        "Albania", "Andorra", "Austria", "Belgium", "Bosnia and Herzegovina", 
        "Bulgaria", "Croatia", "Cyprus", "Czech Republic", "Denmark", "Estonia", 
        "Finland", "France", "Georgia", "Germany", "Greece", "Hungary", "Iceland", 
        "Ireland", "Israel", "Italy", "Latvia", "Liechtenstein", "Lithuania", 
        "Luxembourg", "Malta", "Moldova", "Monaco​", "Montenegro", 
        "Netherlands (Kingdom of the)", "North Macedonia​", "Norway", "Poland", 
        "Portugal", "Romania", "San Marino", "Serbia", "Slovakia", "Slovenia", 
        "Spain", "Sweden", "Switzerland", "Türkiye​", "Ukraine", "United Kingdom", 
        "Vatican"
    ]
}

policy_data = {
    Countru 

}





