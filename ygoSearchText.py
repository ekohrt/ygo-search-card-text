# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 10:34:40 2021


I want a comprehensive list of every card that mentions 'normal' monsters, 
aka 'non-effect' monsters. Because the online database search is bad.


@author: ekohrt
"""

import json
import re

# load the json file of all cards into a list of card objects
with open('YugiohCards.json', 'r', encoding='utf-8') as f:
    cards_list = json.load(f)['data']



class CardObject:
    def __init__(self, name, typ, text, img_link_big, img_link_small, card_id):
        self.name = name
        self.typ = typ
        self.text = text
        self.img_link_big = img_link_big
        self.img_link_small = img_link_small
        self.card_id = card_id
        

def search_all_cards_for_regex(regex_string):
    """
    Returns a list of (cardname, text) tuples of each card with matching text.
    Case insensitive.
    """
    matching_cards = []
    for card_object in cards_list:
        cardname = card_object['name']
        card_text = card_object.get('desc', "").lower() # if card has no text, use empty string
        card_type = card_object.get('type', "No Type")
        card_id = card_object['id']
        img_link_big = card_object.get('card_images', None)[0]['image_url']
        img_link_small = card_object.get('card_images', None)[0]['image_url_small']
        # filter out normal monsters, because they have flavor text
        if card_type != "Normal Monster" and re.match(regex_string, card_text):
            matching_cards.append( CardObject(cardname, card_type, card_text, img_link_big, img_link_small, card_id) )
            
    return matching_cards
        


def output_cardObject_to_file(cardObjects):
    #write results to a human-readable text file
    with open('results.txt', 'w', encoding='utf-8') as outfile:
        for c in cardObjects:
            outfile.write(f"{c.name}__________\n")
            outfile.write(f"{c.typ}\n")
            outfile.write(c.text+'\n')
            outfile.write(c.img_link_big+'\n')
            outfile.write('\n')
    print("RESULTS:", len(cardObjects))
    
    
    

def export_decklist_to_ydk_file(cardObject_list, outfile_path):
    """
    YDK file format:
        
    #created by ygopro2
    #main
    69247929    # card ids go here, 1 per line - but don't put this comment in file
    #extra
    10817524    
    !side
    48940337
    """
    with open(outfile_path, 'w', encoding='utf-8') as outfile:
        outfile.write("#created by me\n")
        outfile.write("#main\n")
        for cardObject in cardObject_list:
            outfile.write( str(cardObject.card_id) + "\n")
        outfile.write("#extra\n")
        outfile.write("!side")
    print(f"File {outfile_path} created.")

def main():
    regex_string = '((.*normal monster.*)|(.*non-effect monster.*)|(.*except for effect monsters.*))' 
    cardObjects = search_all_cards_for_regex(regex_string)
    cardObjects.sort(key=lambda x: x.typ)    #sort by type
    
    export_decklist_to_ydk_file(cardObjects, 'ygoDeck.ydk')
    
    
   
    
    
    
    
    
if __name__ == '__main__':
    main()
    
