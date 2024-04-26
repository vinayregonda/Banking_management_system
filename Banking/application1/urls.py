from django.urls import path
from application1 import views


urlpatterns = [
    path('', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('newAccount/', views.newAccount, name='newAccount'),
    path('manageAccount/', views.manageAccount, name='manageAccount'),
    path('updateAccount/<int:pk>', views.updateAccount, name='updateAccount'),
    path('deleteAccount/<int:pk>', views.deleteAccount, name='deleteAccount'),
    path('announcement/', views.announcement, name='announcement'),
    path('newAnnouncement/', views.newAnnouncement, name='newAnnouncement'),
    path('updateAnnouncement/<int:pk>', views.updateAnnouncement, name='updateAnnouncement'),
    path('deleteAnnouncement/<int:pk>', views.deleteAnnouncement, name='deleteAnnouncement' ),
    path('transactions/', views.allTransactions, name='transactions'),
    path('userLogin/', views.userLogin, name='userLogin'),
    path('base.html/<int:id>/', views.base2, name='base'),
    path('userHome/<int:id>/', views.userHome, name='userHome'),
    path('myAccountupdate/', views.myAccountUpdate, name='myAccountupdate'),
    path('userSetting/', views.userSetting, name='userSetting'),
    path('userTransactions/<int:id>', views.userTransactions, name='userTransactions'),
    path('userDeposit/<int:id>/', views.userDeposit, name='userDeposit'),
    path('userWithdraw/<int:id>', views.userWithdarw, name='userWithdraw'),
    path('userTransfer/<int:id>', views.userTransfer, name='userTransfer'),
    path('logout/', views.logout_user, name='logout'),
    path('userLogout/', views.user_logout, name='userLogout')
]
