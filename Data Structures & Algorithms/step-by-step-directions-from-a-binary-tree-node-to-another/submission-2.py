class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
            def find_path(node: Optional[TreeNode], target: int) -> list[str]:
                if not node:
                    return []

                # Stack stores (current_node, visit_state):
                # 0 = try left child, 1 = try right child, 2 = dead end (backtrack)
                stack: list[tuple[TreeNode, int]] = [(node, 0)]
                path: list[str] = []

                while stack:
                    curr, state = stack[-1]
                    if curr.val == target:
                        return path

                    if state == 0:
                        stack[-1] = (curr, 1)
                        if curr.left:
                            path.append("L")
                            stack.append((curr.left, 0))
                    elif state == 1:
                        stack[-1] = (curr, 2)
                        if curr.right:
                            path.append("R")
                            stack.append((curr.right, 0))
                    else:
                        stack.pop()
                        if path:
                            path.pop()

                return []

            start_path = find_path(root, startValue)
            target_path = find_path(root, destValue)

            i = 0
            while i < len(start_path) and i < len(target_path) and start_path[i] == target_path[i]:
                i += 1

            up_moves = "U" * (len(start_path) - i)
            down_moves = "".join(target_path[i:])
            return up_moves + down_moves