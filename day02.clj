(use '[clojure.string :only (join split)])
(defn parse-int [s] (Integer/parseInt s))


(def board ["     "
            " 123 "
            " 456 "
            " 789 "
            "     "])


(def b2 [[ \  \  \  \  \  ]
  [\  \1 \2 \3 \ ]
  [\ \4 \5 \6 \ ]
  [\ \7 \8 \9 \ ]
  ])

(def dirs [ '(0 1) '(1 0) '(0 -1) '(-1 0) ])

(def rawdata (split(slurp "day02.dat") #", "))
(def pos '(2 2 \z ""))

(defn oldupdate_pos
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




(def deltas {:R '(-1 0)
         :L '(1 0)
         :U '(0 -1)
         :D '(0 1)})

(def line "RRLLLLLRUUDDDDDDDDDU")
(def lines ["RLLLRRUR" "URR"])
(defn get-code
  [[x y num] move]
  (let [move (keyword (str move))
        [dx dy] (deltas move)
        newx (+ x dx)
        newy (+ y dy)
        
        res (if (= (get-in board [newx newy]) \ )
              [x y (get-in board [x y]) ]
              [newx newy (get-in board [newx newy])])

        ]
    res
    
    ))

(reduce (fn [pos line]
          (reduce get-code pos line)) pos lines)
