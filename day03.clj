(use '[clojure.string :only (join split)])
(defn parse-int [s] (Integer/parseInt s))


(def rawdata (split(slurp "day03.dat") #"\n"))



(defn convert [l]  (map parse-int (rest(split l  #"[ \t]+"))))


(def dlist(map convert rawdata))


(defn is-tri? [ [a b c] ]
  (and (> (+ a b) c)
      (> (+ b c) a)
      (> (+ c a) b)
      ))

; answer for part 1
(count(filter is-tri? dlist))


; for part 2
(defn transpose [ [l1 l2  l3]]
  (let [[a b c] l1
        [d e f] l2
        [g h i] l3]
    (list (list a d g) (list b e h) (list c f i))
    )
  
  )
;; transform list by taking every three lines, transposing them, then flattening them back
;; into a plain list 
(def tlist1 (partition 3(flatten (map transpose (partition 3 dlist)))))
(count(filter is-tri? tlist1))


