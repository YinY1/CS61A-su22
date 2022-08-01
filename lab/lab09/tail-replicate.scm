(define (tail-replicate x n)
  ; BEGIN
  (define (tail x n sofar)
    (if (zero? n)
      sofar
      (tail x (- n 1) (cons x sofar)) ; it's wrong to write "cons sofar x"
    )
  )
  (tail x n nil)
  ; END
)