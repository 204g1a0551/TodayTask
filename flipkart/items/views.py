from django.http import HttpResponse
def mview(request,id):
    mobiles=[{'id':1,'name':'Vivo Iqoo Z6x ','config':['8gb','128gb'],'cost':100000},
             {'id':2,'name':'Apple 11','config':['0gb','256gb'],'cost':1000},
             {'id':3,'name':'Nokia 11','config':['12gb','128gb'],'cost':10}]
    result=None
    for i in  mobiles:
        if i['id'] is id:
            result=i
            break
    if result is not None:
        return HttpResponse(f"<h1>Required Phone</h1><br><p><strong>Name: </strong> {result['name']}<br><strong>Configuration: </strong> {result['config'][0]}{result['config'][1]}<br><strong>Cost: </strong> {result['cost']}<br></p>")
    else:
        return HttpResponse(f"Sorry Dude Mobile Not Matched!!!")
def lview(request, id):
    laptops = [
        {'id': 1, 'name': 'HP Pavilion', 'config': ['16gb', '512gb'], 'cost': 80000},
        {'id': 2, 'name': 'Dell XPS 15', 'config': ['32gb', '1tb'], 'cost': 120000},
        {'id': 3, 'name': 'MacBook Pro', 'config': ['16gb', '512gb'], 'cost': 150000}
    ]
    
    result = None
    for laptop in laptops:
        if laptop['id'] == id:
            result = laptop
            break
    
    if result is not None:
        return HttpResponse(f"<h1>Required Laptop</h1><br><p><strong>Name: </strong>{result['name']}<br><strong>Configuration: </strong>{', '.join(result['config'])}<br><strong>Cost: </strong>{result['cost']}<br></p>")
    else:
        return HttpResponse("Sorry Dude Laptop Not Matched!!!")
from django.http import HttpResponse

def mview(request, id):
    mobiles = [
        {'id': 1, 'name': 'Vivo Iqoo Z6x', 'config': ['8gb', '128gb'], 'cost': 100000},
        {'id': 2, 'name': 'Apple 11', 'config': ['0gb', '256gb'], 'cost': 1000},
        {'id': 3, 'name': 'Nokia 11', 'config': ['12gb', '128gb'], 'cost': 10}
    ]
    
    result = None
    for mobile in mobiles:
        if mobile['id'] == id:
            result = mobile
            break
    
    if result is not None:
        return HttpResponse(f"<h1>Required Phone</h1><br><p><strong>Name: </strong>{result['name']}<br><strong>Configuration: </strong>{', '.join(result['config'])}<br><strong>Cost: </strong>{result['cost']}<br></p>")
    else:
        return HttpResponse("Sorry Dude Mobile Not Matched!!!")


def lview(request, id):
    laptops = [
        {'id': 1, 'name': 'HP Pavilion', 'config': ['16gb', '512gb'], 'cost': 80000},
        {'id': 2, 'name': 'Dell XPS 15', 'config': ['32gb', '1tb'], 'cost': 120000},
        {'id': 3, 'name': 'MacBook Pro', 'config': ['16gb', '512gb'], 'cost': 150000}
    ]
    
    result = None
    for laptop in laptops:
        if laptop['id'] == id:
            result = laptop
            break
    
    if result is not None:
        return HttpResponse(f"<h1>Required Laptop</h1><br><p><strong>Name: </strong>{result['name']}<br><strong>Configuration: </strong>{', '.join(result['config'])}<br><strong>Cost: </strong>{result['cost']}<br></p>")
    else:
        return HttpResponse("Sorry Dude Laptop Not Matched!!!")


def aview(request, id):
    airpods = [
        {'id': 1, 'name': 'AirPods 2nd Gen', 'config': ['Bluetooth 5.0', 'Wireless Charging'], 'cost': 15000},
        {'id': 2, 'name': 'AirPods Pro', 'config': ['Active Noise Cancellation', 'Water Resistance'], 'cost': 25000},
        {'id': 3, 'name': 'AirPods Max', 'config': ['Active Noise Cancellation', 'Spatial Audio'], 'cost': 60000}
    ]
    
    result = None
    for airpod in airpods:
        if airpod['id'] == id:
            result = airpod
            break
    
    if result is not None:
        return HttpResponse(f"<h1>Required Laptop</h1><br><p><strong>Name: </strong>{result['name']}<br><strong>Configuration: </strong>{', '.join(result['config'])}<br><strong>Cost: </strong>{result['cost']}<br></p>")
    else:
        return HttpResponse("Sorry Dude Laptop Not Matched!!!")
