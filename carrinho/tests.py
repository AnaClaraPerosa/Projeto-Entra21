from django.test import TestCase

# Create your tests here.
#teste

from clientes.models import Clientes

class Teste(TestCase):

    @classmethod
    def setUpTestData(cls):
        print("setUpTestData: Run once.")
        pass

    def setUp(self):
        print("setUp: Run once ...setup clean data.")
        pass
    


    def ProcuraUser(self):

        cli = Clientes.objects.filter(usuario_id=7)

        if (cli):
            print ("achou cli")
        else: 
            print ("nao achou ")

        for x in cli.values():
            print(x["usuario_id"])
            print(x["cliente_nome"])

        # print (cli.usuario)


x = Teste()
x.ProcuraUser()