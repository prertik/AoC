(ns day2.solution
  (:require [clojure.java.io :as io]
            [clojure.edn :as edn]
            [clojure.string :as str]))

(def input
  (-> "day2.txt"
      io/resource io/file slurp
      (str/split #",")
      (->>
       (map edn/read-string)
       (into []))))

(defn execute [opcode position]
  (let [[code first second dest] (subvec opcode position (+ position 4))
        first (get opcode first)
        second (get opcode second)]
    (case code
      99 opcode
      1 (recur (assoc opcode dest (+ first second)) (+ position 4))
      2 (recur (assoc opcode dest (* first second)) (+ position 4)))))

(defn revert-to-early-stage [rule1 rule2]
  (-> input
      (assoc 1 rule1)
      (assoc 2 rule2)
      (execute 0)
      (get 0)))

(println "Part 1:" (revert-to-early-stage 12 2))

(println "Part 2:"
  (filter some? (for [noun (range (count input))
                      verb (range (count input))]
                  (try (if (= 19690720 (revert-to-early-stage noun verb))
                         (+ (* 100 noun) verb)
                         nil)
                       (catch Exception e
                         (str ""))))))
