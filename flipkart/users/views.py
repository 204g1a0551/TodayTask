from django.http import HttpResponse

def main(request,id):
    customers=[{'id':1,'name':'Mahesh Kumar','phone':7989979634},
               {'id':2,'name':'Usman Basha','phone':39845329598},
               {'id':3,'name':'Mounesh','phone':8393489349}]
    res=None
    for i in customers:
        if i['id']==id:
            res=i
            break
    if res is not None:
        return HttpResponse(f"<h1>Required Customer</h1><br><p><strong>Name: </strong> {res['name']}<br><strong>Phone: </strong> {res['phone']}</p>")
    else:
        return HttpResponse("Sorry Dude! User not found!!")


def main1(request,id):
    admin=[{'id':1,'name':'Mahesh Kumar','phone':7989979634},
               {'id':2,'name':'Usman Basha','phone':39845329598},
               {'id':3,'name':'Mounesh','phone':8393489349}]
    res=None
    for i in admin:
        if i['id']==id:
            res=i
            break
    if res is not None:
        return HttpResponse(f"<h1>Required Adminstratior</h1><br><p><strong>Name: </strong> {res['name']}<br><strong>Phone: </strong> {res['phone']}</p>")
    else:
        return HttpResponse("Sorry Dude! Admin not found!!")