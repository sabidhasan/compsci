;; The first three lines of this file were inserted by DrRacket. They record metadata
;; about the language level of this file in a form that our tools can easily process.
#reader(lib "htdp-beginner-reader.ss" "lang")((modname quiz) (read-case-sensitive #t) (teachpacks ()) (htdp-settings #(#t constructor repeating-decimal #f #t none #f () #f)))
(require 2htdp/image)

;; Design a function that consumes two images and produces true if the first is larger than the second.

;; Image Image -> Boolean
;; compares the two images' area, and returns area_img_one > area_img_two
; (define (image_larger_area? img img2) false)

(define SMALL-IMAGE (rectangle 5 5 "outline" "red"))
(define LARGE-IMAGE (rectangle 50 50 "outline" "green"))

(check-expect (image_larger_area? SMALL-IMAGE SMALL-IMAGE) false)
(check-expect (image_larger_area? SMALL-IMAGE LARGE-IMAGE) false)
(check-expect (image_larger_area? LARGE-IMAGE SMALL-IMAGE) true)

; (define (image_larger_area? img1 img2) (...img1 img2))

(define (image_larger_area? img1 img2)
  (>
   (* (image-width img1) (image-height img1))
   (* (image-width img2) (image-height img2))))