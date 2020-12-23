(define (reverse lst)
    (cond
      ((null? lst) '())
      (else (append (reverse (cdr lst))  (cons (car lst) '())))
    )
)


(define (longest-increasing-subsequence lst)
    (define (lis lst_2 prev_best)
        (cond
          ; base case
          ((null? lst_2) '())
          ; skip this elem and keep the prev_best, as this elem doesn't contribute to LCS
          ((<= (car lst_2) prev_best) (lis (cdr lst_2) prev_best))
          (else
            ; same as above - ignore current element, and keep prev_best
            (define ignore_first (lis (cdr lst_2) prev_best))
            ; take first elem into account, and use it as the new prev_best
            (define take_first (cons (car lst_2) (lis (cdr lst_2) (car lst_2))))
            (if (> (length take_first) (length ignore_first)) take_first ignore_first)
          )
        )
    )
    (lis lst 0)
)

(define (cadr s) (car (cdr s)))
(define (caddr s) (cadr (cdr s)))


; derive returns the derivative of EXPR with respect to VAR
(define (derive expr var)
  (cond ((number? expr) 0)
        ((variable? expr) (if (same-variable? expr var) 1 0))
        ((sum? expr) (derive-sum expr var))
        ((product? expr) (derive-product expr var))
        ((exp? expr) (derive-exp expr var))
        (else 'Error)))

; Variables are represented as symbols
(define (variable? x) (symbol? x))
(define (same-variable? v1 v2)
  (and (variable? v1) (variable? v2) (eq? v1 v2)))

; Numbers are compared with =
(define (=number? expr num)
  (and (number? expr) (= expr num)))

; Sums are represented as lists that start with +.
(define (make-sum a1 a2)
  (cond ((=number? a1 0) a2)
        ((=number? a2 0) a1)
        ((and (number? a1) (number? a2)) (+ a1 a2))
        (else (list '+ a1 a2))))
(define (sum? x)
  (and (list? x) (eq? (car x) '+)))
(define (addend s) (cadr s))
(define (augend s) (caddr s))

; Products are represented as lists that start with *.
(define (make-product m1 m2)
  (cond ((or (=number? m1 0) (=number? m2 0)) 0)
        ((=number? m1 1) m2)
        ((=number? m2 1) m1)
        ((and (number? m1) (number? m2)) (* m1 m2))
        (else (list '* m1 m2))))
(define (product? x)
  (and (list? x) (eq? (car x) '*)))
(define (multiplier p) (cadr p))
(define (multiplicand p) (caddr p))

(define (derive-sum expr var)
  (make-sum (derive (addend expr) var) (derive (augend expr) var))
)

(define (derive-product expr var)
  (make-sum
    (make-product (derive (multiplier expr) var) (multiplicand expr))
    (make-product (multiplier expr) (derive (multiplicand expr) var))
  )
)

; Exponentiations are represented as lists that start with ^.
(define (make-exp base exponent)
  ; The base can be any expression, but assume that the exponent is a non-negative integer.
  (cond
    ((=number? exponent 1) base)
    ((=number? exponent 0) 1)
    ((number? base) (expt base exponent))
    (else (list '^ base exponent))
  )
)

(define (base exp) (cadr exp))

(define (exponent exp) (caddr exp))

(define (exp? exp) (and (list? exp) (eq? (car exp) '^)))

(define x^2 (make-exp 'x 2))
(define x^3 (make-exp 'x 3))

(define (derive-exp exp var)
  (make-product (exponent exp) (make-exp (base exp) (- (exponent exp) 1)))
)