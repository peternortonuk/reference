# https://www.youtube.com/watch?v=EiOglTERPEo


class DoughFactory(object):
    def order_pizza(self, *toppings):
        print('not supposed to run')

    def get_dough(self):
        return 'insecticide treated wheat dough'


class Pizza(DoughFactory):

    def order_pizza1(self, *toppings):
        print('Getting dough')
        dough = super(Pizza, self).get_dough()
        print('Making pie with %s' % dough)
        for topping in toppings:
            print('Adding: %s' % topping)


class OrganicDoughFactory(DoughFactory):
    def get_dough(self):
        return 'pure untreated wheat dough'


class OrganicPizza(Pizza, OrganicDoughFactory):
    pass


if __name__ == '__main__':
    Pizza().order_pizza('Pepperoni', 'Bell Pepper')
    print('========')
    OrganicPizza().order_pizza('Sausage', 'Mushroom')
    pass





