from django.utils.deprecation import MiddlewareMixin


class Row1(MiddlewareMixin):
    def process_request(self,requset):
        print('process_request1')

    def process_response(self,request,response):
        print('process_response1')
        return response
