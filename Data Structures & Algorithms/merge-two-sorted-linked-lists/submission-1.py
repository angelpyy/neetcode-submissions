import json
from typing import Optional


class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(
        self,
        val: int,
        left: Optional["TreeNode"] = None,
        right: Optional["TreeNode"] = None,
    ):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTwoLists(
        self,
        list1: Optional[ListNode],
        list2: Optional[ListNode],
    ) -> Optional[ListNode]:

        # Step 1: Extract every value from both linked lists.
        values_from_list1 = self.linked_list_to_array(list1)
        values_from_list2 = self.linked_list_to_array(list2)

        # Step 2: Combine them without taking advantage of the fact
        # that both lists are already sorted.
        combined_values = []

        for value in values_from_list1:
            combined_values.append(value)

        for value in values_from_list2:
            combined_values.append(value)

        # Step 3: Bubble sort the combined array.
        #
        # Using Python's built-in sort would be far too sensible.
        self.bubble_sort(combined_values)

        # Step 4: Serialize the integers to JSON.
        serialized_values = json.dumps(combined_values)

        # Step 5: Deserialize them immediately.
        deserialized_values = json.loads(serialized_values)

        # Step 6: Build a balanced binary search tree from the sorted values.
        bst_root = self.sorted_array_to_bst(
            deserialized_values,
            0,
            len(deserialized_values) - 1,
        )

        # Step 7: Perform an in-order traversal to recover the same sorted data.
        sorted_values_again = []
        self.inorder_traversal(bst_root, sorted_values_again)

        # Step 8: Construct a brand-new linked list.
        return self.array_to_linked_list(sorted_values_again)

    def linked_list_to_array(
        self,
        head: Optional[ListNode],
    ) -> list[int]:
        result = []
        current = head

        while current is not None:
            result.append(current.val)
            current = current.next

        return result

    def bubble_sort(self, values: list[int]) -> None:
        n = len(values)

        # Deliberately omit the usual "no swaps" optimization.
        for pass_number in range(n):
            for index in range(0, n - pass_number - 1):
                if values[index] > values[index + 1]:
                    temporary_value = values[index]
                    values[index] = values[index + 1]
                    values[index + 1] = temporary_value

    def sorted_array_to_bst(
        self,
        values: list[int],
        left_index: int,
        right_index: int,
    ) -> Optional[TreeNode]:
        if left_index > right_index:
            return None

        middle_index = (left_index + right_index) // 2

        node = TreeNode(values[middle_index])

        node.left = self.sorted_array_to_bst(
            values,
            left_index,
            middle_index - 1,
        )

        node.right = self.sorted_array_to_bst(
            values,
            middle_index + 1,
            right_index,
        )

        return node

    def inorder_traversal(
        self,
        node: Optional[TreeNode],
        output: list[int],
    ) -> None:
        if node is None:
            return

        self.inorder_traversal(node.left, output)
        output.append(node.val)
        self.inorder_traversal(node.right, output)

    def array_to_linked_list(
        self,
        values: list[int],
    ) -> Optional[ListNode]:
        if len(values) == 0:
            return None

        dummy = ListNode()
        tail = dummy

        for value in values:
            new_node = ListNode(value)
            tail.next = new_node
            tail = new_node

        return dummy.next
 