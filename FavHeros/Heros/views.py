from django.http import HttpResponse
def balaya(request,id):
    dialogues=[
    {'id': 1, 'script': "Flute! Jenka mundu oodhu"},
    {'id': 2, 'script': "Simham single ga vusthundi"},
    {'id': 3, 'script': "Jai Balayaa"},
    {'id': 4, 'script': "Adhi Maku Varthichadhu!!!!!!!!"}
    ]
    res=None
    for i in dialogues:
        if i['id']==id:
            res=i
            break
    if res is not None:
        return HttpResponse(f"<h1 align='center'>Resquested Dialogue</h1><hr><div id='1' align ='center' >{res['script']}</div>")
    else:
        return HttpResponse(f"Not Available!")
def chiru(request,id):
    dialogues=[
    {'id': 1, 'script': "Boss is Back"},
    {'id': 2, 'script': "Mookey Kadha Ani pikeysthey Pika Kostha"},
    {'id': 3, 'script': "Rough aadinchesthanu"},
    {'id': 4, 'script': "Patalu Cheppaka poyina nanni acharya ani antaru endhuku antey guntapatalu chepputhanu ani emo!!!"},
    ]
    res=None
    for i in dialogues:
        if i['id']==id:
            res=i
            break
    if res is not None:
        return HttpResponse(f"<h1 align='center'>Resquested Dialogue</h1><hr><div id='1' align ='center'>{res['script']}</div>")
    else:
        return HttpResponse(f"Not Available!")
def mahesh(request,id):
    dialogues=[
    {'id': 1, 'script': "Evadu kodithey dhima thirigi mind block avuthundo vadey padu gadu"},
    {'id': 2, 'script': "Prathi edavaki naa peru thonee problem aaaa"},
    {'id': 3, 'script': "Ontariga puttav… Ontariga pothav… ee Ontariga Jogging chesukoleva… Bayaniki Meaning Ye Theliyani Blood raa Naadhi…"},
    {'id': 4, 'script': "Cinemalu Chudaledha"},
    ]
    res=None
    for i in dialogues:
        if i['id']==id:
            res=i
            break
    if res is not None:
        return HttpResponse(f"<h1>Resquested Dialogue</h1>{res['script']}")
    else:
        return HttpResponse(f"Not Available!")

    
