import webbrowser as wb


def command():
    try: 
        ppp = input("Вы не хотители открыть вк?")
        
        aaa = ["vk", "Vk", "vK", "VK", "вк", "Вк", "вК", "ВК", "Вкантакте", "вкантакте", "вконтакте", "вкентакте", "невкантакте"]

        if ppp in zabanie:
            print("Открываю")
            url = "https://vk.com"
            webbrowser.open(url)
    except:
        print("Вы ввели неправельно")    

command()

