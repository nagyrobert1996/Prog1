(defun faktorialis (n)
        (if (= n 1)
                1
        (* n (faktorialis (- n 1) ))
        ))
(princ "szam: ")
(setq a (read))
(princ (faktorialis a))