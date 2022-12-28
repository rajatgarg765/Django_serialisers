import json
from django.contrib.auth.models import User

class SimpleMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        # One-time configuration and initialization.

    def __call__(self, request):
        
        print("###############################################################")
        print("before view")

        response = self.get_response(request)

        print("after view")
        print("###############################################################")

        return response



        # if 'api' in request.path and 'admin' not in request.path:
        #     choice_dct = dict()
        #     choice_dct['rooms'] = 1
        #     choice_dct['digir'] = 2
        #     choice_dct['other'] = 3

        #     #default api_choice other
        #     api_choice = choice_dct['other']
        #     request_ip = get_client_ip(request)
        #     try:
        #         request_json = request.body.decode('utf-8')
        #         request_json = json.loads(request_json)
                
        #     except:
        #         request_json = None
            

        #     for val in choice_dct.keys():
        #         if val in request.path:
        #             api_choice = choice_dct[val]
        #             break
            

        #     res_status = response.status_code
            
        #     if res_status ==200:
        #         status_choice = 2
        #     else:
        #         status_choice = 1

        #     print(request_json, request_ip,res_status, api_choice," ", status_choice,response.data)

        #     if request.user.is_anonymous:
        #         print("anonymous")

        #     if 'api' in request.path:
        #         print("API")

            
        #     try:
        #         if request.user.is_anonymous:
        #             CreativeRAPILog.objects.create(user_ip=request_ip,user_request = request_json,response = response.data, request_api=api_choice,request_status= status_choice)
        #             print("hi")

        #         else:
        #             CreativeRAPILog.objects.create(user = request.user, user_request = request_json, user_ip=request_ip, response = response.data, request_api=api_choice,request_status= status_choice)
        #     except Exception as e:
        #         print("Exception is ",e)