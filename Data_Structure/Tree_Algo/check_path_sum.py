class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


"""
This is done using pass by value
"""
def check_sum_pass_by_value(root, target, level_sum, result, path):
    if root == None:
        return

    number = int(level_sum) + root.val
    level_sum = str(number)
    diff = target - number
    path = path + str(root.val)

    if root.left == None and root.right == None and diff == 0:
        result.append(path)
    check_sum_pass_by_value(root.left, target, level_sum, result, path + ",")
    check_sum_pass_by_value(root.right, target, level_sum, result, path + ",")


def check_sum_by_reference(root, target, current_sum_at_each_level, result, path):
    if root == None:
        return
    current_sum_at_each_level = current_sum_at_each_level + root.val
    path.append(root.val)
    if root.left == None and root.right == None and current_sum_at_each_level == target:
        result.append(path.copy())

    check_sum_by_reference(root.left, target, current_sum_at_each_level, result, path)
    check_sum_by_reference(root.right, target, current_sum_at_each_level, result, path)
    path.pop()


if __name__ == "__main__":
    root = TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),
                    TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1))))
    # level_sum = "0"
    # result = []
    # path = ""
    # target = 22
    # check_sum_pass_by_value(root, target, "0", result, path)
    # updated_result = []
    # for path in result:
    #     updated_result.append([path])
    # print(updated_result)

    result = []
    path = []
    target = 22
    check_sum_by_reference(root, target, 0, result, path)
    print(result)
