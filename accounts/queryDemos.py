#(1)
customers = Customer.objects.all()

#(2)
firstCustomer = Customer.objects.first()

#(3)
lastCustomer = Customer.objects.last()

#(4)
customerByName = Customer.objects.get(name='Peter Piper')

#(5)
customerById = Customer.objects.get(id=2)

#(6)
firstCustomer.order_set.all()

#(7)
order = Order.objects.first() 
parentName = order.customer.name

#(8)
products = Product.objects.filter(category="Out Door")

#(9)
leastToGreatest = Product.objects.all().order_by('id') 
greatestToLeast = Product.objects.all().order_by('-id') 


#(10) 
productsFiltered = Product.objects.filter(tags__name="Sports")

#Returns total count for each product orderd
allOrders = {}

for order in firstCustomer.order_set.all():
	if order.product.name in allOrders:
		allOrders[order.product.name] += 1
	else:
		allOrders[order.product.name] = 1
        
#RELATED SET EXAMPLE
class ParentModel(models.Model):
	name = models.CharField(max_length=200, null=True)

class ChildModel(models.Model):
	parent = models.ForeignKey(Customer)
	name = models.CharField(max_length=200, null=True)

parent = ParentModel.objects.first()
#Returns all child models related to parent
parent.childmodel_set.all()