; Owner and Vehicle Abstraction
(define (make-owner name age)
  (cons name (cons age nil)))

(define (get-name owner) (car owner))

(define (get-age owner) (car (cdr owner)))

(define (make-vehicle model year previous-owners)
  (cons model (cons year previous-owners)))

(define (get-model vehicle) (car vehicle))

(define (get-year vehicle) (car (cdr vehicle)))

(define (get-owners vehicle) (cdr (cdr vehicle)))

(define (older-vehicle vehicle1 vehicle2)
  (if (< (get-year vehicle1) (get-year vehicle2))
    (get-model vehicle1)
    (get-model vehicle2)
  )
)

(define (new-owner vehicle owner)
  (make-vehicle (get-model vehicle) (get-year vehicle) (cons owner (get-owners vehicle)))
)

(define (owners-names vehicle) (map (lambda (owner) (get-name owner)) (get-owners vehicle)))


; solution
(define (split-at lst n)
  (cond ((= n 0) (cons nil lst))
        ((null? lst) (cons lst nil))
        (else (let ((rec (split-at (cdr lst) (- n 1))))
                (cons (cons (car lst) (car rec)) (cdr rec)))))
)
; MY dumb
(define (split-at lst n)
  (define (first lst n)
    (if (zero? n)
      nil
      (if (null? lst)
        nil
        (cons (car lst) (first (cdr lst) (- n 1))))))
  (define (rest lst n)
    (if (zero? n)
      lst
      (if (null? lst)
        nil
        (rest (cdr lst) (- n 1)))))
  (cons (first lst n) (rest lst n))
)


; Tree Abstraction
; Constructs tree given label and list of branches
(define (tree label branches)
  (cons label branches))

; Returns the label of the tree
(define (label t) (car t))

; Returns the list of branches of the given tree
(define (branches t) (cdr t))

; Returns #t if t is a leaf, #f otherwise
(define (is-leaf t) (null? (branches t)))

(define (filter-odd t) 
  (if (null? t)
    nil
    (if (even? (label t))
      (tree nil (map filter-odd (branches t)))
      (tree (label t) (map filter-odd (branches t)))
    )
  )
)
