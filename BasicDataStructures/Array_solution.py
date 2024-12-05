
import unittest


def array_solution(k):
    # k being an array of arrays 
    # initialise a variable for the leading values and one for the last values 
    leading_values = []
    last_values = []

    for inner_list in k:
        leading_values.append(inner_list[0])
        last_values.append(inner_list[-1])

    # now having added the leading values and trailing last values 
    leading_values.sort()
    last_values.sort()
    print(last_values)
    print(leading_values)
    common_values = set()


    # a value to be common has to be amongst the last value( greatest value in ) leading values
    # the value also has to be amongst the smallest (the first value of the last values )

    for inner_list in k:
        prevailing_set = { value for value in inner_list if value <= last_values[0] and value >= leading_values[-1]}
        print(f"prevailing set {prevailing_set}")
        prevailing_list = list(prevailing_set)
        print(f"prevailing list {prevailing_list}")
        for item in prevailing_list:
            for smaller_list in k:

                if item in smaller_list:
                    common_values.add(item)

    
    # now to sort
    common_list_values = list(common_values)
    print(f"common values {common_list_values}")
    if common_list_values:
        if common_list_values[0]:
            return common_list_values[0]
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
            self.assertEqual(array_solution(my_list), expected_result, f"Test case failed expected {expected_result}")
            print("try block")
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
            self.assertEqual(array_solution(my_list), expected_result, f"expected {expected_result}")
            print("try block")
        except AssertionError as e:
            print("Assertion error expected 5")
            print(str(e))

    def tearDown(self) -> None:
        print("finishing test case")




if __name__ == "__main__":
    unittest.main()


