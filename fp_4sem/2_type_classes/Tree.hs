import Data.Foldable (toList)

-- (1 балла) Определите тип данных Двоичное дерево.
data Tree a = Node { value :: a, left :: Tree a, right :: Tree a } | Null deriving (Show, Read, Eq)

-- (2 балла) Сделайте Двоичное дерево представителем 
-- класса Foldable, реализовав обход дерева в глубину.
-- instance Foldable Tree where
--   foldr z _ Null = mempty
--   foldr z f (Node x l r) = preorder f (Node x l r)

instance Foldable Tree where
  foldMap _ Null = mempty
  foldMap f (Node x l r) = f x `mappend` preorder f l `mappend` preorder f r

tree = Node 4 (Node 2 (Node 0 Null Null) (Node 6 Null Null)) (Node 7 (Node 8 Null Null) Null)

dfs :: Monoid m => (a -> m) -> Tree a -> m
dfs _ Null = mempty
dfs f (Node x l r) = f x `mappend` dfs f l `mappend` dfs f r

-- (3 балла) Сделайте Двоичное дерево представителем 
-- класса Foldable, реализовав обход дерева в ширину.
bfs :: Monoid m => (a -> m) -> Tree a -> m
bfs _ Null = mempty
bfs f t = bfs' mempty [t]
  where bfs' acc [] = acc
        bfs' acc (t:ts) = let acc' = acc `mappend` (f $ value t) 
                          in bfs' acc' $ ts ++ subtrees t
        subtrees t = [ sub | sub@(Node _ _ _) <- [left t, right t] ]

-- (2 балла) Расширение задачи 5. Реализуете три варианта обхода дерева: 
-- preorder, in-order, postorder, https://en.m.wikipedia.org/wiki/Tree_traversal.
preorder :: Monoid m => (a -> m) -> Tree a -> m
preorder _ Null = mempty
preorder f (Node x l r) = f x `mappend` preorder f l `mappend` preorder f r

inorder :: Monoid m => (a -> m) -> Tree a -> m
inorder _ Null = mempty
inorder f (Node x l r) = inorder f l `mappend` f x `mappend` inorder f r

postorder :: Monoid m => (a -> m) -> Tree a -> m
postorder _ Null = mempty
postorder f (Node x l r) = postorder f l `mappend` postorder f r `mappend` f x






perms :: [a] -> [[a]]
perms [] = []
perms [x] = [[x]]
perms xs = do let len = length xs
              let flip (x:xs) = xs ++ [x]
              rotation <- take len $ iterate flip xs      
              (y:ys)   <- return rotation                      
              result   <- do tailPerm <- perms ys               
                             return $ y : tailPerm
              return result
