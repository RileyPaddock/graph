from railroad_travel_time import order_towns_by_travel_time_using_tree_class
from railroad_travel_time import order_towns_by_travel_time_from_scratch

railroad_segments = [('B','C'), ('B','A'), ('A','D'), ('E','D'), ('C','F'), ('G','C')]

print("\nTesting order_towns_by_travel_time_from_scratch with D as home:")
assert order_towns_by_travel_time_from_scratch('D',railroad_segments) == ['D', 'A', 'E', 'B', 'C', 'F', 'G'],"Incorrect Result for order_towns_by_travel_time_from_scratch with D as home"
print("\n   Passed")

print("\nTesting order_towns_by_travel_time_from_scratch with A as home:")
assert order_towns_by_travel_time_from_scratch('A',railroad_segments) == ['A', 'B', 'D', 'C', 'E', 'F', 'G'],"Incorrect Result for order_towns_by_travel_time_from_scratch with A as home"
print("\n   Passed")

print("\nTesting order_towns_by_travel_time_using_tree_class with D as home:")
assert order_towns_by_travel_time_using_tree_class('D',railroad_segments) == ['D', 'A', 'E', 'B', 'C', 'F', 'G'],"Incorrect Result for order_towns_by_travel_time_using_tree_class with D as home"
print("\n   Passed")

print("\nTesting order_towns_by_travel_time_using_tree_class with A as home:")
assert order_towns_by_travel_time_using_tree_class('A',railroad_segments) == ['A', 'B', 'D', 'C', 'E', 'F', 'G'],"Incorrect Result for order_towns_by_travel_time_using_tree_class with A as home"
print("\n   Passed")