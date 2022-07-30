(define (over-or-under num1 num2)
    (if (= num1 num2)
        0
        (if (< num1 num2) -1 1)
    )
)

(define (composed f g) (lambda (x) (f (g x))))

(define (square n) (* n n))

(define (pow base exp) 
    (if (= exp 1)
        base
        (if (= base 1)
            1
            (if (even? exp)
                (* (pow base (/ exp 2)) (pow base (/ exp 2)))
                (* base (pow base (- exp 1)))
            )
        )
    )
)

(define (ascending? lst) 
    (if (null? (cdr lst))
        #t
        (if (> (car lst) (car (cdr lst)))
            #f
            (ascending? (cdr lst))
        )
    )
)