from kavenegar import *


def send_otp_code(phone_number,code):
    try:
        api = KavenegarAPI('Null')
        params = {
            'sender': '',  # optional
            'receptor': phone_number,  # multiple mobile number, split by comma
            'message': f'{code}کد تایید شما ',
        }
        response = api.sms_send(params)
        print(response)
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)