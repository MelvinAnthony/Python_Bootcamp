import unittest
import cap


class test_cap(unittest.TestCase):
    
    def test_one_word(self):
        text = "python"
        res = cap.capitalize(text)
        self.assertEqual(res,"Python")
        return res
    
    def multi_word(self):
        text = "mel python"
        res = cap.all_character_first_cap(text)
        self.assertEqual(res,"Me Python")
        return res
    
if __name__ == '__main__':
    unittest.main()