(ns advent-of-code.day02
  (:require [clojure.java.io :as io]))

(defn read-and-parse-input []
  (with-open [f (io/reader "inputs/day02.txt")]
    (doall (line-seq f))))

(defn count-letter-in-string [string letter]
  (->>
   string
   (filter (fn [char] (= char letter)))
   count))

(defn policy1 [min-value max-value char password]
  (<= min-value (count-letter-in-string password char) max-value))

(defn policy2 [min-value max-value char password]
  (->>
   [min-value max-value]
   (filter (fn [value] (= (nth password (dec value) false) char)))
   count
   (= 1)))

(defn valid-pasword? [raw-password policy]
  (let [[ignore min-str max-str char password] (re-find #"(\d+)-(\d+) ([a-zA-Z]): (\w+)" raw-password)
        min-value (Integer/parseInt min-str)
        max-value (Integer/parseInt max-str)]
    (policy min-value max-value (first char) password)))

(defn solve [policy]
  (->>
   (read-and-parse-input)
   (filter (fn [password] (valid-pasword? password policy)))
   count))


;; answer 1


(println (solve policy1))

;; answer 2

(println (solve policy2))
