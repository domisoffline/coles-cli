import requests
import colorama

print(f"{colorama.Fore.RED}Coles-CLI By Dom Is Offline{colorama.Fore.RESET}")
print(f"{colorama.Fore.BLUE}[1] {colorama.Fore.GREEN}Search Item{colorama.Fore.RESET}")
option = input(f"{colorama.Fore.BLUE}Enter desired option: {colorama.Fore.RESET}")
if option == "1":
    option = input(f"{colorama.Fore.BLUE}Enter desired search term: {colorama.Fore.RESET}")
    r = requests.get(f"https://shop.coles.com.au/search/resources/autosuggest/bySearchTerm/{option}?rows=5")
    for i in r.json()['records']:
        print(i['searchterm'].title())