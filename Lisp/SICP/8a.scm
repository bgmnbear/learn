;;; data base [assertions]
;;; **see microshaft-data-base in the file ch4-query.scm

;;; Simple queries

(job ?x (computer programmer))

(address ?x ?y)

(supervisor ?x ?x)

(job ?x (computer ?type))

(job ?x (computer . ?type))

;;; Compound queries

(and (job ?person (computer programmer))
     (address ?person ?where))

(or (supervisor ?x (Bitdiddle Ben))
    (supervisor ?x (Hacker Alyssa P)))

(and (supervisor ?x (Bitdiddle Ben))
     (not (job ?x (computer programmer))))

(and (salary ?person ?amount)
     (lisp-value > ?amount 30000))

;;; data base [rules]
;;; **see microshaft-data-base in the file ch4-query.scm

;;; queries
(lives-near ?x (Bitdiddle Ben))

(and (job ?x (computer programmer))
     (lives-near ?x (Bitdiddle Ben)))
