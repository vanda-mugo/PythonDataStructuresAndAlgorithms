from TreeNode import TreeNode, sample_root_node, print_path, print_tree

print_tree(sample_root_node)

def dfs(root, target, path=()):
  path = path + (root,)

  if root.value == target:
    return path

  for child in root.children:
    node_found = dfs(child, target, path)

    if node_found is not None:
      return node_found

  return None
        
        
node = dfs(sample_root_node, "F")
print(node)