(use '[clojure.string :only (join split trim-newline)])
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





(def deltas {:R '(0 1)
             :L '(0 -1)
             :U '(-1 -0)
             :D '(1 0)})


(defn get-code
  [[x y num code] move]
  (let [move (keyword (str move))
        [dx dy] (deltas move)
        newx (+ x dx)
        newy (+ y dy)
        
        res (if (= (get-in board [newx newy]) \ )
              [x y (get-in board [x y]) code ]
              [newx newy (get-in board [newx newy]) code])

        ]
    res
    
    ))


(def rawdata (map trim-newline (split(slurp "day02.dat") #"\n")))
(def pos '(2 2 \5 ""))


(-> (reduce (fn [[x y num code] line]
          (let [ [nx ny nnum ncode] (reduce get-code [x y num code] line)
                ]
            [nx ny num (str nnum code)]
            )
              )pos rawdata)
    (nth 3)
    clojure.string/reverse
    )

