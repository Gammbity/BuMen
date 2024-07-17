from rest_framework.throttling import UserRateThrottle

class CreateContactAppNumThrottle(UserRateThrottle):
    rate = '2/h'
    scope = 'create_contact_application'

    def get_cache_key(self, request, view):
        return request.data.get('phone')
    
class CreateContactAppIPThrottle(UserRateThrottle):
    rate = '2/h'
    scope = 'create_contact_application'

    

