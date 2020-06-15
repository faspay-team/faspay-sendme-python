from FaspaySendme import Api

#Api.Services.enableProd(Api.Services)
#test = Api.Services.mutasi(Api.Services, {
#    "virtual_account" : "9920015307",
#    "start_date" : "2019-02-01",
#    "end_date" 	 : "2019-02-18"
#})

test = Api.Services.transfer(Api.Services, {
      "virtual_account" : "9920015307",
      "beneficiary_bank_code" : "alf",
      "beneficiary_region_code" : "0391",
      "beneficiary_country_code" : "ID",
      "beneficiary_purpose_code" : "1",
      "beneficiary_phone" : "092132132123",
      "beneficiary_email" : "ulin.nuha@faspay.co.id",
      "trx_no" : "431440034568",
      "trx_date" : "2020-10-13 14:16:00",
      "instruct_date" : "",
      "trx_amount" : "2500000",
      "trx_desc" : "Test Alfa",
      "callback_url" : "https://dev2.faspay.co.id/account/api/callback",
      "ktp_id" : "0123456449105144",
      "place_of_birth" : "Jakarta",
      "date_of_birth" : "1990-06-21",
      "gender" : "F",
      "citizenship" : "WNI",
      "occupation"  : "test",
      "trx_expired" : "",
      "address" : "jln pintu air Raya",
      "beneficiary_account_name" : "testtt"
})
print(test)