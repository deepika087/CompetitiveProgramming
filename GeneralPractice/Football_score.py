__author__ = 'deepika'
import copy

POINT_VALUES = [2, 3, 7]
def footballScores(score):
  # initialize the table with the ways to score 0 points
  T = { 0: [{}] }
  for k in range(1, score + 1):
      T[k] = []
      for value in POINT_VALUES:
          if k - value < 0 or k - value not in T:
              # if we can't fit this point value, skip it
              continue

          for score_config in T[k - value]:
              # for each score config in the previous total, append this value to it
              new_score_config = copy.copy(score_config)
              new_score_config[value] = new_score_config.get(value, 0) + 1

              if new_score_config not in T[k]:
                  # if we haven't already seen this config, add it
                  T[k].append(new_score_config)

  return T[score]

print footballScores(10) #How many ways can we form 10. Same as coin change problem