from FaspaySendme import Api

#Api.Services.enableProd(Api.Services)
#test = Api.Services.mutasi(Api.Services, {
#    "virtual_account" : "9920015307",
#    "start_date" : "2019-02-01",
#    "end_date" 	 : "2019-02-18"
#})

test = Api.Services.transfer(Api.Services, {
  "virtual_account": "9920003365",
  "beneficiary_bank_code": "alf",
  "beneficiary_region_code": "0391",
  "beneficiary_country_code": "ID",
  "beneficiary_purpose_code": "1",
  "beneficiary_phone": "081311555551",
  "beneficiary_email": "reky@datacell.id",
  "trx_no": "001",
  "trx_date": "2020-06-16 16:06:00",
  "instruct_date": "",
  "trx_amount": "100000",
  "trx_desc": "Test Alfa",
  "callback_url": "https://postb.in/b/1592269578457-5281115856487",
  "ktp_id": "1122334455667788",
  "place_of_birth": "Jakarta",
  "date_of_birth": "1990-06-21",
  "gender": "F",
  "citizenship": "WNI",
  "occupation": "Karyawan",
  "trx_expired": "",
  "address": "Jl Alam Asri Indah nomer 36, Cimahi Utara",
  "beneficiary_account_name": "Ocha"
})
print(test)