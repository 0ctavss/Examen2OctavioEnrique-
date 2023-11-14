import unittest
from Examen2 import MiClase
objeto = MiClase(5, 120, 12, ["Canción 1", "Canción 2", "Canción 3"], [0.8, 0.9, 0.7])
class TestCocinero(unittest.TestCase):

    def test_ObtieneValencia(self):
        self.assertEqual(objeto.ObtieneValencia(120), 1)

    def test_ObtieneValencia2 (self):
        self.assertEqual(objeto.ObtieneValencia(13333), 5)
    
    def test_DivisibleTempo (self):
        self.assertEqual(objeto.DivisibleTempo(5), [1,5])

    def test_DivisibleTempo2 (self):
        self.assertEqual(objeto.DivisibleTempo(21), [1,3,7,21])

    def test_ObtieneMasBailable(self): 
        self.assertEqual(objeto.ObtieneMasBailable([1, 2, 3]),3) 

    def test_ObtieneMasBailable2(self): 
        self.assertEqual(objeto.ObtieneMasBailable([4, 5, 6]),6)    

    def test_VerificaListaCanciones(self): 
        self.assertEqual(objeto.VerificaListaCanciones(["Tengo 30", "Blood", "Poco a Poco"]), 1)  
 
    def test_VerificaListaCanciones2(self): 
        self.assertEqual(objeto.VerificaListaCanciones(["Procura", "Remember Me", "Feeling"]), 1)  

    def test_Encuentra (self):
        self.assertEqual(objeto.Encuentra([1,2,3,44], 44),1)
    
        
if __name__ == "__main__":
    unittest.main()