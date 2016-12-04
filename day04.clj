(use '[clojure.string :only (join split)])
(defn parse-int [s] (Integer/parseInt s))


(def rawdata (split(slurp "day04.dat") #"\n"))


(defn comparefunc [a b]
  "Use this to get the 2 level sorting (count and alphabetical)"
  (if (= (second a) (second b))
    (compare (first a) (first b))
    (compare (second a) (second b))))




(defn makerotter [n]
  "Return a function to rotate a string by n chars while converting - to space"
  (fn [c] (let [j (mod (+ n(- (int c) 97)) 26)
                ans (char (+ 97 j))]
            (if (= c \- )
              \space
            ans))))
(defn rotword [w n]
  (apply str(map (makerotter n) w)))


(defn calc_sum [chars]
  "Return the checksum of the room given a string of only the letters"
  (->> chars
       frequencies
       (sort-by first) 
       reverse
       (sort-by second)
       reverse
       (take 5)
       (map first)
       (apply str)
       ))

(defn dosplit [l]
  (let [splitter1 #"([a-z\-]+)([0-9]+)\[([a-z]+)\]"
        [orig code ids chksum] (re-find splitter1 l)
        id (parse-int ids)
        chars (apply str(split code #"-"))
        csum (calc_sum chars)
        ]
    (if (= csum chksum)
      id
      0)
    )
  )

(defn dosplit2 [l]
  (let [splitter1 #"([a-z\-]+)([0-9]+)\[([a-z]+)\]"
        [orig code ids chksum] (re-find splitter1 l)
        id (parse-int ids)
        chars (apply str(split code #"-"))
        csum (calc_sum chars)
        ]
    (if (= csum chksum)
      [id code (rotword code id)]
      [0 "" ""]
      )
    )
  )


(def roomnames(map dosplit2 rawdata))


(defn ftest [ [i c s]]
  (re-find #"obj" s)
  )


; answer for part 1
(apply + (map dosplit rawdata))

; for part 2
(filter ftest roomnames)

