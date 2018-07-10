(define (eval exp env)
  (cond ((lambda? exp)
         (make-procedure (lambda-parameters exp)
                         (lambda-body exp)
                         env))
        ((application? exp)
         (apply (eval (operator exp) env)
                (list-of-values (operands exp) env)))))


(define (apply procedure arguments)
    (eval-sequence
        (procedure-body procedure)
        (extend-environment
            (procedure-parameters procedure)
            arguments
            (procedure-environment procedure))))


;;EXERCISE 5.4
(define (expt b n)
  (if (= n 0)
      1
      (* b (expt b (- n 1)))))

(define (expt b n)
  (define (expt-iter counter product)
    (if (= counter 0)
        product
        (expt-iter (- counter 1) (* b product))))
  (expt-iter n 1))