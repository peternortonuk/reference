'''
Raymond Hettinger - Super considered super! - PyCon 2015
https://www.youtube.com/watch?v=EiOglTERPEo

mro rules simplified:
(1) Subclasses appear before base classes
(2) Base class declaration order is preserved
(3) For all classes in an inheritance graph, the relative orderings guaranteed by 1 and 2 are preserved at all points in the graph.
https://sixty-north.com/blog/method-resolution-order-c3-and-super-proxies.html
'''


class DoughFactory(object):
    def order_pizza(self, *toppings):
        print('this never gets called')

    def get_dough(self):
        return 'insecticide treated wheat dough'


class Pizza(DoughFactory):

    def order_pizza(self, *toppings):
        print('Getting dough')
        dough = super(Pizza, self).get_dough()
        print('Making pie with %s' % dough)
        for topping in toppings:
            print('Adding: %s' % topping)


class OrganicDoughFactory(DoughFactory):
    def get_dough(self):
        return 'pure untreated wheat dough'


# is this dependency injection? we're changing the mro
# which changes which get_dough method gets called
class OrganicPizza(Pizza, OrganicDoughFactory):
    pass


if __name__ == '__main__':
    # the super of Pizza is DoughFactory
    print(Pizza.__mro__)
    Pizza().order_pizza('Pepperoni', 'Bell Pepper')
    print

    # now the super of Pizza is OrganicDoughFactory
    print(OrganicPizza.__mro__)
    OrganicPizza().order_pizza('Sausage', 'Mushroom')
    pass





