; constructor city
(define berkeley (make-city 'Berkeley 122 37))
;>brkeley
(get-name berkeley)
;>Berkeley
(get-lat berkeley)
;>122
(get-lon city)
;>37


; Q1: Distance
(define (distance city-a city-b)
    (define lat-a (get-lat city-a))
    (define lat-b (get-lat city-b))
    (define lon-a (get-lon city-a))
    (define lon-b (get-lon city-b))
    (sqrt ((+ (expt (- lat-a lat-b) 2) (expt (- lon-a lon-b) 2))))
)

; Q2: Closer City
(define (closer-city lat lon city-a city-b)
    (define city (make-city 'cur lat lon))
    (define d1 (distance city city-a))
    (define d2 (distance city city-b))
    (if (< d1 d2) (get-name city-a) (get-name city-b))
)


; constructor tree
(define t (tree 5 (list (tree 4 nil) (tree 7 nil))))
;>t
(label t)
;>5
(label (car (branches t)))
;>4
(label (car (cdr (branches t))))
;>7

; Q3: Is Leaf
(define (is-leaf? t)
    (null? (cdr branches))
)

; Q4: Sum Nodes
(define (sum-list lst)
    (define (tail lst sofar)
        (if (null? lst)
            sofar
            (tail (cdr lst) (+ sofar (car lst)))
        )
    )
    (tail lst 0)
)

(define (sum-nodes t)
    (define branch-sums (map sum-nodes (branches t)))
    (+ (label t) (sum-list branch-sums))
)

; Q5: Fun Tree
#| Implement fun-tree, 
which takes in a one-argument procedure fun and a tree t. 
It returns a new tree with the same shape as t,
but each label is the result of applying fun to the corresponding label in t. |#
(define (fun-tree fun t)
    (define new-label (fun (label t)))
    (define new-branches (map (lambda (b) (fun-tree fun b)) (branches t)))
    (tree new-label new-branches)
)