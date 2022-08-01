; Q3: Sum (with tail context)
(define (sum lst)
  (define (tail_sum lst res)
    (if (null? lst)
      res
      (tail_sum (cdr lst) (+ (car lst) res))
    )
  )
  (tail_sum lst 0)
)
; ALTERNATE SOLUTION
(define (sum lst)
    (cond
      ((null? lst) 0)
      ((null? (cdr lst)) (car lst))
      (else (sum (cons (+ (car lst) (car (cdr lst))) (cdr (cdr lst)))))
    )
)

; Q4: Reverse
(define (reverse lst)
  (define (helper current rest)
    (if (null? rest)
      current
      (helper (cons (car rest) current) (cdr rest))
    )
  )
  (helper nil lst)
)