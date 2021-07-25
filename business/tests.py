from django.test import TestCase
from .models import Business ,Neighbourhood , Profile

# Create your tests here.
class BusinessTestClass(TestCase):
    def setUp(self) :
        self.business = Business(business_name = 'business')

    def test_instance(self):
        self.assertTrue(isinstance(self.business , Business))

    def test_save_method(self):
        self.business.save_business()
        business = Business.objects.all()
        self.assertTrue(len(business) >0)

    def test_delete_method(self):
        self.business.save_business()
        business = Business.objects.all()
        self.business.objects.filter(id = self.business.id).delete()