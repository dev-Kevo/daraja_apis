from requests import Response

class MpesaResponse(Response):
    response_id = ''
    response_code = ''
    response_description = ''
    customer_message = ''
    conversion_id = ''
    originator_conversion_id = ''
    error_code = ''
    error_message = ''
    merchant_request_id = ''
    checkout_request_id = ''

def mpesa_response(response):
    """
    Create Mpesa Response from Push Response
    Args:
        response:
            rsponse object from the push notification =
    """

    response.__class__ = MpesaResponse
    json_reponse = response.json()
    response.response_id = json_reponse.get('requestId', '')
    response.response_code = json_reponse.get('ResponseCode', '')
    response.response_description = json_reponse.get('ResponseDescription', '')
    response.customer_message = json_reponse.get('CustomerMessage', '')
    response.conversion_id = json_reponse.get('ConversationID', '')
    response.originator_conversion_id = json_reponse.get('OriginatorConversationID', '')
    response.error_code = json_reponse.get('errorCode', '')
    response.error_message = json_reponse.get('errorMessage')
    response.merchant_request_id = json_reponse.get('MerchantRequestID', '')
    response.checkout_request_id = json_reponse.get('CheckoutRequestID', '')

    return response

    


