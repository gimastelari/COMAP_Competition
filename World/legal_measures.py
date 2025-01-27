# Import Libraries 
import pandas as pd #used for data manipulation and analysis 
import numpy as np #used for numerical operations
import matplotlib.pyplot as plt 
import seaborn as sns 

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

df = pd.read_csv('World/cybersecurity_framework_and_mandates.csv')

regulations = [
    "ICT regulator have a cybersecurity mandate", 
    "Cybersecurity legislation/regulation exist", 
    "Areas covered", 
    "Specific requirements to operators and service providers", 
    "Requirements to operators and service providers (e.g., cybersecurity, online safety)"
]
df_filtered = df[df['seriesName'].isin(regulations)]

region_map = {
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

region_dict = {country: region for region, countries in region_map.items() for country in countries}

df_filtered['Region'] = df_filtered["entityName"].map(region_dict)

compliance_counts = df_filtered.groupby(["Region", "seriesName"]).size().unstack(fill_value=0)

compliance_percentage = compliance_counts.div(compliance_counts.sum(axis=1), axis=0) * 100

ax = compliance_percentage.plot(kind="bar", stacked = True, figsize = (14,8), width=0.7, cmap="tab20")

for i, bar in enumerate(ax.patches): 
    height = bar.get_height() 
    if height > 0: 
        x = bar.get_x() + bar.get_width() / 2
        y = bar.get_y() + height / 2
        ax.text(
            x, y, 
            f"{height: .1f}%", 
            ha='center', 
            va='center', 
            fontsize=9, 
            color="white",
            weight="bold"
        )


plt.title("Compliance with Cybersecurity Regulations by Region", fontsize=16)
plt.xlabel("Region", fontsize=14)
plt.ylabel("Percentage of Countries", fontsize=14)
plt.xticks(rotation=45, ha = "right", fontsize=10)
plt.legend(
    title="Regulations", 
    bbox_to_anchor=(1.05, 1), 
    loc='upper left', 
    fontsize=9
)
plt.grid(axis='y', linestyle="--", linewidth=0.5, alpha=0.7)
plt.tight_layout()
plt.show()



vcdb1 = open("Incidents/vcdb_1.csv", "r")
vcdb2 = open("Incidents/vcdb_1.csv", "r")
vcdb1.read()
vcdb2.read()

vcdb1_df = pd.read_csv("Incidents/vcdb_1.csv", low_memory=False)
vcdb2_df = pd.read_csv("Incidents/vcdb_2.csv", low_memory=False)
vcdb = pd.concat([vcdb1_df, vcdb2_df], ignore_index = True)


region_mapping_for_iso_codes = {
    "Africa": [
        "victim.country.AO", "victim.country.BJ", "victim.country.BW", 
        "victim.country.BF", "victim.country.BI", "victim.country.CM",
        "victim.country.CV", "victim.country.TD", "victim.country.CG",
        "victim.country.CI", "victim.country.CD", "victim.country.GQ",
        "victim.country.ER", "victim.country.SZ", "victim.country.ET",
        "victim.country.GA", "victim.country.GM", "victim.country.GH",
        "victim.country.GN", "victim.country.GW", "victim.country.KE",
        "victim.country.LS", "victim.country.LR", "victim.country.MG",
        "victim.country.MW", "victim.country.ML", "victim.country.MU",
        "victim.country.MZ", "victim.country.NA", "victim.country.NE",
        "victim.country.NG", "victim.country.RW", "victim.country.ST",
        "victim.country.SN", "victim.country.SC", "victim.country.SL",
        "victim.country.SO", "victim.country.ZA", "victim.country.SS",
        "victim.country.TZ", "victim.country.TG", "victim.country.UG",
        "victim.country.ZM", "victim.country.ZW"
    ],
    "The Americas": [
        "victim.country.AG", "victim.country.AR", "victim.country.BS",
        "victim.country.BB", "victim.country.BZ", "victim.country.BO",
        "victim.country.BR", "victim.country.CA", "victim.country.CL",
        "victim.country.CO", "victim.country.CR", "victim.country.CU",
        "victim.country.DM", "victim.country.DO", "victim.country.EC",
        "victim.country.SV", "victim.country.GD", "victim.country.GT",
        "victim.country.GY", "victim.country.HT", "victim.country.HN",
        "victim.country.JM", "victim.country.MX", "victim.country.NI",
        "victim.country.PA", "victim.country.PY", "victim.country.PE",
        "victim.country.KN", "victim.country.LC", "victim.country.VC",
        "victim.country.SR", "victim.country.TT", "victim.country.US",
        "victim.country.UY", "victim.country.VE"
    ],
    "Arab States": [
        "victim.country.DZ", "victim.country.BH", "victim.country.KM",
        "victim.country.DJ", "victim.country.EG", "victim.country.IQ",
        "victim.country.JO", "victim.country.KW", "victim.country.LB",
        "victim.country.LY", "victim.country.MR", "victim.country.MA",
        "victim.country.OM", "victim.country.PS", "victim.country.QA",
        "victim.country.SA", "victim.country.SO", "victim.country.SD",
        "victim.country.SY", "victim.country.TN", "victim.country.AE",
        "victim.country.YE"
    ],
    "Asia and the Pacific": [
        "victim.country.AF", "victim.country.AU", "victim.country.BD",
        "victim.country.BT", "victim.country.BN", "victim.country.KH",
        "victim.country.CN", "victim.country.KP", "victim.country.FJ",
        "victim.country.HK", "victim.country.IN", "victim.country.ID",
        "victim.country.IR", "victim.country.JP", "victim.country.KI",
        "victim.country.KR", "victim.country.LA", "victim.country.MO",
        "victim.country.MY", "victim.country.MV", "victim.country.MH",
        "victim.country.FM", "victim.country.MN", "victim.country.MM",
        "victim.country.NR", "victim.country.NP", "victim.country.NZ",
        "victim.country.PK", "victim.country.PW", "victim.country.PG",
        "victim.country.PH", "victim.country.WS", "victim.country.SG",
        "victim.country.SB", "victim.country.LK", "victim.country.TH",
        "victim.country.TL", "victim.country.TO", "victim.country.TV",
        "victim.country.VU", "victim.country.VN"
    ],
    "CIS": [
        "victim.country.AM", "victim.country.AZ", "victim.country.BY",
        "victim.country.KZ", "victim.country.KG", "victim.country.RU",
        "victim.country.TJ", "victim.country.TM", "victim.country.UZ"
    ],
    "Europe": [
        "victim.country.AL", "victim.country.AD", "victim.country.AT",
        "victim.country.BE", "victim.country.BA", "victim.country.BG",
        "victim.country.HR", "victim.country.CY", "victim.country.CZ",
        "victim.country.DK", "victim.country.EE", "victim.country.FI",
        "victim.country.FR", "victim.country.GE", "victim.country.DE",
        "victim.country.GR", "victim.country.HU", "victim.country.IS",
        "victim.country.IE", "victim.country.IL", "victim.country.IT",
        "victim.country.LV", "victim.country.LI", "victim.country.LT",
        "victim.country.LU", "victim.country.MT", "victim.country.MD",
        "victim.country.MC", "victim.country.ME", "victim.country.NL",
        "victim.country.MK", "victim.country.NO", "victim.country.PL",
        "victim.country.PT", "victim.country.RO", "victim.country.SM",
        "victim.country.RS", "victim.country.SK", "victim.country.SI",
        "victim.country.ES", "victim.country.SE", "victim.country.CH",
        "victim.country.TR", "victim.country.UA", "victim.country.GB",
        "victim.country.VA"
    ]
}


region_incident_counts = {region:0 for region in region_mapping_for_iso_codes.keys()}
for region, countries in region_mapping_for_iso_codes.items(): 
    for country in countries: 
        if country in vcdb.columns: 
            region_incident_counts[region] += vcdb[country].sum()

region_incident_df = pd.DataFrame(
    list(region_incident_counts.items()), columns = ["Regions", "Incident Count"]
)

region_incident_df = region_incident_df.sort_values(by= "Incident Count", ascending = False)

plt.figure(figsize=(12,8))
sns.barplot(x="Incident Count", y="Regions", data=region_incident_df, palette = "viridis")
plt.title("Frequency of Cybercrime Incidents by Region", fontsize = 16)
plt.xlabel("Frequency of Incidents", fontsize = 14)
plt.ylabel("Region", fontsize = 14)
plt.tight_layout()
plt.show()
