; Q1 Virahanka-Fibonacci
(define (vir-fib n)
    (if (<= n 1) 
        n 
        (+ (vir-fib (- n 1)) (vir-fib (- n 2))))
)

; Q2 List Making
(define with-list
    (list
        (list 'a 'b) 'c 'd (list 'e)
    )
)

(define with-quote
    '(
        (a b) c d (e)
    )

)

(define helpful-list
   (cons 'a (cons 'b nil)))

(define another-helpful-list
    (cons 'c (cons 'd (cons (cons 'e nil) nil))))

(define with-cons
    (cons
        helpful-list another-helpful-list
        ;or
        ;(cons 'a (cons 'b nil)) (cons 'c (cons 'd (cons (cons 'e nil) nil)))
    )
)


; Q3 List Concatenation
(define (list-concat a b)
    (if (null? a)
        b
        (cons (car a) (list-concat (cdr a) b)))
)

; Q4 Map
(define (map-fn fn lst)
    (if (null? lst)
        nil
        (cons (fn (car lst)) (map-fn fn (cdr lst))))
)

; Q5 Remove
(define (remove item lst)
  (if (null? lst)
    nil
    (if (= item (car lst))
      (remove item (cdr lst))
      (cons (car lst) (remove item (cdr lst)))))
)
; alternative solution
(define (remove item lst)
  (cond ((null? lst) '())
        ((equal? item (car lst)) (remove item (cdr lst)))
        (else (cons (car lst) (remove item (cdr lst)))))
)
; alternative solution with filter
(define (remove item lst)
  (filter (lambda (x) (not (= x item))) lst))