import unittest
# using set operation we can be able to find all the common values in a list of list

def array_set_approach(k) -> int:
    # initialise a set of common values 
    common_set = set(k[0])
    for inner_list in k[1:]:
        common_set &= set(inner_list)

    
    if common_set:
        return min(common_set)
    else:
        return -1 
    




class TestArrayFunction(unittest.TestCase):
    def setUp(self) -> None:
        print("starting test case")

    def test_array_fun(self):
        my_list = [
                        [1, 2, 3, 4],
                        [2, 4, 7, 8],
                        [4, 10, 11, 12],
                        [9, 14, 15, 16]
                    ]
        expected_result = -1
        try:
            self.assertEqual(array_set_approach(my_list), expected_result, f"Test case failed expected {expected_result}")
            print("try block")
            print(array_set_approach(my_list))
        except AssertionError as e:
            print("assertion error -1 expected")
            print(str(e))

    def test_array_positive(self):
        my_list = [
                        [1, 2, 3, 4, 5, 6, 7],
                        [3, 4, 5, 6, 7, 8, 9],
                        [5, 6, 7, 8, 9, 10, 11],
                        [5, 6, 7, 9, 10, 11, 12]
                    ]
        expected_result = 5

        try:
            self.assertEqual(array_set_approach(my_list), expected_result, f"expected {expected_result}")
            print("try block")
            print(array_set_approach(my_list))
        except AssertionError as e:
            print("Assertion error expected 5")
            print(str(e))

    def tearDown(self) -> None:
        print("finishing test case")




if __name__ == "__main__":
    unittest.main()



