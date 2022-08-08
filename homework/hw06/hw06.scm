(define (cddr s) (cdr (cdr s)))

(define (cadr s) (car (cdr s)))

(define (caddr s) (car (cddr s)))

(define (interleave lst1 lst2) 
    (if (null? lst1)
        lst2
        (if (null? lst2)
            lst1
            (cons (car lst1) (cons (car lst2) (interleave (cdr lst1) (cdr lst2))))
        )  
    )
)
; solution
(define (interleave lst1 lst2)
  (if (or (null? lst1) (null? lst2))
      (append lst1 lst2)
      (cons (car lst1)
            (cons (car lst2)
                  (interleave (cdr lst1) (cdr lst2)))))
)



(define (my-filter pred lst) 
    (if (null? lst)
        lst
        (if (pred (car lst))
            (cons (car lst) (my-filter pred (cdr lst)))
            (my-filter pred (cdr lst))
        )
    )
)
; solution
(define (my-filter pred lst)
  (cond ((null? lst) '())
        ((pred (car lst)) (cons (car lst) (my-filter pred (cdr lst))))
        (else (my-filter pred (cdr lst))))
)



(define (concatenate s) 
    (define (tail s sofar)
        (if (null? s)
            sofar
            (tail (cdr s) (append sofar (car s)))
        )
    )
    (tail s '())
)
