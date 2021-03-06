"""import module."""
import requests


class CountryCovidData:
    """Class for tranfer the specific data from the APIweb (Json)."""

    country = {"Afghanistan": 217,
               "Albania": 216,
               "Algeria": 215,
               "Andorra": 214,
               "Angola": 213,
               "Anguilla": 212,
               "Antigua and Barbuda": 211,
               "Argentina": 210,
               "Armenia": 209,
               "Aruba": 208,
               "Australia": 207,
               "Austria": 206,
               "Azerbaijan": 205,
               "Bahamas": 204,
               "Bahrain": 203,
               "Bangladesh": 202,
               "Barbados": 201,
               "Belarus": 200,
               "Belgium": 199,
               "Belize": 198,
               "Benin": 197,
               "Bermuda": 196,
               "Bhutan": 195,
               "Bolivia": 194,
               "Bosnia": 193,
               "Botswana": 192,
               "Brazil": 191,
               "British Virgin Islands": 190,
               "Brunei": 189,
               "Bulgaria": 188,
               "Burkina Faso": 187,
               "Burundi": 186,
               "Cabo Verde": 185,
               "Cambodia": 184,
               "Cameroon": 183,
               "Canada": 182,
               "Caribbean Netherlands": 181,
               "Cayman Islands": 180,
               "Central African Republic": 179,
               "Chad": 178,
               "Channel Islands": 177,
               "Chile": 176,
               "China": 175,
               "Colombia": 174,
               "Comoros": 173,
               "Congo": 172,
               "Costa Rica": 171,
               "Croatia": 170,
               "Cuba": 169,
               "Curaçao": 168,
               "Cyprus": 167,
               "Czechia": 166,
               "Côte d'Ivoire": 165,
               "DRC": 164,
               "Denmark": 163,
               "Diamond Princess": 162,
               "Djibouti": 161,
               "Dominica": 160,
               "Dominican Republic": 159,
               "Ecuador": 158,
               "Egypt": 157,
               "El Salvador": 156,
               "Equatorial Guinea": 155,
               "Eritrea": 154,
               "Estonia": 153,
               "Ethiopia": 152,
               "Falkland Islands (Malvinas)": 151,
               "Faroe Islands": 150,
               "Fiji": 149,
               "Finland": 148,
               "France": 147,
               "French Guiana": 146,
               "French Polynesia": 145,
               "Gabon": 144,
               "Gambia": 143,
               "Georgia": 142,
               "Germany": 141,
               "Ghana": 140,
               "Gibraltar": 139,
               "Greece": 138,
               "Greenland": 137,
               "Grenada": 136,
               "Guadeloupe": 135,
               "Guatemala": 134,
               "Guinea": 133,
               "Guinea-Bissau": 132,
               "Guyana": 131,
               "Haiti": 130,
               "Holy See (Vatican City State)": 129,
               "Honduras": 128,
               "Hong Kong": 127,
               "Hungary": 126,
               "Iceland": 125,
               "India": 124,
               "Indonesia": 123,
               "Iran": 122,
               "Iraq": 121,
               "Ireland": 120,
               "Isle of Man": 119,
               "Israel": 118,
               "Italy": 117,
               "Jamaica": 116,
               "Japan": 115,
               "Jordan": 114,
               "Kazakhstan": 113,
               "Kenya": 112,
               "Kuwait": 111,
               "Kyrgyzstan": 110,
               "Lao People's Democratic Republic": 109,
               "Latvia": 108,
               "Lebanon": 107,
               "Lesotho": 106,
               "Liberia": 105,
               "Libyan Arab Jamahiriya": 104,
               "Liechtenstein": 103,
               "Lithuania": 102,
               "Luxembourg": 101,
               "MS Zaandam": 100,
               "Macao": 99,
               "Macedonia": 98,
               "Madagascar": 97,
               "Malawi": 96,
               "Malaysia": 95,
               "Maldives": 94,
               "Mali": 93,
               "Malta": 92,
               "Marshall Islands": 91,
               "Martinique": 90,
               "Mauritania": 89,
               "Mauritius": 88,
               "Mayotte": 87,
               "Mexico": 86,
               "Moldova": 85,
               "Monaco": 84,
               "Mongolia": 83,
               "Montenegro": 82,
               "Montserrat": 81,
               "Morocco": 80,
               "Mozambique": 79,
               "Myanmar": 78,
               "Namibia": 77,
               "Nepal": 76,
               "Netherlands": 75,
               "New Caledonia": 74,
               "New Zealand": 73,
               "Nicaragua": 72,
               "Niger": 71,
               "Nigeria": 70,
               "Norway": 69,
               "Oman": 68,
               "Pakistan": 67,
               "Palestine": 66,
               "Panama": 65,
               "Papua New Guinea": 64,
               "Paraguay": 63,
               "Peru": 62,
               "Philippines": 61,
               "Poland": 60,
               "Portugal": 59,
               "Qatar": 58,
               "Romania": 57,
               "Russia": 56,
               "Rwanda": 55,
               "Réunion": 54,
               "S. Korea": 53,
               "Saint Kitts and Nevis": 52,
               "Saint Lucia": 51,
               "Saint Martin": 50,
               "Saint Pierre Miquelon": 49,
               "Saint Vincent and the Grenadines": 48,
               "San Marino": 47,
               "Sao Tome and Principe": 46,
               "Saudi Arabia": 45,
               "Senegal": 44,
               "Serbia": 43,
               "Seychelles": 42,
               "Sierra Leone": 41,
               "Singapore": 40,
               "Sint Maarten": 39,
               "Slovakia": 38,
               "Slovenia": 37,
               "Solomon Islands": 36,
               "Somalia": 35,
               "South Africa": 34,
               "South Sudan": 33,
               "Spain": 32,
               "Sri Lanka": 31,
               "St. Barth": 30,
               "Sudan": 29,
               "Suriname": 28,
               "Swaziland": 27,
               "Sweden": 26,
               "Switzerland": 25,
               "Syrian Arab Republic": 24,
               "Taiwan": 23,
               "Tajikistan": 22,
               "Tanzania": 21,
               "Thailand": 20,
               "Timor-Leste": 19,
               "Togo": 18,
               "Trinidad and Tobago": 17,
               "Tunisia": 16,
               "Turkey": 15,
               "Turks and Caicos Islands": 14,
               "UAE": 13,
               "UK": 12,
               "USA": 11,
               "Uganda": 10,
               "Ukraine": 9,
               "Uruguay": 8,
               "Uzbekistan": 7,
               "Venezuela": 6,
               "Vietnam": 5,
               "Wallis and Futuna": 4,
               "Western Sahara": 3,
               "Yemen": 2,
               "Zambia": 1,
               "Zimbabwe": 0, }

    def __init__(self):
        """Get data from API web after initialize object."""
        self.data = self.get_data()

    def get_result(self, case, country):
        """Get the result data by country if the country name is valid."""
        if self.country_name_isvalid(country):
            country_code = self.find_country_code(country)
            return int(self.data[country_code][case])
        else:
            return 0

    def get_data(self):
        """Get the data in Json from the API web."""
        country_api = "https://corona.lmao.ninja/v2/countries?sort=country"
        return requests.get(country_api).json()

    def find_country_code(self, country_name):
        """Return the country object data."""
        for i in range(999):
            if country_name == self.data[i]["country"]:
                return i

    def country_name_isvalid(self, country_name):
        """Check if the country name is valid."""
        name_is_valid = country_name in self.country.keys()
        return name_is_valid


class WorldCovidData:
    """Class for transfer the specific data from the API web (Json)."""

    def __init__(self):
        """Get data from API web after initialize object."""
        self.world_today = self.get_data()

    def get_data(self):
        """Get the data in Json from the API web."""
        world_covid_api = "https://corona.lmao.ninja/v2/all"
        return requests.get(world_covid_api).json()

    def get_result(self, case):
        """Get the result data by the case name."""
        return self.world_today[case]


class ThailandCovidData:
    """Class for transfer thailand data from the API web (Json)."""

    def __init__(self):
        """Get data from API web after initialize object."""
        self.thailand = self.get_data()

    def get_data(self):
        """Get the data in Json from the API web."""
        world_covid_api = "https://covid19.th-stat.com/api/open/cases/sum"
        return requests.get(world_covid_api).json()

    def get_result(self, province):
        """Get the result data by the case name."""
        try:
            return int(self.thailand["Province"][province])
        except Exception:
            return 0
