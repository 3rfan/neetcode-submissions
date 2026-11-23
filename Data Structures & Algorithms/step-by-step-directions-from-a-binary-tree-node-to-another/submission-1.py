class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        # helper method to find paths 
        def find_path(node: TreeNode | None, value: int, path: list[str]) -> bool:
            if not node:
                return False

            if node.val == value:
                return True

            # check left subtree
            path.append("L")
            if find_path(node.left, value, path):
                return True
            
            # value not found in left subtree, remove
            path.pop()

            # check right subtree
            path.append("R")
            if find_path(node.right, value, path):
                return True
            
            # value not found in right subtree, remove
            path.pop()

            return False


        # find path from root to start and target value
        start_path: list[str] = []
        target_path: list[str] = []
        find_path(root, startValue, start_path)
        find_path(root, destValue, target_path)

        # advance pointer past shared prefix path (root to lowest common ancestor)
        i = 0
        while (i < len(start_path) and i < len(target_path) and start_path[i] == target_path[i]):
            i += 1

        # return full answer 
        up_moves = "U" * (len(start_path) - i)
        down_moves = "".join(target_path[i:])
        return up_moves + down_moves

