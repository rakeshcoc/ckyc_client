from django.shortcuts import render,redirect
from rest_framework.views import APIView
from django.http import HttpResponse, HttpResponseRedirect,JsonResponse
from rest_framework.response import Response
from rest_framework import status
import hashlib,json,workflow.connect,datetime,base64,requests,uuid,os,random,ast,workflow.final_connect,workflow.parser
from collections import OrderedDict
from django.contrib.auth.decorators import login_required 
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from subprocess import call
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from collections import OrderedDict
from django.contrib.auth.forms import UserCreationForm
from .models import txn_flow
from django.conf import settings

@login_required
def login_success(request):
	print(request.user.is_maker,'request.user.is_maker')
	print(request.user.is_checker,'request.user.is_checker')
	if request.user.is_maker:
		return HttpResponseRedirect('/')
	elif request.user.is_checker:
		return HttpResponseRedirect('/')
	else:
		return HttpResponse("Hello in future")


def generateTxnId(d_id,time_c):
    st1=str(d_id)+str(time_c)
    st1en=st1.encode()
    update_txn_id = int(hashlib.sha256(st1en).hexdigest(), 16) % (10 ** 8)
    return update_txn_id
# Create your views here.
BankName = settings.BANK_NAME
mytoken='Token '+settings.CKYC_AUTH_TOKEN
url = "http://"+settings.CENTRAL_SERVER+":8000/ckyc-api/"
Blockchain_url = settings.BLOCKCHAIN_URL
token = settings.CKYC_AUTH_TOKEN
kfield,ofield,prooffield = workflow.parser.field()
status =["Submitted","Verification Failed","Verified","Rejected","Approved"]
call('python3 xml_to_html/py_file/field.py',shell=True)
call('python3 xml_to_html/py_file/update.py',shell=True)
call('python3 xml_to_html/py_file/forgot.py',shell=True)

@login_required(login_url="/login/")
def home(request):
	return render(request,'workflow/home.html')

def Pending_txns(request):
	if request.user.is_checker:
		plist = txn_flow.objects.filter(status=status[0])
		return render(request,'workflow/plist.html',{'plist':plist})
	else:
		result ="You are not authorized"
		return render(request,'onboard/success.html',{'abc':result})

def accept_txn_details(request,txn_id):                                    #send_to_chain
		try:
			val=None
			digital_id =""
			count = workflow.connect.retrieve_info_by_key(txn_id)
			if count == 0:
				result = "Not Found"
			else:
				for i in count['value']:
					digital_id = i['header']['digital_id']
					val=i
				txn_type = count['type']
				time = (datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
				payload ={"created_user":mytoken,"status":status[2],"txn_id":txn_id,"remarks":""}
				requests.put(url=url+"txn-status/"+txn_id+"/",data=payload,headers={'Authorization':mytoken})
				payload = {      'digital_identity' : digital_id,'last_modified_by':mytoken,'last_update_time':time}
				if txn_type == "new":
					r = requests.post(url = url,data=payload,headers={'Authorization':mytoken})
					if r.status_code == 201:
						txn_flow.objects.filter(txn_id=txn_id).update(status=status[2])
						payload ={"created_user":mytoken,"status":status[4],"txn_id":txn_id,"remarks":""}
						data =eval(eval(r.content.decode()))
						val['header']['updated_txn_id'] = data["result"]["updated_txn_id"]
						workflow.final_connect.update_db(digital_id,val)

						print("********** ADD IN CHAIN *************")
						chain_payload = {"ckycId":data["result"]["digital_id"],"bankName":data["result"]["bankName"],
						"ckyctxId":data["result"]["updated_txn_id"],"ckyctimestamp":data["result"]["timestamp"],"ckycStatus":data["result"]["status"]}
						print(chain_payload)
						try:
							# New insert to chain, please make sure url is working.
							requests.post(url = Blockchain_url+"/ckyc/transactions",json=chain_payload)
							print(" Record added to chain")	
						except :
							print(" Chain_Link not found, so record not added to chain")


						txn_flow.objects.filter(txn_id=txn_id).update(status=status[4])
						requests.put(url=url+"txn-status/"+txn_id+"/",data=payload,headers={'Authorization':mytoken})
						result ="Txn_id: "+str(txn_id) + "Status: Approved "

					elif r.status_code == 409:
						payload ={"created_user":mytoken,"status":status[3],"txn_id":txn_id,"remarks":"Digtal-Id already created"}
						requests.put(url=url+"txn-status/"+txn_id+"/",data=payload,headers={'Authorization':mytoken})
						txn_flow.objects.filter(txn_id=txn_id).update(status=status[3],remarks="Digtal-Id already created")
						result ="Txn_id: "+str(txn_id) + "Status: Rejected as DigitalId already registered"
				else:
					url1 = url[0:-1]+"-update/"
					r = requests.post(url = url1,data=payload,headers={'Authorization':mytoken})
					if r.status_code == 201:
						txn_flow.objects.filter(txn_id=txn_id).update(status=status[2])
						payload ={"created_user":mytoken,"status":status[4],"txn_id":txn_id,"remarks":""}
						data =eval(eval(r.content.decode()))
						t =data["result"]["updated_txn_id"]
						val['header'].update({'updated_txn_id': t})
						workflow.final_connect.update_db(digital_id,val)

						print("********** Update IN CHAIN *******")
						chain_payload = {"ckycId":data["result"]["digital_id"],"bankName":data["result"]["bankName"],
						"ckyctxId":data["result"]["updated_txn_id"],"ckyctimestamp":data["result"]["timestamp"],"ckycStatus":data["result"]["status"]}
						print(chain_payload)
						try:
							# Update to chain, please make sure url is working.
							requests.post(url = Blockchain_url+"/ckyc/transactions/update",json=chain_payload)
							print(" Record updated to chain")	
						except :
							print(" Chain_Link not found, so record not updated to chain")
						txn_flow.objects.filter(txn_id=txn_id).update(status=status[4])
						requests.put(url=url+"txn-status/"+txn_id+"/",data=payload,headers={'Authorization':mytoken})
						result ="Txn_id: "+str(txn_id) + "Status: Approved "
					# return render(request,'onboard/success.html',{'abc':result})

		except Exception as e:
			return e
		return render(request,"onboard/approved.html",{"abc":result})

def reject_txn_details(request,txn_id):
	result = "txn_id"
	payload ={"created_user":mytoken,"status":status[1],"txn_id":txn_id,"remarks":""}
	x = requests.put(url=url+"txn-status/"+txn_id+"/",data=payload,headers={'Authorization':mytoken})
	txn_flow.objects.filter(txn_id=txn_id).update(status=status[1])
	result = "Txn_id: "+str(txn_id) + "Status: Verification Failed "
	return render(request,"onboard/approved.html",{"abc":result})


def view_txn_details(request,txn_id):
	if request.user.is_checker:
		count = workflow.connect.retrieve_info_by_key(txn_id)
		if count == 0:
			result = "Not Found"
		else:
			for i in count['value']:
				x = i['body']
			profilePhoto ={}
			profileBuild ={}
			for i in prooffield:
				if i in x:
					profilePhoto[i] = x[i].decode()


			for i in kfield:
				if i in x:
					profileBuild[i] = x[i]

			for i in ofield:
				if i in x:
					profileBuild[i] = x[i]

			mapping = x['mapping']
			return render(request,'workflow/view_txn_details.html',{"finalprofile":profileBuild,"profilePhoto":profilePhoto,"txn_id":txn_id,"mapping":mapping})
	else:
		result ="You are not authorized"
		return render(request,'onboard/success.html',{'abc':result})

@login_required(login_url="/login/")
def mod_form(request):
	if request.method == "GET":
		return render(request,'onboard/choose_doc_2.html')
	else:
		key = ""
		for i in kfield:
			key = key + request.POST[i]
		d_id = int(hashlib.sha256(key.encode()).hexdigest(), 16) % (10 ** 12)
		digital_id = int(str(d_id).rstrip("L"))
		temp_id = uuid.uuid3(uuid.NAMESPACE_DNS, str(digital_id))
		digitalId = str(temp_id).replace('-', '')
		digital_id =digitalId.upper()[:12]
		body ={}
		header = {}
		t = request.POST['map']
		mapping =eval(t)['myMap']
		print(mapping) 
		for i in kfield:
			value = request.POST[i]
			body.update({i:value})
		for i in ofield:
			value = request.POST[i]
			if value is not "":
				body.update({i : value})
		body['mapping'] = mapping
		for i in prooffield:
			try:
				data = request.FILES[i]
			except:
				data = ""
			if data is not "":
				tmp = os.path.join(settings.MEDIA_ROOT, "tmp", data.name)
				path = default_storage.save(tmp, ContentFile(data.read()))
				with open("media/tmp/"+str(data.name), "rb") as imageFile:
					str1 = base64.b64encode(imageFile.read())
					type(str1)
					body.update({i:str1})
			else:
				pass
		time = (datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
		payload = {      'digital_identity' : digital_id,
      					'last_modified_by':mytoken,
      					'last_update_time':time
				}
		try:
			if workflow.final_connect.localfind(str(digital_id)) > 0:
				result ="Account is already registered with token Id "+str(digital_id)
				return render(request,'onboard/success.html',{'abc':result})

			#  CHECK CHAIN already have registered digital_id or not
			elif requests.post(url = Blockchain_url+"/ckyc/transactions/ckycId",json={"ckycId":digital_id}).status_code == 200 :
			# elif requests.get(url = url+"users/"+str(digital_id)+"/",headers={'Authorization':mytoken}).status_code == 200 :
				result ="You are already registered,please goto update section if want to update"
				return render(request,'onboard/success.html',{'abc':result})

			else:
				trans_id =generateTxnId(digital_id,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
				workflow_txn_id = BankName.upper() + str(trans_id)
				header.update({"Updated_by":BankName,"Last_updated":time,"workflow_txn_id":workflow_txn_id,"digital_id":digital_id})
				detail = {"header":header,"body":body}
				payload ={"created_user":mytoken,"status":status[0],"txn_id":workflow_txn_id,"remarks":""}
				if requests.post(url=url+"txn-status/",data=payload,headers={'Authorization':mytoken}).status_code == 201:
					txn_flow.objects.create(status=status[0],txn_id=workflow_txn_id,digital_id=digital_id)
					workflow.connect.to_db(workflow_txn_id,detail,status[0],"new")
					call('rm media/tmp/*',shell=True)
					result = "Transaction-Id "+str(workflow_txn_id)+ " is created for future reference"
				else:
					result ="Not able to post payload on server"
				return render(request,'onboard/success.html',{'abc':result,})

		except Exception as e:
			result = e
			return render(request,'onboard/success.html',{'abc':result,})



@login_required(login_url="/login/")
def update_check_did(request):
	if request.method == 'GET':
		digital_id =request.GET["digital_id"]
		if workflow.final_connect.localfind(digital_id) > 0 :
			result ="Your Digital Id is:"+str(digital_id)

		#  CHECK CHAIN already have registered digital_id or not
		elif requests.post(url = Blockchain_url+"/ckyc/transactions/ckycId",json={"ckycId":digital_id}).status_code == 200 :
		# elif (requests.get(url = url+"users/"+str(digital_id)+"/",headers={'Authorization':mytoken})).status_code == 200 :
			result ="Success" + " "+str(digital_id)

		#  Ensure BLOCKCHAIN server is up and running
		elif requests.post(url = Blockchain_url+"/ckyc/transactions/ckycId",json={"ckycId":digital_id}).status_code == 503 :
		# elif (requests.get(url = url+"users/"+str(digital_id)+"/",headers={'Authorization':mytoken})).status_code == 503 :
			result ="Central Server Down"
			return render(request,'onboard/success.html',{'abc':result,})
		else:
			result ="Sorry no record found"
			return render(request,'onboard/success.html',{'abc':result,})
		request.session['digital_id'] = digital_id
		return redirect("updateform1/")


@login_required(login_url="/login/")
def update_html_form1(request):
	if request.method == 'GET':
		return render(request,'userprofile/update.html')


def form_update(request):
	if request.method == 'GET':
		key=None
		if request.session.has_key('digital_id'):
			digital_id = request.session['digital_id']
		return render(request,'onboard/update.html',{"digital_id":digital_id, })
	else:
		try:
			if request.session.has_key('digital_id'):
				digital_id = request.session['digital_id']
			del request.session['digital_id']
			body ={}
			header ={}
			t = request.POST['map']
			mapping =eval(t)['myMap']
			body['mapping'] = mapping
			for i in ofield:
				value = request.POST[i]
				if value is not "":
					body.update({i : value})
			for i in prooffield:
				try:
					data = request.FILES[i]
				except:
					data = ""
				if data is not "":
					print(data)
					tmp = os.path.join(settings.MEDIA_ROOT, "tmp", data.name)
					path = default_storage.save(tmp, ContentFile(data.read()))
					with open("media/tmp/"+str(data), "rb") as imageFile:
						str1 = base64.b64encode(imageFile.read())
						body.update({i:str1})
				else:
					pass
			time = (datetime.datetime.now().strftime("%m/%d/%Y, %H:%M:%S"))
			trans_id =generateTxnId(digital_id,datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
			workflow_txn_id = BankName.upper() + str(trans_id)
			header.update({"Updated_by":BankName,"Last_updated":time,"workflow_txn_id":workflow_txn_id,"digital_id":digital_id})
			detail = {"header":header,"body":body}
			payload ={"created_user":mytoken,"status":status[0],"txn_id":workflow_txn_id,"remarks":""}
			if requests.post(url=url+"txn-status/",data=payload,headers={'Authorization':mytoken}).status_code == 201:
				txn_flow.objects.create(status=status[0],txn_id=workflow_txn_id,digital_id=digital_id)
				workflow.connect.to_db(workflow_txn_id,detail,status[0],"update")
				call('rm media/tmp/*',shell=True)
				result = "Transaction-Id "+str(workflow_txn_id)+ " is created for future reference"
				trans_id = trans_id+1
			else:
				result ="Not able to post payload on server"
			return render(request,'onboard/success.html',{'abc':result,})
		except Exception as e:
			result = e
			return render(request,'onboard/success.html',{'abc':result,})

@login_required(login_url="/login/")
def forgot(request):
	if request.method == 'GET':
		return render(request,'onboard/forgot.html')
	else:
		key =""
		try:
			for i in kfield:
				key = key + request.POST[i]
			print(key)
			d_id = int(hashlib.sha256(key.encode()).hexdigest(), 16) % (10 ** 12)
			digital_id = int(str(d_id).rstrip("L"))
			temp_id = uuid.uuid3(uuid.NAMESPACE_DNS, str(digital_id))
			digitalId = str(temp_id).replace('-', '')
			digital_id =digitalId.upper()[:12]
			if workflow.final_connect.localfind(digital_id) > 0 :
				result ="Your Digital Id is:"+str(digital_id)

			#  CHECK CHAIN already contains given registered digital_id or not
			elif requests.post(url = Blockchain_url+"/ckyc/transactions/ckycId",json={"ckycId":digital_id}).status_code == 200 :
			# elif (requests.get(url = url+"users/"+str(digital_id)+"/",headers={'Authorization':mytoken})).status_code == 200 :
				result ="Success" + " "+str(digital_id)
			else:
				result ="Sorry no record found"
		except Exception as e:
			result = str(e)
		return render(request,'onboard/success.html',{'abc':result,})

@login_required(login_url="/login/")
def fetch_form(request):
	if request.method == 'GET':
		return render(request,'userprofile/fetch.html')

@login_required(login_url="/login/")
def update_check_did2(request):
	if request.method == 'GET':
		digital_id =request.GET["digital_id"]

		#  CHECK CHAIN already have registered digital_id or not
		r =requests.post(url = Blockchain_url+"/ckyc/transactions/ckycId",json={"ckycId":digital_id})
		# r =requests.get(url = url+"users/"+str(digital_id)+"/",headers={'Authorization':mytoken})
		if r.status_code == 200 :
			result ="Success" + " "+str(digital_id)
		elif r.status_code == 503:
			result ="Central Server Down"
			return render(request,'onboard/success.html',{'abc':result,})

		else:
			print(r.status_code)
			result ="Sorry Digital-Id not found"
			return render(request,'onboard/success.html',{'abc':result,})
		request.session['digital_id1'] = digital_id
		return redirect("fetchform1/")

@login_required(login_url="/login/")
def fetch(request):
	if request.method == 'GET':
		finalprofile = OrderedDict()
		call('rm media/decode/*',shell=True)
		try:			
			for i in kfield:
				finalprofile.update({i:""})
			for j in ofield:
				finalprofile.update({j:""})
			for k in prooffield:
				finalprofile.update({k:""})
			finalprofile['mapping'] = {}
			digital_id =""
			if request.session.has_key('digital_id1'):
				digital_id = request.session['digital_id1']
			del request.session['digital_id1']
			x = url+"fetch/"+str(digital_id)+"/"
			r =requests.get(url=x,headers={'Authorization':mytoken})
			print(r.status_code)
			if r.status_code != 503:
				data = eval(r.content.decode())
				orderingData = data["ckyc_ordering"]	
				membersData = data["membersData"]
				for i in reversed(orderingData):
					for j in membersData[i['bank']]['value']:
						if j['header']['updated_txn_id'] == i['txn_id']:
							for k in j['body']:
								if k != "mapping" and finalprofile[k] == "":
									finalprofile[k] = j['body'][k]
								elif k == "mapping":
									for t in j['body'][k]:
										finalprofile[k][t] = j['body'][k][t]

				profileBuild ={}
				profilePhoto = {}
				for i in prooffield:
					if i in finalprofile and finalprofile[i]!="":
						profilePhoto[i] = finalprofile[i]

				for i in kfield:
					profileBuild[i] = finalprofile[i]
				for i in ofield:
					profileBuild[i] = finalprofile[i]
				mapping = finalprofile['mapping']
				return render(request,'userprofile/profile.html',{'finalprofile':profileBuild,'profilePhoto':profilePhoto,'mapping':mapping,})
			elif r.status_code == 503:
				result = "One of local servers are down. So, can't make full profile"
			else:
				result ="Something went wrong"
		except Exception as e:
			result = str(e)
		return render(request,'onboard/success.html',{'abc':result,})

class fetch_by_ckyc(APIView):
	def post(self,request):
		try:
			key = request.data["digital_id"]
			j=workflow.final_connect.retrieve_info_by_seq(key)
			if j == 0:
				j = {"msg":"Invalid Digital Id"}
				return Response(j,status=status.HTTP_404_NOT_FOUND)
			else:
				for i in j['value']:
					print(type(i))
				return Response(j)
		except:
			return HttpResponse("Some error occurred, please try again with proper fields",status=status.HTTP_400_BAD_REQUEST)

@login_required(login_url="/login/")
def check_txn_form(request):
	if request.method == 'GET':
		return render(request,'userprofile/check_txn_form.html')

@login_required(login_url="/login/")
def fetch_txn_status(request):
	if request.method == "GET":
		try:
			txn_id = request.GET['txn_id']
			x = txn_flow.objects.filter(txn_id=txn_id)
			result =""
			if len(x) == 0:										#local db search unsuccessfull
				r = requests.get(url=url+"txn-status/"+txn_id+"/",headers={'Authorization':mytoken})
				if r.status_code == 200:
					data = (r.content.decode())
					data1 = json.loads(data)															#Convert json response from ckyc-server to dict
					result = "Status : "+str(data1["status"]).upper()+" , Transaction Id "+txn_id+" , Remarks: "+str(data1["remarks"]).upper()

				else:																	#record not on localdb or ckyc-server
					result = "Txn-id not found"
			else:
				for i in x:																		#localdb-search successfull 
					if i.status == status[4]:
						result = "Status : "+(i.status).upper()+" , Transaction Id "+txn_id+"\n\nDigital_Id:"+str(i.digital_id)
					else:
						result = "Status : "+(i.status).upper()+" , Transaction Id "+txn_id+" , Remarks: "+str(i.remarks).upper()
		
			return render(request,'onboard/success.html',{'abc':result,})
		except Exception as e:
			result = str(e)
			return render(request,'onboard/success.html',{'abc':result,})

