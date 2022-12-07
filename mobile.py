mobile_data = {
    'status': True,
    'data': [
        {'name': 'Xiaomi Note 5', 'price': '300 USD', 'made': 'China'},
        {'name': 'Samsung Note 6', 'price': '200 USD', 'made': 'USA'},
        {'name': 'Iphone 5', 'price': '180.5 USD', 'made': 'Japan'},
        {'name': 'Pixel 5', 'price': '89.60 USD', 'made': 'Rusia'},
        {'name': 'Techno 5', 'price': '110 USD', 'made': 'Uk'},
        {'name': 'Huawei 5', 'price': '350 USD', 'made': 'Malaysia'},
    ],
    'exchnage_rate': 103.25
}

#  Your Code Starts from here
exchnage_rate = mobile_data['exchnage_rate']
i = 0
while i < len(mobile_data['data']):
    name = mobile_data['data'][0]['name']
    country = mobile_data['data'][0]['made']
    price_usd_full = mobile_data['data'][0]['price']
    price_usd = int(price_usd_full[0:3])
    price_bdt = int(price_usd * exchnage_rate)
    i += 1


sentence = f'{name} is made in {country}. The price is {price_usd_full} which is almost equal to {price_bdt} BDT'

print(sentence)