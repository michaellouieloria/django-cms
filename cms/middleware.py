class HeaderMiddleware(object):

    def process_response(self, request, response):
        response['X-Permitted-Cross-Domain-Policies'] = 'master-only'
        response['X-UA-Compatible'] = 'IE=edge,chrome=1'
        response['Server'] = 'Server'
        return response
