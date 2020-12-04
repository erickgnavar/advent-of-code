(ns advent-of-code.day01)

(require '[clojure.java.io :as io])

(defn cart [colls]
  "Compute the cartesian product of list of lists"
  (if (empty? colls)
    '(())
    (for [more (cart (rest colls))
          x (first colls)]
      (cons x more))))

(defn read-and-parse-input []
  (with-open [f (io/reader "inputs/day01.txt")]
    (doall (map #(Integer/parseInt %) (line-seq f)))))

(defn find-two-values-which-sum-2020 [values]
  (let [cart-values (cart [values values])
        filtered-values (filter (fn [[a b]] (= 2020 (+ a b))) cart-values)
        [n1 n2] (first filtered-values)]
    (* n1 n2)))

(defn find-three-values-which-sum-2020 [values]
  (let [cart-values (cart [values values values])
        filtered-values (filter (fn [[a b c]] (= 2020 (+ a b c))) cart-values)
        [n1 n2 n3] (first filtered-values)]
    (* n1 n2 n3)))
;TODO: these two functions could be one if we generalize them and use apply to make the predicate and result calculation

;; answer 1
(println (find-two-values-which-sum-2020 (read-and-parse-input)))

;; answer 2
(println (find-three-values-which-sum-2020 (read-and-parse-input)))

