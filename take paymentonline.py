#step 1 : take the upi id from user
#step2: payment url define
# step 3: generate QR code
# step 4: can save also 
# step 5:  to display using pillow

import qrcode
upi_id = input("Enter your UPI ID= ")

#Defining the payment URL based on the UPI ID and the payment app
# can modify these URLS on the payment app yo want to support

phonepe_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#CARETE QR CODE FO EACH PAYMENT

phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save the RE code
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#Display QR USING PILLOW LIB
phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()

