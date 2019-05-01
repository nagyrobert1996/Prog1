(princ "szam: ")
(setq a (read))
(setq b 1)
(loop for i from 1 to a
	do( setq b (* b i)))
(princ b)