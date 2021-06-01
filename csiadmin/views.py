from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
import pandas as pd
from .models import Assignedtask,Userdata
from django.core.paginator import Paginator
from django.db import connection
from django.core.mail import send_mail
import random as r
import xlsxwriter

a=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<']

cursor = connection.cursor()


sheet_url ="https://docs.google.com/spreadsheets/d/1Qw1dnn7ynTIiqzceZ5WubFNY6D1_yU5IedLqxD92MKw/edit#gid=1669915180"
csv_export_url = sheet_url.replace('/edit#gid=', '/export?format=csv&gid=')
l1=""
l2=""

# Create your views here.
def login_page(request):
    return (render(request, 'index.html'))
    # return (render(request, 'login_dashboard.html'))

@csrf_exempt
def login_dashboard(request):
    if request.method == "POST":
        loginusername = request.POST['loginusername']
        loginpassword = request.POST['loginpassword']
        user = authenticate(username=loginusername, password=loginpassword)

        if user is not None:
            login(request, user)
            if (request.user.is_staff):
                messages.success(request, "Successfully Login!!!")
                return (render(request, 'login_dashboard.html'))
            else:
                return (render(request, 'user_dashboard.html'))
        else:
            messages.error(request, "Invalid User name or Password")
            return (render(request, 'index.html'))
            # return (render(request))

def logout_admin(request):
    logout(request)
    return (render(request, 'index.html'))

def user_registration(request):
    if (str(request.user) != "AnonymousUser"):
        if(request.user.is_staff):
            return (render(request, 'user_registration.html'))
        else:
            return (render(request, 'index.html'))
    else:
        return (render(request, 'index.html'))


def check_user_registration(request):
    if (str(request.user) != "AnonymousUser"):
        if(request.user.is_staff):
            if request.method == "POST":
                fname = request.POST['first_name']
                lname = request.POST['last_name']
                username = request.POST['username']
                email = request.POST['email']
                p1 = request.POST['password']
                p2 = request.POST['confirm_password']

                if(p1!=p2):
                    messages.error(request, "Password didn't Match")
                    return (render(request, 'user_registration.html'))
                try:
                    myuser = User.objects.create_user(username, email, p1)
                    myuser.first_name = fname
                    myuser.last_name = lname
                    myuser.save()
                    messages.success(request,"User Created Successfully")
                    body="Sir/Ma'am,"+"\n\n"+"Your Login Credential for the National Level Article Competition are mention below:"+"\n\n"+"Username: "+ username+"\n\n"+"Password:"+p1+"\n\n"+"Login URL: http://udyat.pythonanywhere.com/"
                    send_mail(
                        'Article Competition CSI Id Password',
                        body,
                        'udyat@miet.ac.in',
                        [email],
                        fail_silently=False,
                    )
                    return (render(request, 'user_registration.html'))
                except:
                    messages.error(request, "Username Already Registered")
                    return (render(request, 'user_registration.html'))
            else:
                return(HttpResponse("Error"))
        else:
            return (render(request, 'index.html'))
    else:
        return (render(request, 'index.html'))

def dashboard(request):
    if (str(request.user) != "AnonymousUser"):
        if(request.user.is_staff):
            return (render(request, 'login_dashboard.html'))
        else:
            return (render(request, 'index.html'))
    else:
        return (render(request, 'index.html'))


def assign_task(request):
    if (str(request.user) != "AnonymousUser"):
        if(request.user.is_staff):
            global df,l1,l2
            l3=[]
            l4=[]
            k=[]
            l5={}
            df = pd.read_csv(csv_export_url)
            k1 = df.values.tolist()
            k.extend(k1)

            sam = User.objects.all()
            lst = []
            for i in sam:
                if (i.is_staff == False):
                    lst.append(i.username)

            for i in range(len(k)):
                file_url = "https://drive.google.com/open?id="
                l1=file_url + k[i][6][33:]
                l2=file_url + k[i][7][33:]
                l3.append(l1)
                l4.append(l2)
            a=Assignedtask.objects.all()
            for i in a:
                l5[i.teamid]=[i.checkername,i.date]
                print(i.date)

            # l4 Id-Card link

            f = {'f1': l3, 'l5': l5, 'l1':lst}
            #print(f['f1'])
            paginator=Paginator(f['f1'],10)
            page = request.GET.get('page')
            f['f1']= paginator.get_page(page)
            return render(request,'assign_task2.html',f)
        else:
            return (render(request, 'index.html'))
    else:
        return (render(request, 'index.html'))


def impdata(request):
    global t
    t=[]
    cname= str(request.POST.get('name'))
    link=str(request.POST.get('li'))
    id=str(request.POST.get('id1'))
    Assign_info = Assignedtask(checkername = cname,filelink=link,teamid=id)
    Assign_info.save()
    t.append(cname)
    t.append(link)
    t.append(id)
    #print(id)
    try:
        user = Userdata.objects.get(Id=id)
        user.delete()
        #print(user)
    except:
        pass

    return HttpResponse(cname)



def get_review(request):
    x=int(request.POST.get('x'))
    lst=[]
    k = 0
    z=[]
    u1 = Userdata.objects.all().order_by('Id')

    for j in u1:
        d=j.date
        t=d.strftime("%b %d, %Y, %I:%M %p")
        z.append(t)
        lst.append([j.Id, j.Decision, j.Reason+"\n\nReviewed Date: "+t])
    print(z)
    try:
        #t=lst[-1][0]+1
        t=x+1
    except:
        t=0

    for j in range(t):
        try:
            if (lst[k][0] == j):
                k += 1
            else:
                lst.insert(k, [j, 2, ""])
                k += 1
        except:
            lst.insert(k, [j, 2, ""])
            k += 1

    return HttpResponse([lst[x]])


def review_task(request):
    if (str(request.user) != "AnonymousUser"):
        if(not request.user.is_staff):
            udict1 = {}
            udict2 = {}
            lt = []
            name = str(request.user)

            a1 = Assignedtask.objects.all().order_by('teamid')
            for i in a1:
                cn = i.checkername.split(",")
                # print(k, i.teamid)

                if name in cn:
                    lt.append([i.teamid,i.date])
                    udict2[i.teamid] = i.filelink
                    udict1[i.teamid] = cn
            # print(lst)
            paginator = Paginator(lt, 10)
            page = request.GET.get('page')
            lt = paginator.get_page(page)
            return render(request, 'user_review.html', {'udict': udict1, 'udict2': udict2, 'lt': lt})
        else:
            return (render(request, 'index.html'))
    else:
        return (render(request, 'index.html'))





def udata(request):
    A1=str(request.POST.get('Acc1'))
    T1=str(request.POST.get('Text'))
    u1=str(request.POST.get('uname'))
    keys = int(request.POST.get('k'))
    link = str(request.POST.get('d'))
    # user = Userdata.objects.get(Id=keys)
    # print(user.Reason)
    #print(link)

    #print(A1,R1,T1,u1)
    if(A1=="true"):
        udata_info = Userdata(Decision =1,Reason = T1,Username = u1,Id = keys,flink=link)

    else:
        udata_info = Userdata(Decision=0, Reason=T1,Username = u1,Id = keys,flink=link)
    udata_info.save()

    return HttpResponse(T1)

def see_user(request):
    if (str(request.user) != "AnonymousUser"):
        if(request.user.is_staff):
            sam = User.objects.all()
            lst = []
            for i in sam:
                if (i.is_staff == False):
                    lst.append([i.username, i.password, i.email, i.first_name, i.last_name])
            #print(lst)
            return (render(request, 'see_user.html', {'l1': lst}))
        else:
            return (render(request, 'index.html'))
    else:
        return (render(request, 'index.html'))


def change_username(request):
    name = str(request.POST.get('name'))
    password = str(request.POST.get('password'))
    email = str(request.POST.get('email'))
    # print(name, password)
    u = User.objects.get(username=name);
    u.set_password(password);
    u.save()
    # email=request.user.email
    body="Hello "+name+","+"\n\n"+"Your Password is Updated by Admin"+"\n\n"+"Your New Login Credential for the National Level Article Competition are mention below:"+"\n\n"+"Username: "+name+"\n\n"+"Password:"+password+"\n\n"+"Login URL: http://udyat.pythonanywhere.com/"
    send_mail(
        'Article Competition CSI Id Password',
        body,
        'udyat@miet.ac.in',
        [email],
        fail_silently=False,
    )
    #print(u.password)
    return (HttpResponse("Done"))

def deleteuser(request):
    name = str(request.POST.get('name'))
    print(name)
    u = User.objects.get(username=name);
    u.delete()
    Assignedtask.objects.filter(checkername=name).delete()
    Userdata.objects.filter(Username=name).delete()

    return (HttpResponse("Done"))

def check_status(request):
    if (str(request.user) != "AnonymousUser"):
        if(request.user.is_staff):
            u1 = Userdata.objects.all().order_by('Id')
            paginator = Paginator(u1, 10)
            page = request.GET.get('page')
            u1 = paginator.get_page(page)

            return render(request, 'check_status.html', {'u1': u1})
        else:
            return (render(request, 'index.html'))
    else:
        return (render(request, 'index.html'))


def show_id(request):
    if (str(request.user) != "AnonymousUser"):
        if(request.user.is_staff):
            global df, l2

            l4 = []
            k = []
            df = pd.read_csv(csv_export_url)
            k1 = df.values.tolist()
            k.extend(k1)

            sam = User.objects.all()
            lst = []
            for i in sam:
                if (i.is_staff == False):
                    lst.append(i.username)

            for i in range(len(k)):
                file_url = "https://drive.google.com/open?id="
                l2 = file_url + k[i][7][33:]
                l4.append(l2)
            #print(l4)

            f = {'l4': l4}
            paginator = Paginator(f['l4'], 10)
            page = request.GET.get('page')
            f['l4'] = paginator.get_page(page)
            return (render(request, 'show_id.html', f))
        else:
            return (render(request,'index.html'))
    else:
        return (render(request, 'index.html'))


def change_password(request):
    if (str(request.user) != "AnonymousUser"):
        return (render(request, 'change_password.html'))
    else:
        return (render(request, 'index.html'))


def update_password(request):
    if (str(request.user) != "AnonymousUser"):
        p1 = str(request.POST['password1'])
        p2 = str(request.POST['password2'])
        if (p1 != p2):
            messages.error(request, "Password and Confirm Password must be Same !!!")
        else:
            name = str(request.user)
            u = User.objects.get(username=name);
            u.set_password(p1);
            u.save()
            messages.success(request, "Password Changed !!!")
            email=request.user.email
            body="Hello "+name+","+"\n\n"+"Your Password is Successfully Updated"+"\n\n"+"Your New Login Credential for the National Level Article Competition are mention below:"+"\n\n"+"Username: "+name+"\n\n"+"Password:"+p1+"\n\n"+"Login URL: http://udyat.pythonanywhere.com/"
            send_mail(
                'Article Competition CSI Id Password',
                body,
                'udyat@miet.ac.in',
                [email],
                fail_silently=False,
            )
        return (render(request, 'change_password.html'))
    else:
        return (render(request, 'index.html'))

def login_dashboard2(request):
    if (str(request.user) != "AnonymousUser"):
        if(request.user.is_staff):
            return (render(request, 'login_dashboard.html'))
        else:
            return (render(request,'user_dashboard.html'))
    else:
        return (render(request, 'index.html'))

def check_mail(request):
    subject=str(request.POST['subject'])
    body=str(request.POST['body'])
    u1 = Userdata.objects.all().order_by('Id')
    l=[]
    k=[]
    eid=[]
    all_comments=[]
    for i in u1:
        if i.Decision==1:
            l.append(i.Id)
            all_comments.append(i.Reason)
    df = pd.read_csv(csv_export_url)
    k1 = df.values.tolist()
    k.extend(k1)

    for j in range(len(l)):
        eid.append(k[l[j]-1][1])
    for i in range(len(eid)):
        send_mail(
            subject,
            body.format(comment=all_comments[i]),
            'udyat@miet.ac.in',
            [eid[i]],
            fail_silently=False,
        )
    return HttpResponse()

def check_mail1(request):
    subject=str(request.POST['subject'])
    body=str(request.POST['body'])
    u1 = Userdata.objects.all().order_by('Id')
    l=[]
    k=[]
    eid=[]
    df = pd.read_csv(csv_export_url)
    all_email=df['Email Address'].values.tolist()
    for i in u1:
        if i.Decision==1:
            l.append(i.Id)


    k1 = df.values.tolist()
    k.extend(k1)
    for j in range(len(l)):
        eid.append(k[l[j]-1][1])

    eid=list(set(all_email)-set(eid))
    send_mail(
        subject,
        body,
        'udyat@miet.ac.in',
        eid,
        fail_silently=False,
    )
    return HttpResponse()

def forgot_password(request):
    username = str(request.POST.get('name'))
    u = User.objects.get(username=username);

    s=''
    for i in range(8):
        s += a[r.randint(0, 75)]
    u.set_password(s);
    u.save()

    user = authenticate(username=username, password=s)
    login(request, user)
    email=request.user.email
    logout(request)
    subject = "MIET-CSI"
    body = f"""Hello {username},
Your Newly Genarated Password is {s} you can change it any time."""

    send_mail(
        subject,
        body,
        'udyat@miet.ac.in',
        [email],
        fail_silently=False,
    )
    return HttpResponse("done")

def About_us(request):
    return (render(request, 'About_us.html'))

def del_data(request):
    id = int(request.POST.get('id1'))
    Assignedtask.objects.filter(teamid=id).delete()
    Userdata.objects.filter(Id=id).delete()
    return HttpResponse()

def report(request):
    u1 = Userdata.objects.filter(Decision=1).order_by('Id')
    u2 = Userdata.objects.filter(Decision=0).order_by('Id')

    r = [i.Id for i in u2]

    df = pd.read_csv(csv_export_url)
    k1 = df.values.tolist()

    report_accept = []
    for i in u1:
        report_accept.append([k1[i.Id-1][2], k1[i.Id-1][1], k1[i.Id-1][3], k1[i.Id-1][4], k1[i.Id-1][5],i.Reason,i.Username])

    report_reject = []
    for i in u2:
        report_reject.append(
            [k1[i.Id - 1][2], k1[i.Id - 1][1], k1[i.Id - 1][3], k1[i.Id - 1][4], k1[i.Id - 1][5], i.Reason, i.Username])

    df1 = pd.DataFrame(report_accept, columns=["Name", "Email", "Contact No.", "College", "Title", "Comment", "Reviewer"])
    df2 = pd.DataFrame(report_reject,
                       columns=["Name", "Email", "Contact No.", "College", "Title", "Comment", "Reviewer"])
    a = df[["Name of Team Leader", "Email Address", "Phone No. of Team Leader",
            "Institute/Organization Name of Team Leader", "Title"]]
    d = {"Name of Team Leader": "Name", "Email Address": "Email", "Phone No. of Team Leader": "Contact No.",
         "Institute/Organization Name of Team Leader": "College", "Title": "Title"}
    a=a.rename(columns=d)
    writer = pd.ExcelWriter('static/report.xlsx', engine='xlsxwriter')
    a.to_excel(writer, sheet_name='All_Participants', index=False)
    df1.to_excel(writer, sheet_name='Accepted', index=False)
    df2.to_excel(writer, sheet_name='Rejected', index=False)

    writer.save()

    return HttpResponse()

def feedback(request):
    return (render(request, 'query.html'))