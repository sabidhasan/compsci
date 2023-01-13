;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname shapes) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

; playing with shapes
(circle 20 "solid" "pink")

(beside
        (circle 15 "solid" "green")
        (rectangle 25 40 "solid" "red")
        (square 20 "solid" "blue"))

; stop sign
(overlay
         (text "STOP" 46 "white")
         (regular-polygon 60 8 "solid" "red"))

; constants
(define TEST 2)
(* 2 TEST)

; functions
(define (draw-circle color)
  (circle 30 "solid" color))
(draw-circle "purple")

; booleans
(define T true)
(define F false)

(> 5 1) ; should be true
(< (image-width (rectangle 10 10 "solid" "red")) (image-width (rectangle 20 20 "outline" "pink"))) ; should be true

(= 66 66)
(string=? "boo" "boo2")

(if false "blah" "blah2")

; these are short circuited in this language
(and true true)
(or true false)
(not true)