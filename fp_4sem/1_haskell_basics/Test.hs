module Test where
  picks :: [t] -> [([t], t)]
  picks [] = []
  picks (x:xs) = [(xs,x)] ++ [(x:ys,y) | (ys,y) <- picks xs] -- всевозможные расщепления голова:хвост
  perms :: [t] -> [[t]]
  perms [] = [[]]
  perms xs = [(x:zs) | (ys,x) <- picks xs, zs <- perms ys]  


  strict :: (a -> b) -> a -> b
  strict f x = x `seq` f x

  foldlppp :: (a -> b -> a) -> a -> [b] -> a
  foldlppp _ z []     = z                  
  foldlppp f z (x:xs) = foldlppp f (f z x) xs

  foldl' :: (a -> b -> a) -> a -> [b] -> a
  foldl' _ z []  	= z
  foldl' f z (x:xs) = strict (foldl' f) (f z x) xs

