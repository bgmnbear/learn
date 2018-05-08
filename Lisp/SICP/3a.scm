(define (list-ref items n)
  (if (= n 0)
      (car items)
      (list-ref (cdr items) (- n 1))))

;: (define squares (list 1 4 9 16 25))

;: (list-ref squares 3)


;; Mapping over lists

(define (scale-list items factor)
  (if (null? items)
      nil
      (cons (* (car items) factor)
            (scale-list (cdr items) factor))))

;: (scale-list (list 1 2 3 4 5) 10)

;: (map + (list 1 2 3) (list 40 50 60) (list 700 800 900))

;: (map (lambda (x y) (+ x (* 2 y)))
;:      (list 1 2 3)
;:      (list 4 5 6))

(define (map proc items)
  (if (null? items)
      nil
      (cons (proc (car items))
            (map proc (cdr items)))))

;: (map abs (list -10 2.5 -11.6 17))

;: (map (lambda (x) (* x x))
;:      (list 1 2 3 4))

(define (scale-list items factor)
  (map (lambda (x) (* x factor))
       items))


;; Painters

(define (segments->painter segment-list)
  (lambda (frame)
    (for-each
     (lambda (segment)
       (draw-line
        ((frame-coord-map frame) (start-segment segment))
        ((frame-coord-map frame) (end-segment segment))))
     segment-list)))


(define (transform-painter painter origin corner1 corner2)
  (lambda (frame)
    (let ((m (frame-coord-map frame)))
      (let ((new-origin (m origin)))
        (painter
         (make-frame new-origin
                     (sub-vect (m corner1) new-origin)
                     (sub-vect (m corner2) new-origin)))))))


(define (flip-vert painter)
  (transform-painter painter
                     (make-vect 0.0 1.0)    ; new origin
                     (make-vect 1.0 1.0)    ; new end of edge1
                     (make-vect 0.0 0.0)))  ; new end of edge2


(define (shrink-to-upper-right painter)
  (transform-painter painter
                     (make-vect 0.5 0.5)
                     (make-vect 1.0 0.5)
                     (make-vect 0.5 1.0)))


(define (rotate90 painter)
  (transform-painter painter
                     (make-vect 1.0 0.0)
                     (make-vect 1.0 1.0)
                     (make-vect 0.0 0.0)))


(define (squash-inwards painter)
  (transform-painter painter
                     (make-vect 0.0 0.0)
                     (make-vect 0.65 0.35)
                     (make-vect 0.35 0.65)))


(define (beside painter1 painter2)
  (let ((split-point (make-vect 0.5 0.0)))
    (let ((paint-left
           (transform-painter painter1
                              (make-vect 0.0 0.0)
                              split-point
                              (make-vect 0.0 1.0)))
          (paint-right
           (transform-painter painter2
                              split-point
                              (make-vect 1.0 0.0)
                              (make-vect 0.5 1.0))))
      (lambda (frame)
        (paint-left frame)
        (paint-right frame)))))