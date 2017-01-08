(use '[clojure.string :only (join split)])
(defn parse-int [s] (Integer/parseInt s))

(def dirs [ '(0 1) '(1 0) '(0 -1) '(-1 0) ])

(def rawdata (split(slurp "day01.dat") #", "))
(def pos '(0 0 0))

(defn update_pos
  [ [x y dir] move]
  (let [
       turn (first move)
        samount (subs move 1)
        amount (parse-int samount)
        tmpnewdir (if (= turn \L)
                 (dec dir)
                 (inc dir))
        newdir (mod tmpnewdir 4)
        newx (+ x (* amount (first (nth dirs newdir))))
        newy (+ y (* amount (second (nth dirs newdir))))
        ]
    
  [newx newy newdir]
  ))

(reduce update_pos pos rawdata)

(update_pos pos "L1")

(defn convert [l]  (map parse-int (rest(split l  #"[ \t]+"))))


(def dlist(map convert rawdata))

(defn is-tri? [ [a b c] ]
  (and (> (+ a b) c)
      (> (+ b c) a)
      (> (+ c a) b)
      ))

; answer for part 1
(count(filter is-tri? dlist))

