import collections
import re
import requests


list_ips = []
list_country = []


# Geolocation API
def get_country(ip):
    api_key = "dc410de53add485f8dbeac491e1fd242" #Change to your API key. This one has a daily limit of 1000 requests.
    url = f"https://api.ipgeolocation.io/ipgeo?apiKey={api_key}&ip={ip}" #Change the API to the one you want to use.
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        list_country.append(response.json()["country_name"])
        if 'country_name' in data:
            country = data['country_name']
            return country
    return "API Error/Private Address"


#Opens the file, reads it line by line, and closes it.
with open("sshd.log", "r") as file:
    #Goes over each line of the file
    for line in file:
        result = re.search(r"(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})", line)
        if result:  #If the regex matches, it prints the IP and the country.
            ip = result.group(1)
            if ip not in list_ips:
                list_ips.append(ip)
                country = get_country(ip)
                print(f"IP: {ip} - Country: {country}")



#Prints the number of IP addresses and the number of times each country appears.
print(f"Number of IP Adresses: {len(list_ips)}")
list_country = collections.Counter(list_country)
print(list_country)
