from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from helloworld import dbconnection
#def index(request):
    #return HttpResponse("<h1>Hello World!!! Welcome</h1>")
def index(request):
    return render(request,'index.html',{})

def login(request):
    if request.method == "POST":
        e=request.POST.get("email")
        p=request.POST.get("password")
        sql="select * from hello_reg where email='"+e+"' and password='"+p+"'"
        data=dbconnection.selectone(sql)
        if data:
            request.session["user"]=e
            return HttpResponseRedirect("userhome")
    return render(request,'login.html',{})

def register(request):
    #return render(request,'register.html',{})
    if request.method=="POST":
        name=request.POST.get("n")
        email=request.POST.get("e")
        age=request.POST.get("a")
        password=request.POST.get("p")
        address=request.POST.get("ad")
        img=request.FILES['photo']
        fs=FileSystemStorage()
        fs.save("helloworld/static/upic/"+img.name,img)

        sql="INSERT INTO hello_reg(name,email,password,age,address,photo) values('"+name+"','"+email+"','"+password+"','"+age+"','"+address+"','"+img.name+"')"
        dbconnection.insert(sql)
        return HttpResponseRedirect("register")
    return render(request,'register.html',{})

def pages(request):
    return render(request,'pages.html',{})

def userhome(request):
    us=request.session["user"]
    sql="SELECT * FROM hello_reg WHERE email='"+us+"'"
    data=dbconnection.selectone(sql)
    return render(request,'userhome.html',{"d":data})
# Create your views here.
def edit(request):
    uid=request.GET['id']
    if request.method=="POST":
        name=request.POST.get("n")
        email=request.POST.get("e")
        age=request.POST.get("a")
        password=request.POST.get("p")
        address=request.POST.get("ad")
        sql1="update hello_reg set name='"+name+"', email='"+email+"', age='"+age+"', password='"+password+"', address='"+address+"' where id='"+uid+"'"
        dbconnection.update(sql1)
        return HttpResponseRedirect("userhome")
    sql=" select * from hello_reg where id='"+uid+"' "
    data=dbconnection.selectone(sql)
    return render(request,"edit.html",{"d":data})

def mygallery(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        type = request.POST.get('type')
        file = request.FILES['photo']
        fs = FileSystemStorage()
        fs.save('helloworld/static/upic/' + file.name, file)
        sql = 'INSERT INTO `uploadtb`(`nemail`, `title`, `file`, `type`) VALUES ("' + request.session['user'] + '","' + title + '","' + str(file) + '","' + type + '")'
        dbconnection.insert(sql)
        return HttpResponseRedirect('mygallery')
    return render(request,"mygallery.html",{})

def image(request):
    sql="select *from uploadtb where nemail='"+request.session['user']+"' and type='1'"
    data=dbconnection.selectall(sql)
    return render(request,'image.html',{"d":data})


def audio(request):
    sql="select *from uploadtb where nemail='"+request.session['user']+"' and type='2'"
    data=dbconnection.selectall(sql)
    return render(request,'audio.html',{"d":data})


def video(request):
    sql="select *from uploadtb where nemail='"+request.session['user']+"' and type='3'"
    data=dbconnection.selectall(sql)
    return render(request,'video.html',{"d":data})