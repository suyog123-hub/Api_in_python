# code to show the real time status of coovid-19 in nepal 
import requests
def covid(country):
    url=f"https://disease.sh/v3/covid-19/countries/{country}"
    data=requests.get(url).json()
    # it show the data in the terminal 
    print(f"totalCases in {country}",data["cases"])
    print(f"totalDeaths in {country}",data["deaths"])
    print(f"totalRecovered in {country}",data["recovered"])
# to check the cases for other country simple change the nepal to the country name you want
covid("Nepal")