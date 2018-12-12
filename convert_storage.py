import os, copy
from Churn_Models import*

folder = 'JSON'

class Offer_Read:
    @staticmethod
    def offer_scan():
        offer_list = os.listdir(folder)
        loaded_offers = []

        for i in offer_list:
            print(f'Adding offer: {i}')
            offer = Offer.read_from_json_file(f'{folder}/{i}')
            loaded_offers.append(offer)
        import db
        for offer in loaded_offers:
            offer = copy.copy(offer)
            db.session.add(offer)
        db.session.commit()


Offer_Read.offer_scan()






