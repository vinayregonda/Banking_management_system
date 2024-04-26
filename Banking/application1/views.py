from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib import auth
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm = request.POST.get('confirm_password')

        if password == confirm:
            if User.objects.filter(username=username).exists():
                print('username Exists.... Try with another Username')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    print('Email is already Exists.... Try with another Email')
                    return redirect('register')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password)
                    user.save()
                    return redirect('login')
        else:
            print('Password Did not match.... Please Choose the Correct one')
            return redirect('register')
    return render(request, 'register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            print("Login Successfull....")
            return redirect('home')
        else:
            print("Invalid Credentials")
            return redirect('login')
        
    return render(request, 'login.html')

@never_cache
@login_required(login_url='login')
def home(request):
    home = Account.objects.all()
    main = Account.objects.all().count()
    Bal = []
    
    for x in home:
        if x.beginingBalance not in Bal:
            Bal.append(x.beginingBalance)

    Tot = sum(Bal)
    balance = Tot


    context = {
        'home':home,
        'main':main,
        'balance': balance
    
    }
    return render(request, 'home.html', context)

@login_required(login_url='login')
def newAccount(request):
    newAccount = Account.objects.all()
    transaction = Transactions.objects.all()

    if request.method == 'POST'    :
        accountnumber = request.POST.get('AN')
        balance = request.POST.get('BB')
        # createdDate = request.POST.get('')

        new  = Transactions(
            account_id = accountnumber,
            Amount = balance
        )
        new.save()
    
    if request.method == 'POST':
        accountnumber = request.POST.get('AN')
        firstname = request.POST.get('FN')
        middlename = request.POST.get('MN')
        lastname = request.POST.get('LN')
        email = request.POST.get('EMAIL')
        password = request.POST.get('PS')
        pin = request.POST.get('PIN')
        beginingbalance = request.POST.get('BB')
        
        
        New = Account(
            accountNumber = accountnumber,
            firstName = firstname,
            middleName = middlename,
            lastName = lastname,
            Email = email,
            Password = password,
            Pin = pin,
            beginingBalance = beginingbalance

        )
        New.save()
        return redirect('manageAccount')

    context = {
        'newAccount' : newAccount,
    }
        
    return render(request, 'newAccount.html',context)

@never_cache
@login_required(login_url='login')
def manageAccount(request):
    manageAccount = Account.objects.all()

    page_num = request.GET.get('page')
    paginator = Paginator(manageAccount, 3)

    try:
        manageAccount = paginator.page(page_num)
    except PageNotAnInteger:
        manageAccount = paginator.page(1)
    except EmptyPage:
        manageAccount = paginator.page(paginator.num_pages)
        
    context = {
        'manageAccount' : manageAccount
    }
    return render(request, 'manageAccount.html', context)


@never_cache
@login_required(login_url='login')
def updateAccount(request,  pk):
    updateAccount = Account.objects.get(id=pk)
    if request.method == "POST":
        FirstName = request.POST.get('FirstName')
        MiddleName = request.POST.get('MiddleName')
        LastName = request.POST.get('LastName')
        mail = request.POST.get('E_MAIL')
        pin = request.POST.get('PIN')
        Account.objects.filter(id = pk).update(
            firstName = FirstName,
            middleName = MiddleName,
            lastName = LastName,
            Email = mail,
            Pin = pin,
            last_update=datetime.now()

        )
        return redirect('manageAccount')
    context = {
        'updateAccount':updateAccount
    }
    return render(request, 'updateAccount.html',context)


@never_cache
@login_required(login_url='login')
def deleteAccount(request, pk):
    Delete = Account.objects.get(id=pk)
    Delete.delete()
    return redirect('manageAccount')


@never_cache
@login_required(login_url='login')
def announcement(request):
    announcement = Announcement.objects.all()
    page_num = request.GET.get('page')
    paginator = Paginator(announcement, 2)

    try:
        announcement = paginator.page(page_num)
    except PageNotAnInteger:
        announcement = paginator.page(1)
    except EmptyPage:
        announcement = paginator.page(paginator.num_pages)
    
    context = {
        'announcement':announcement
    }    
    return render(request, 'announcement.html',context)

@never_cache
@login_required(login_url='login')
def newAnnouncement(request):
    announcement = Announcement.objects.all()
    if request.method == "POST":
        Title = request.POST.get('TITLE')
        Body = request.POST.get('BODY')
        Announcement(
            title = Title,
            body = Body,
        ).save()
        return redirect('announcement')
    context = {
        'announcement' : announcement
    }
    return render(request, 'newAnnouncement.html',context)


@never_cache
@login_required(login_url='login')
def  updateAnnouncement(request,pk):
    updateAnnouncement = Announcement.objects.get(id=pk)
    if request.method == "POST":
        Title =  request.POST.get('Title')
        Body = request.POST.get('Body')
        Announcement.objects.filter(id=pk).update(
            title = Title,
            body = Body
        )
        return redirect('announcement')
    context = {
        'updateAnnouncement':updateAnnouncement
    }
    return render(request, 'updateannouncement.html',context)


@never_cache
@login_required(login_url='login')
def deleteAnnouncement(request, pk):
    deleteAnnouncement = Announcement.objects.get(id = pk)
    deleteAnnouncement.delete()
    return redirect('announcement')


@never_cache
@login_required(login_url='login')
def allTransactions(request):
    ann = Transactions.objects.all()
    context = {
        'ann':ann
    }
    return render(request, 'Transactions.html', context)


@never_cache
def userLogin(request):
    if request.method == "POST" and "userlogin" in request.POST:
        email = request.POST.get('EMAIL')
        password = request.POST.get('password')
        accdetails=Account.objects.all()
        details=None
        for x in accdetails:
            if x.Email==email and x.Password==password:
                details=x.id
                print(details)
        print(details)
        if details:
            return redirect('base', details)
        else:
            return redirect('userLogin')
    return render(request, 'userLogin.html')
    


@never_cache

def base2(request,id):
    print(id)
    return render(request, 'base2.html',{'id':id})

@never_cache
def userHome(request,id):
    userHome = Account.objects.get(id=id)
    print(userHome,id)
    context = {
        'userHome':userHome,
        'id':id,
    }
    return render(request, 'userHome.html',context)

@never_cache
def myAccountUpdate(request):
    return render(request, 'myAccountupdate.html')

@never_cache
def userSetting(request):
    return render(request, 'userSetting.html')

@never_cache
def userTransactions(request,id):
    userTransactions = Account.objects.get(id=id)
    usertrans = Transactions.objects.filter(account_id=userTransactions.accountNumber)
    context = {
        'userTransactions':userTransactions,
        'id':id,
        'usertrans':usertrans,
    }
    return render(request, 'userTransactions.html',context)

@never_cache
def userDeposit(request,id):
    userDeposit = Account.objects.get(id=id)
    current_balence=userDeposit.beginingBalance
    if request.method == 'POST':
        deposit = request.POST.get('DAM')
        current_balence+=int(deposit)

        Account.objects.filter(id=id).update(
             beginingBalance = current_balence
        )
        Transactions(
            account_id=userDeposit.accountNumber,
            Transaction_type="DEPOSIT",
            Amount=deposit
        ).save()
        return redirect('userDeposit',id)
    context = {
        'userDeposit':userDeposit,
        'id':id,
    }
    return render(request, 'userDeposit.html',context)



@never_cache
def userWithdarw(request,id):
    userWithdarw = Account.objects.get(id=id)
    current_balance = userWithdarw.beginingBalance
    if request.method == 'POST':
        withdraw = request.POST.get('with')
        if int(withdraw) <= int(current_balance):
            current_balance-= int(withdraw)
            Account.objects.filter(id=id).update(
                beginingBalance = current_balance
            )
            Transactions(
                account_id=userWithdarw.accountNumber,
                Transaction_type="WITHDRAW",
                Amount=withdraw
            ).save()
            return redirect('userWithdraw', id)
        else:
            return redirect('userWithdraw', id)
        

    context = {
        'userWithdarw':userWithdarw,
        'id':id,
    }
    return render(request, 'userWithdraw.html',context)


@never_cache
def userTransfer(request,id):
    users = Account.objects.all()
    userTransfer = Account.objects.get(id=id)
    current_balance = userTransfer.beginingBalance
    if request.method == 'POST':
        account_number = request.POST.get('ACN')
        transfer = request.POST.get('transfer')
        
        acnumbers=[]
        for x in users:
            acnumbers.append(x.accountNumber)
        if (account_number in acnumbers) and account_number!=userTransfer.accountNumber:
                current_balance-= int(transfer)
                print(current_balance)
                Account.objects.filter(id=id).update(
                    beginingBalance = current_balance
                )
                amount=Account.objects.get(accountNumber=account_number)
                finalamount=int(amount.beginingBalance)+int(transfer)
                Account.objects.filter(accountNumber=account_number).update(
                    beginingBalance = finalamount
                )
                Transactions(
                    account_id = userTransfer.accountNumber,
                    Transaction_type = 'Transfer',
                    Amount = transfer
                ).save()
                
        else:
            return redirect('userTransfer', id)
        
        return redirect('userTransfer', id)
    context = {
        'userTransfer':userTransfer,
        'id':id,
        'users':users
        
    }
    return render(request, 'userTransfer.html',context)
    

@never_cache
def logout_user(request):
    logout(request)
    return render(request,'login.html')

@never_cache
def user_logout(request):
    logout(request)
    return render(request, 'userLogin.html')