; Q8: List Insert
(define (insert element lst index)
   (if (zero? index)
      (cons element lst)
      (cons (car lst) (insert element (cdr lst) (- index 1)))
   )
)

; Q9: Group by Non-Decreasing
(define (nondecreaselist s)
    (if (null? s)
        nil
        (let ((rest (nondecreaselist (cdr s)) ))
            (if (or (null? (cdr s)) (> (car s) (car (cdr s))))
                (cons (list (car s)) rest)
                (cons (cons (car s) (car rest)) (cdr rest))
            )
        )
    )
)