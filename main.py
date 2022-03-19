#Web scraping basics 
#Scraping a google page to find jobs in a certain area

from requests_html import HTMLSession
s = HTMLSession()


print("Please enter your location: ")
query = input()
url  = f"https://www.google.com/search?q=jobs+in+{query}&rlz=1C1CHBF_enCA965CA965&oq=job&aqs=chrome.1.69i57j69i59l2j0i512l2j69i60l3&sourceid=chrome&ie=UTF-8&ibp=htl;jobs&sa=X&sqi=2&ved=2ahUKEwj4raa0ndP2AhUiyosBHdqrBGgQutcGKAB6BAgQEAQ&sxsrf=APq-WBuI0mz1WVWj6LhyHWoj4Gqvdyi5Cw:1647729147752#htivrt=jobs&htidocid=HmnyQPFY6QAAAAAAAAAAAA%3D%3D&fpstate=tldetail"

r=  s.get(url, headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36"})

print("-------------------------------")
print("These are the jobs in your area:")
print("-------------------------------")
for item in (r.html.find('div.BjJfJf')):
    print(item.text)

