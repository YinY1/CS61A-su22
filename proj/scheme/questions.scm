(define (caar x) (car (car x)))
(define (cadr x) (car (cdr x)))
(define (cdar x) (cdr (car x)))
(define (cddr x) (cdr (cdr x)))

;; Problem 15
;; Returns a list of two-element lists
(define (enumerate s)
  ; BEGIN PROBLEM 15
  (define (tail s index)
       (if (null? s)
           nil
           (cons (list index (car s)) (tail (cdr s) (+ index 1))))
  )
  (tail s 0)
  )
  ; END PROBLEM 15

;; Problem 16

;; Merge two lists LIST1 and LIST2 according to ORDERED? and return
;; the merged lists.
(define (merge ordered? list1 list2)
  ; BEGIN PROBLEM 16
  (define (tail list1 list2 sofar)
    (if (null? list1)
      (append sofar list2)
      (if (null? list2)
        (append sofar list1)
        (if (ordered? (car list1) (car list2))
          (tail (cdr list1) list2 (append sofar (list (car list1))))
          (tail list1 (cdr list2) (append sofar (list (car list2))))
        )
      )
    )
  )      
  (tail list1 list2 '())
)
  ; END PROBLEM 16

