from django.test import TestCase
from .models import Item, Comment
# Create your tests here.

class ItemTestCase(TestCase):
    
    def setUp(slef):
        
        #Create an Item
       a1 = Item.objects.create(title="phone", manager="harry") 
       a2 = Item.objects.create(title="book", manager="cong")
       
       #Creaet a comment
       Comment.objectsj.create()