import unittest


class TestLists(unittest.TestCase):
    person = []

    def setUp(self):
        self.person = ["Gagandeep", 30, True, 78.4, 1 + 4j]

    def test_length_of_the_list(self):
        self.assertEqual(5, len(self.person), "The length of the list is incorrect")

    def test_fetching_the_range_of_the_list(self):
        self.assertEqual(range(0, 5), range(len(self.person)), "Incorrect range of the list")

    def test_fetch_item_from_list(self):
        self.assertTrue(self.person[2], "This person should be enabled")
        self.assertEqual([78.4], self.person[3:4], "The weight is incorrect")

    def test_slicing_the_lists(self):
        self.assertEqual([30, True], self.person[1:3], "Incorrect slicing for [1:3]")
        self.assertEqual(["Gagandeep", 30, True], self.person[0:3], "Incorrect slicing for [0:3]")
        self.assertEqual(["Gagandeep", 30, True], self.person[:3], "Incorrect slicing for [:3]")
        self.assertEqual([1 + 4j], self.person[4:5], "Incorrect slicing for [4:5]")
        self.assertEqual([78.4, 1 + 4j], self.person[3:], "Incorrect slicing for [3:]")
        self.assertEqual([], self.person[100:], "Incorrect slicing for [6:]")

    def test_updating_single_element_in_the_list(self):
        temp_person = self.person
        temp_person[0] = "Gagandeep Singh"
        self.assertEqual(["Gagandeep Singh", 30, True, 78.4, 1 + 4j], temp_person, "Incorrect list is supplied")
        temp_person[1:3] = [37, False]
        self.assertEqual(["Gagandeep Singh", 37, False, 78.4, 1 + 4j], temp_person, "Incorrect list is supplied")

    def test_deleting_items_from_list(self):
        del self.person[3:5]
        self.assertEqual(["Gagandeep", 30, True], self.person, "Delete unsuccessful")
        del self.person[:2]
        self.assertEqual([True], self.person, "Delete unsuccessful for slicing")
        self.assertEqual(1, len(self.person), "Incorrect length")

        with self.assertRaises(IndexError) as context:
            person_x = self.person[3]
            print(person_x)
        self.assertEqual("list index out of range", str(context.exception), "Incorrect message")

    def test_concatenating_two_lists(self):
        first_5_odd = [1, 3, 5, 7, 9]
        first_5_even = [2, 4, 6, 8, 10]
        self.assertEqual([1, 3, 5, 7, 9, 2, 4, 6, 8, 10], first_5_odd + first_5_even, "Concatenation failure")

    def test_find_element_in_list(self):
        found_element_age = 30 in self.person
        self.assertTrue(found_element_age, "Age is not found in the person list")

    def test_element_is_not_present_in_the_list(self):
        element_is_not_in_list = 'X-Men' not in self.person
        self.assertTrue(element_is_not_in_list, "X-Men is in wrong list")

    def test_modifying_list_using_slice_but_with_less_elements(self):
        # Here I'm slicing two elements but providing only single element
        # This element will replace both of them and will adjust the indices.
        self.person[1:3] = [35]
        self.assertEqual(["Gagandeep", 35, 78.4, 1 + 4j], self.person, "Updating of less elements failed")

    # ----------------------------------
    #  Test adding elements in the list
    # ----------------------------------
    #
    # Adding elements to the list involves
    # - Appending new elements to the end of the list
    # - Inserting them at a specific index
    # - Extending the list with elements from other iterable object
    #
    # We can make use of the following methods to achieve that
    # - append(): Insert a single item at the end of the list
    # - extend(): Insert multiple items at the end of the list from another iterable (like another list)
    # - insert(): Insert a single item at a specific index

    # Adding list items using append
    def test_adding_list_items_using_append_function(self):
        names = ['Gagan', 'Dara']
        print()
        names.append('Aagya')
        self.assertEqual(['Gagan', 'Dara', 'Aagya'], names, "Appending of kids failed")

    # Adding element at a specific position / index
    def test_adding_an_element_at_specific_position_using_insert(self):
        names = ['Gagan', 'Dara']
        names.insert(1, 'Aagya')
        self.assertEqual(['Gagan', 'Aagya', 'Dara'], names, "Inserting of kids failed")

    # Appending multiple elements using an extend function
    def test_appending_multiple_items_using_extend(self):
        names = ['Gagan', 'Dara']
        names.extend(['Aagya', 'Akaal'])
        self.assertEqual(['Gagan', 'Dara', 'Aagya', 'Akaal'], names, "Extending names failure")

    # --------------------------------------
    #  Test removing elements from the list
    # --------------------------------------
    #
    # Removing elements from the list means, deleting element(s) from the list. Lists are ordered collection of items.
    # You can remove the elements from a certain index or from the end.
    # You can perform these operations using the following methods:
    # - remove(): Removed the first occurrence of an item from the list.
    #               Raises ValueError if the value is not present.
    # - pop(): Removes last element if no index is provided, otherwise remove the element at index and alter list.
    #           Pop will also return the value of the item it has removed.
    #           Raises IndexError if list is empty or index is out of range.
    # - clear(): Remove all the elements from the list and returns `None` but list becomes `[]` or empty.
    #
    # You can also make use of the `del` statement to remove elements from certain indices.

    # Removing element from the list using the remove function
    def test_remove_item_from_list(self):
        names = ['Gagan', 'Dara', 'Gagan', 'Dara']
        names.remove('Gagan')
        self.assertEqual(['Dara', 'Gagan', 'Dara'], names, 'Removing of my name is unsuccessful')

    # What if the element is not found
    def test_remove_item_that_does_not_exist(self):
        names = ['Gagan', 'Dara', 'Gagan', 'Dara']
        with self.assertRaises(ValueError) as context:
            names.remove('Aagya')
        self.assertEqual('list.remove(x): x not in list', str(context.exception), 'Exception was not thrown')

    # Remove items using the pop method
    def test_remove_the_last_item(self):
        self.assertEqual(1 + 4j, self.person.pop(), 'Pop was not successful')

    # Remove item at an index using the `pop` function
    def test_remove_item_at_index_using_pop(self):
        self.assertTrue(self.person.pop(2), "Index pop was unsuccessful")

    # Remove all the elements from the list and returns a None
    def tests_remove_all_elements_from_list(self):
        self.assertIsNone(self.person.clear(), "Clear was unsuccessful")
        self.assertEqual([], self.person, "Return type is different")


if __name__ == '__main__':
    unittest.main()
