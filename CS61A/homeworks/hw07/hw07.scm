(define (cddr s)
  (cdr (cdr s))
)

(define (cadr s)
  (car (cdr s))
)

(define (caddr s)
  (car (cdr (cdr s)))
)

(define (sign x)
  (cond
    ((> x 0) 1)
    ((< x 0 ) -1)
    (else 0)
  )
)

(define (square x) (* x x))

(define (pow b n)
  (cond
    ; base case - if n = 0 return 1
    ((= n 0) 1)
    ; if n is even, return (pow b n/2) squared
    ((even? n) (square (pow b (/ n 2))))
    (else (* b (pow b (- n 1))))
  )
)

(define (ordered? s)
  ; check if next position is empty
  (cond
    ((null? s) true)
    ((null? (cdr s)) true)
    (< (car s) (cadr s) (ordered? (cdr s)))
    (else false)
  )
)

(define (empty? s) (null? s))

(define (add s v)
  (cond
    ; base case - empty list - return list of one item
    ((null? s) (list v))
    ; if curr value equal to v return set, as this is dupe
    ((= (car s) v) (cons (car s) (cdr s)))
    ; if curr value greater than target, prepend
    ((> (car s) v) (cons v s))
    ; if curr value less than target, continue traversing
    ((< (car s) v) (cons (car s) (add (cdr s) v)))
  )
)

; Sets as sorted lists
(define (contains? s v)
  (cond
    ((empty? s) false)
    ((> (car s) v) false)
    ((< (car s) v) (contains? (cdr s) v))
    ((= (car s) v) true)
  )
)

; Equivalent Python code, for your reference:
;
; def empty(s):
;     return s is Link.empty
;
; def contains(s, v):
;     if empty(s):
;         return False
;     elif s.first > v:
;         return False
;     elif s.first == v:
;         return True
;     else:
;         return contains(s.rest, v)

(define (intersect s t)
  (cond
    ; base cases
    ((null? s) '())
    ((null? t) '())
    ; look at first values, if equal add the value, and advance
    ((= (car s) (car t)) (cons (car t) (intersect (cdr s) (cdr t))))
    ; if not equal, advance one of the lists and recurse
    ((> (car s) (car t)) (intersect s (cdr t)))
    ((< (car s) (car t)) (intersect (cdr s) t))
  )
)

; Equivalent Python code, for your reference:
;
; def intersect(set1, set2):
;     if empty(set1) or empty(set2):
;         return Link.empty
;     else:
;         e1, e2 = set1.first, set2.first
;         if e1 == e2:
;             return Link(e1, intersect(set1.rest, set2.rest))
;         elif e1 < e2:
;             return intersect(set1.rest, set2)
;         elif e2 < e1:
;             return intersect(set1, set2.rest)

(define (union s t)
  (cond
    ; base cases
    ((null? s) t)
    ((null? t) s)
    ((= (car s) (car t)) (cons (car s) (union (cdr s) (cdr t))))
    ((< (car s) (car t)) (cons (car s) (union (cdr s) t)))
    ((> (car s) (car t)) (cons (car t) (union s (cdr t))))
  )
)