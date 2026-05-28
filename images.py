#peyton mcadams
#images: tutorial on how to open images using python

import webbrowser

def puppy_practice():
    url = "https://parade.com/.image/w_750,q_auto:good,c_limit/MTkwNTc4NDMyMDQ3Nzg1ODUy/golden-retriever.jpg?arena_f_auto"
    webbrowser.open(url)
    #sources of information
    #picture of puppy
    #name: Seth Casteel
    #url: https://parade.com/656669/beckyhughes/photos-celebrate-national-puppy-day-with-12-adorable-puppies/
    #date: March 21, 2023 9:35 PM EDT
    #article: Celebrate National Puppy Day With Photos of 12 Absolutely Adorable Puppies
    #article author: Becky Hughes

url = ["https://dornob.com/wp-content/uploads/2010/03/beach-house-malibu-rockefeller.jpg", "https://pictures.lodgix.com/media/gallery/property-98427/i020892_preview.jpg", "https://s.wsj.net/public/resources/images/OB-WN986_hodj02_HD_20130303224012.jpg", "https://s.wsj.net/public/resources/images/BN-RT353_HOTY_TOP_20170123150754.jpg"]
descriptions = ["a smaller yet still spacious house near the beach, built on a small lot with wood and limestone features", "a huge beach house perfect for large families right on the beach", "a humble ski chalet perfect for lazy and active ski days on the heart of the mountain", "a larger ski house perfect for large vacationing families, fulfilling every winter desire"]
def realtor():
    temp = input("Would you like to be in a warm or cold climate? ")
    if temp == "warm" or temp == "Warm":
        beach = input("Would you like to be on the beach: yes or no? ")
        if beach == "Yes" or beach == "yes":
            webbrowser.open(url[1])
            print(descriptions[1])
        if beach == "No" or beach == "no":
            webbrowser.open(url[0])
            print(descriptions[0])
    if temp == "cold" or temp == "Cold":
        size = input("Would you like a large or small house? ")
        if size == "large" or size == "Large":
            webbrowser.open(url[3])
            print(descriptions[3])
        if size == "small" or size == "Small":
            webbrowser.open(url[2])
            print(descriptions[2])

realtor()

#sources
#WARM CLIMATE HOUSE photo from dornob.com
#Big Luxury Beach House Makes the Most of a Small Lot
#by Dornob Staff

#BIG BEACH HOUSE from Ben's Beach Homes
#titled Luxury Breeze
#2020

#SMALL SKI HOUSE From the Wall Street Journal
#"Asia House of the Day: Ski Chalet in Japan"
#by Patrick Brzeski
#on March 5, 2013 8:52 AM ET

#LARGE SKI HOUSE From the Wall Street Jounral
#"House of the Year: A Big Sky Manor Wins"
#by Sarah Tilton
#on January 26, 2017 10:23 AM ET
