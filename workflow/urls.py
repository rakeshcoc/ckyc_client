
from django.conf.urls import url,include
from django.urls import path
from workflow import views
from .views import fetch_by_ckyc

app_name = 'workflow'
urlpatterns = [
#path('onboard/',onboard.as_view(),name="onboard"),
#path('update/',update.as_view(),name="update"),
path('',views.home,name ="home"),
path('mod_form/',views.mod_form,name='mod_form'),
path('login-success/',views.login_success),
path('check_did1/',views.update_check_did,name="check_did1"),
path('check_did2/',views.update_check_did2,name="check_did2"),
path('check_did1/updateform1/',views.form_update,name="updateform1"),
path('updatehtmlform1/',views.update_html_form1,name="updatehtmlform1"),
path('forgot/',views.forgot,name='forgot'),
path('fetchform/',views.fetch_form,name='fetchform'),
path('check_did2/fetchform1/',views.fetch,name='fetch'),
# path('fetch/',views.fetch,name='fetch'),
path('fetch_by_ckyc/',fetch_by_ckyc.as_view(),name ="fetch_by_ckyc"),
path('check_txn_form/',views.check_txn_form,name="check_txn_form"),
path('fetch_txn_status/',views.fetch_txn_status,name='fetch_txn_status'),
path('pending-txns/',views.Pending_txns,name='pending-txns'),
path('view-txn-details/<str:txn_id>/',views.view_txn_details,name='view-txn-details'),
path('accept_txn_details/<str:txn_id>/',views.accept_txn_details,name='accept_txn_details'),
path('reject_txn_details/<str:txn_id>/',views.reject_txn_details,name='reject_txn_details')

]
#/login-success