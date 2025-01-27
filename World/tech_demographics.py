# Import Libraries 
import pandas as pd #used for data manipulation and analysis 
import matplotlib
import matplotlib.pyplot as plt 
import seaborn as sns 



REGION_ISO_MAP = {
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

COUNTRY_REGION_MAP = {'South Africa': 'Africa',
 'Angola': 'Africa',
 'Burundi': 'Africa',
 'Benin': 'Africa',
 'Botswana': 'Africa',
 'Burkina Faso': 'Africa',
 'Central African Rep.': 'Africa',
 'Cameroon': 'Africa',
 'Congo (Rep. of the)': 'Africa',
 'Comoros': 'Africa',
 'Cabo Verde': 'Africa',
 "Côte d'Ivoire": 'Africa',
 'Djibouti': 'Africa',
 'Ethiopia': 'Africa',
 'Gabon': 'Africa',
 'Ghana': 'Africa',
 'Gambia': 'Africa',
 'Guinea-Bissau': 'Africa',
 'Equatorial Guinea': 'Africa',
 'Guinea': 'Africa',
 'Kenya': 'Africa',
 'Liberia': 'Africa',
 'Libya': 'Arab States',
 'Madagascar': 'Africa',
 'Mali': 'Africa',
 'Mauritania': 'Africa',
 'Malawi': 'Africa',
 'Mozambique': 'Africa',
 'Morocco': 'Arab States',
 'Niger': 'Africa',
 'Nigeria': 'Africa',
 'Rwanda': 'Africa',
 'Senegal': 'Africa',
 'Seychelles': 'Africa',
 'Sierra Leone': 'Africa',
 'Somalia': 'Africa',
 'Eswatini': 'Africa',
 'Sudan': 'Africa',
 'Chad': 'Africa',
 'Togo': 'Africa',
 'Tunisia': 'Arab States',
 'Tanzania': 'Africa',
 'Uganda': 'Africa',
 'Zambia': 'Africa',
 'Zimbabwe': 'Africa',
 'Eritrea': 'Africa',
 'South Sudan': 'Africa',
 'Aruba': 'The Americas',
 'Anguilla': 'The Americas',
 'Antigua and Barbuda': 'The Americas',
 'Argentina': 'The Americas',
 'Bahamas': 'The Americas',
 'Barbados': 'The Americas',
 'Belize': 'The Americas',
 'Bolivia (Plurinational State of)': 'The Americas',
 'Brazil': 'The Americas',
 'Canada': 'The Americas',
 'Chile': 'The Americas',
 'Colombia': 'The Americas',
 'Costa Rica': 'The Americas',
 'Cuba': 'The Americas',
 'Dominica': 'The Americas',
 'Dominican Rep.': 'The Americas',
 'Ecuador': 'The Americas',
 'El Salvador': 'The Americas',
 'French Guiana': 'The Americas',
 'Grenada': 'The Americas',
 'Greenland': 'The Americas',
 'Guatemala': 'The Americas',
 'Guyana': 'The Americas',
 'Haiti': 'The Americas',
 'Honduras': 'The Americas',
 'Jamaica': 'The Americas',
 'Mexico': 'The Americas',
 'Nicaragua': 'The Americas',
 'Panama': 'The Americas',
 'Paraguay': 'The Americas',
 'Peru': 'The Americas',
 'Puerto Rico': 'The Americas',
 'Saint Kitts and Nevis': 'The Americas',
 'Saint Lucia': 'The Americas',
 'Saint Vincent and the Grenadines': 'The Americas',
 'Suriname': 'The Americas',
 'Trinidad and Tobago': 'The Americas',
 'United States': 'The Americas',
 'Uruguay': 'The Americas',
 'Venezuela': 'The Americas',
 'Virgin Islands (US)': 'The Americas',
 'British Virgin Islands': 'The Americas',
 'Curacao': 'The Americas',
 'Algeria': 'Arab States',
 'Saudi Arabia': 'Arab States',
 'Bahrain': 'Arab States',
 'Egypt': 'Arab States',
 'Iraq': 'Arab States',
 'Jordan': 'Arab States',
 'Kuwait': 'Arab States',
 'Lebanon': 'Arab States',
 'Oman': 'Arab States',
 'Qatar': 'Arab States',
 'Syrian Arab Republic': 'Arab States',
 'United Arab Emirates': 'Arab States',
 'Yemen': 'Arab States',
 'Afghanistan': 'Asia and the Pacific',
 'Australia': 'Asia and the Pacific',
 'Bangladesh': 'Asia and the Pacific',
 'Bhutan': 'Asia and the Pacific',
 'Brunei Darussalam': 'Asia and the Pacific',
 'Cambodia': 'Asia and the Pacific',
 'China': 'Asia and the Pacific',
 'Cook Islands': 'Asia and the Pacific',
 'Fiji': 'Asia and the Pacific',
 'India': 'Asia and the Pacific',
 'Indonesia': 'Asia and the Pacific',
 'Iran (Islamic Republic of)': 'Asia and the Pacific',
 'Israel': 'Asia and the Pacific',
 'Japan': 'Asia and the Pacific',
 'Kazakhstan': 'Commonwealth of Independent States (CIS)',
 'Kiribati': 'Asia and the Pacific',
 'Lao P.D.R.': 'Asia and the Pacific',
 'Malaysia': 'Asia and the Pacific',
 'Maldives': 'Asia and the Pacific',
 'Mongolia': 'Asia and the Pacific',
 'Myanmar': 'Asia and the Pacific',
 'Nepal (Republic of)': 'Asia and the Pacific',
 'New Zealand': 'Asia and the Pacific',
 'Pakistan': 'Asia and the Pacific',
 'Papua New Guinea': 'Asia and the Pacific',
 'Philippines': 'Asia and the Pacific',
 'Samoa': 'Asia and the Pacific',
 'Singapore': 'Asia and the Pacific',
 'Sri Lanka': 'Asia and the Pacific',
 'Thailand': 'Asia and the Pacific',
 'Timor-Leste': 'Asia and the Pacific',
 'Tonga': 'Asia and the Pacific',
 'Turkmenistan': 'Commonwealth of Independent States (CIS)',
 'Tuvalu': 'Asia and the Pacific',
 'Uzbekistan': 'Commonwealth of Independent States (CIS)',
 'Vanuatu': 'Asia and the Pacific',
 'Viet Nam': 'Asia and the Pacific',
 'Armenia': 'Commonwealth of Independent States (CIS)',
 'Azerbaijan': 'Commonwealth of Independent States (CIS)',
 'Belarus': 'Commonwealth of Independent States (CIS)',
 'Georgia': 'Commonwealth of Independent States (CIS)',
 'Kyrgyzstan': 'Commonwealth of Independent States (CIS)',
 'Moldova': 'Commonwealth of Independent States (CIS)',
 'Russian Federation': 'Commonwealth of Independent States (CIS)',
 'Tajikistan': 'Commonwealth of Independent States (CIS)',
 'Ukraine': 'Commonwealth of Independent States (CIS)',
 'Albania': 'Europe',
 'Andorra': 'Europe',
 'Austria': 'Europe',
 'Belgium': 'Europe',
 'Bosnia and Herzegovina': 'Europe',
 'Bulgaria': 'Europe',
 'Croatia': 'Europe',
 'Cyprus': 'Europe',
 'Czech Republic': 'Europe',
 'Denmark': 'Europe',
 'Estonia': 'Europe',
 'Finland': 'Europe',
 'France': 'Europe',
 'Germany': 'Europe',
 'Gibraltar': 'Europe',
 'Greece': 'Europe',
 'Hungary': 'Europe',
 'Iceland': 'Europe',
 'Ireland': 'Europe',
 'Italy': 'Europe',
 'Latvia': 'Europe',
 'Liechtenstein': 'Europe',
 'Lithuania': 'Europe',
 'Luxembourg': 'Europe',
 'Malta': 'Europe',
 'Monaco': 'Europe',
 'Montenegro': 'Europe',
 'Netherlands': 'Europe',
 'North Macedonia': 'Europe',
 'Norway': 'Europe',
 'Poland': 'Europe',
 'Portugal': 'Europe',
 'Romania': 'Europe',
 'San Marino': 'Europe',
 'Serbia': 'Europe',
 'Slovakia': 'Europe',
 'Slovenia': 'Europe',
 'Spain': 'Europe',
 'Sweden': 'Europe',
 'Switzerland': 'Europe',
 'United Kingdom': 'Europe',
 'Vatican': 'Europe',
 'Ascension': 'Africa',
 'Bermuda': 'The Americas',
 'Cayman Islands': 'The Americas',
 "Dem. People's Rep. of Korea": 'Asia and the Pacific',
 'Dem. Rep. of the Congo': 'Africa',
 'Falkland (Malvinas) Is.': 'The Americas',
 'Faroe Islands': 'Europe',
 'French Polynesia': 'Asia and the Pacific',
 'Guadeloupe': 'The Americas',
 'Guam': 'Asia and the Pacific',
 'Guernsey': 'Europe',
 'Hong Kong, China': 'Asia and the Pacific',
 'Jersey': 'Europe',
 'Korea (Rep. of)': 'Asia and the Pacific',
 'Kosovo': 'Europe',
 'Lesotho': 'Africa',
 'Macao, China': 'Asia and the Pacific',
 'Marshall Islands': 'Asia and the Pacific',
 'Martinique': 'The Americas',
 'Mauritius': 'Africa',
 'Mayotte': 'Africa',
 'Micronesia': 'Asia and the Pacific',
 'Montserrat': 'The Americas',
 'Namibia': 'Africa',
 'Nauru': 'Asia and the Pacific',
 'New Caledonia': 'Asia and the Pacific',
 'Niue': 'Asia and the Pacific',
 'Palau': 'Asia and the Pacific',
 'Réunion': 'Africa',
 'Sao Tome and Principe': 'Africa',
 'Solomon Islands': 'Asia and the Pacific',
 'St. Helena': 'Africa',
 'State of Palestine': 'Arab States',
 'Taiwan, Province of China': 'Asia and the Pacific',
 'Tokelau': 'Asia and the Pacific',
 'Türkiye': 'Europe',
 'Wallis and Futuna': 'Asia and the Pacific'
}


# Read in Internet Usage Data

# Create a pandas dataframe from the CSV data
int_usage_df = pd.read_csv("World/individuals_using_internet.csv")

# print(int_usage_df)

# Read in Annual Investment Data

# Create a pandas dataframe from the CSV data
ann_invs_df = pd.read_csv("World/annual-investment-in-telecommunication-services_1737932363975.csv")

# Read in Country Connectivity data
country_conn = pd.read_csv("World/country-access-to-international-connectivity_1737944348620.csv")

# Keep only relevant columns (Iso, ID, and value)
int_usage_df = int_usage_df[["entityIso", "entityID", "dataValue", "entityName"]]
ann_invs_df = int_usage_df[["entityIso", "entityID", "dataValue", "entityName"]]
country_conn = country_conn[["entityIso", "entityID", "dataValue", "entityName"]]

# Add 'Region' column to each data frame from region map
int_usage_df['Region'] = int_usage_df['entityName'].map(COUNTRY_REGION_MAP) 
ann_invs_df['Region'] = ann_invs_df['entityName'].map(COUNTRY_REGION_MAP)
country_conn['Region'] = country_conn['entityName'].map(COUNTRY_REGION_MAP)

# Boxplots for each demographic

# Internet Usage
int_usage_plot = sns.boxplot(int_usage_df, x="Region", 
y="dataValue", palette="Set1")

int_usage_plot.set_xlabel("Region")
int_usage_plot.set_ylabel("Internet Usage (%)")

plt.title('Internet Usage by Region')
# # Annual Investment
# sns.boxplot(ann_invs_df, x="Region", y="dataValue", palette="Set1")
# plt.title('Annual Investment')
# # Country Connectivity
# sns.boxplot(country_conn, x="Region", y="dataValue", palette="Set1")
# plt.title('Country Connectivity (pct)')


plt.show()

##### CORRELATION #####
# Load VCDB database
vcdb_data1 = pd.read_csv("Incidents/vcdb_1.csv")
vcdb_data2 = pd.read_csv('Incidents/vcdb_2.csv')