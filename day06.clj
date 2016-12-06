(use '[clojure.string :only (join split)])
(defn parse-int [s] (Integer/parseInt s))


(def rawdata (split(slurp "day06.dat") #"\n"))


(def l
  (->>(eval (cons #'map (cons #'vector rawdata)))
    (map frequencies)
    (map (fn [x](sort-by second x)))
;    (map reverse) ;; this line is needed for part 1
    (map first)
    (map first)
    (apply str)
    ))

(print l)
