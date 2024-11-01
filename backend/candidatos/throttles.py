from rest_framework.throttling import AnonRateThrottle

class CurriculoAnonRateThrottle(AnonRateThrottle):
    rate = '5/day'