class MobileOrFullMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        #request.mobile вылетает ошибка. сделал по своему
        if request.headers._store.get('sec-ch-ua-mobile')[1] != '?0':
            prefix = "mobile/"
        else:
            prefix = "full/"
        
        if type(response.template_name) == list:
            #генерация ошибки ERROR
            response.template_name = prefix + response.template_name[0] #+ sdasd 
     
        return response