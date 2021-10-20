# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 18:40:57 2021

Get all yugioh cards and put their info into a giant json file
API: https://db.ygoprodeck.com/api-guide/
rate limited to 20 requests per second

@author: ekohrt
"""



import requests
import json 



def download_all_cards_json(output_filename):
    """
    Downloads a json file from the internet containing information for 
    every Yu-Gi-Oh card.
    File size is 13,000+ KB.
    """
    
    url = 'https://db.ygoprodeck.com/api/v7/cardinfo.php'
    response = requests.get(url)
    j = response.json()
    with open(output_filename, 'w') as outfile:
        json.dump(j, outfile)
        print(f"File {output_filename} successfully created.")





    

"""
CARD DATA FORMAT: ________________________________

{
  "data": [
    {
      "id": 6983839,
      "name": "Tornado Dragon",
      "type": "XYZ Monster",
      "desc": "2 Level 4 monsters\nOnce per turn (Quick Effect): You can detach 1 material from this card, then target 1 Spell/Trap on the field; destroy it.",
      "atk": 2100,
      "def": 2000,
      "level": 4,
      "race": "Wyrm",
      "attribute": "WIND",
      "card_sets": [
        {
          "set_name": "Battles of Legend: Relentless Revenge",
          "set_code": "BLRR-EN084",
          "set_rarity": "Secret Rare",
          "set_rarity_code": "(ScR)",
          "set_price": "4.08"
        },
        {
          "set_name": "Duel Devastator",
          "set_code": "DUDE-EN019",
          "set_rarity": "Ultra Rare",
          "set_rarity_code": "(UR)",
          "set_price": "1.4"
        },
        {
          "set_name": "Maximum Crisis",
          "set_code": "MACR-EN081",
          "set_rarity": "Secret Rare",
          "set_rarity_code": "(ScR)",
          "set_price": "4.32"
        }
      ],
      "card_images": [
        {
          "id": 6983839,
          "image_url": "https://storage.googleapis.com/ygoprodeck.com/pics/6983839.jpg",
          "image_url_small": "https://storage.googleapis.com/ygoprodeck.com/pics_small/6983839.jpg"
        }
      ],
      "card_prices": [
        {
          "cardmarket_price": "0.42",
          "tcgplayer_price": "0.48",
          "ebay_price": "2.99",
          "amazon_price": "0.77",
          "coolstuffinc_price": "0.99"
        }
      ]
    }
  ]
}
"""
    
