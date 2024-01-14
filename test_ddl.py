import pytest
from ddl import DoubleLinkedList


@pytest.mark.parametrize("test_input,expected", [(DoubleLinkedList(), None)])
def test_if_initialization_of_an_empty_ddl_results_in_the_none_head(
    test_input, expected
):
    assert test_input.head is expected


def test_if_insertion_of_element_results_in_positioning_at_the_beginning_of_the_ddl():
    double_linked_list: DoubleLinkedList = DoubleLinkedList()
    element_to_add = 5
    double_linked_list.list_insert(value=element_to_add)
    assert double_linked_list.head.key == element_to_add


@pytest.mark.parametrize("test_input,expected", [(4, 4)])
def test_if_insertion_of_element_into_nonempty_ddl_results_in_appropriate_update_of_nodes_attributes(
    test_input, expected
):
    double_linked_list: DoubleLinkedList = DoubleLinkedList()
    element_to_add = 5
    double_linked_list.list_insert(value=element_to_add)
    double_linked_list.list_insert(value=test_input)
    assert (
        double_linked_list.head.key == expected
        and double_linked_list.head.prev is None
        and double_linked_list.head.child.key == element_to_add
        and double_linked_list.head.child.prev == double_linked_list.head
    )
