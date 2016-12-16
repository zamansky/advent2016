
(use '[clojure.string :only (join split)])
(defn parse-int [s] (Integer/parseInt s))

(def input "11011110011011101")
;(def targetlen 272)
(def targetlen 35651584) ; for part 2

(defn flip [x]
  (apply str (map #(if (= % \1) \0 \1)x)))

(defn f [x]
  (apply str x "0" (flip (reverse x))))

(defn toint [x] (- (int x) (int \0)))

(defn xnor [[x y]]
  (if (= x y) 1 0))

(defn checksum [x]
  (map xnor (partition 2 x)))

(defn checkchecksums [vals]
  (loop  [c (checksum vals)]
    (if (odd? (count c))
      (apply str c)
      (recur (checksum c))
  )))

(defn doit [input targetlen]
  (let [ dragon (take 1 (drop-while #(< (count %) targetlen) (iterate f input)))
        intvals (map toint (take targetlen (first dragon)))
        ans (checkchecksums intvals)
        ;;ans (apply str (first (take 1 (drop-while #(even? (count %)) (iterate checksum intvals)))))
        ]
    ans
    )
  )


(println (doit input targetlen))

(defn -main []
  (println ("HELLO WORLD")))
