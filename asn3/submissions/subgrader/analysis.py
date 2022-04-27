# analysis.py
# -----------
# Licensing Information:  You are free to use or extend these projects for
# educational purposes provided that (1) you do not distribute or publish
# solutions, (2) you retain this notice, and (3) you provide clear
# attribution to UC Berkeley, including a link to http://ai.berkeley.edu.
# 
# Attribution Information: The Pacman AI projects were developed at UC Berkeley.
# The core projects and autograders were primarily created by John DeNero
# (denero@cs.berkeley.edu) and Dan Klein (klein@cs.berkeley.edu).
# Student side autograding was added by Brad Miller, Nick Hay, and
# Pieter Abbeel (pabbeel@cs.berkeley.edu).


######################
# ANALYSIS QUESTIONS #
######################

# Set the given parameters to obtain the specified policies through
# value iteration.

def question2():
    """
    python autograder.py -q q2
    python gridworld.py -a value -i 100 -g BridgeGrid --discount 0.9 --noise 0.2
    """
    answerDiscount = 0.9
    answerNoise = 0.01
    return answerDiscount, answerNoise


def question3a():
    """
    a. Prefer the close exit (+1), risking the cliff (-10)
    python autograder.py -q q3
    python gridworld.py -a value -i 100 -g DiscountGrid --discount 0.9 --noise 0.1 --livingReward -1
    """
    answerDiscount = 0.9
    answerNoise = 0.1
    answerLivingReward = -4
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3b():
    """
    b. Prefer the close exit (+1), but avoiding the cliff (-10)
    python autograder.py -q q3
    python gridworld.py -a value -i 100 -g DiscountGrid --discount 0.9 --noise 0.1 --livingReward -1
    """
    answerDiscount = 0.5
    answerNoise = 0.3
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3c():
    """
    c. Prefer the distant exit (+10), risking the cliff (-10)
    python autograder.py -q q3
    python gridworld.py -a value -i 100 -g DiscountGrid --discount 0.9 --noise 0.1 --livingReward -1
    """
    answerDiscount = 0.9
    answerNoise = 0.1
    answerLivingReward = -1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3d():
    """
    d. Prefer the distant exit (+10), avoiding the cliff (-10)
    python autograder.py -q q3
    python gridworld.py -a value -i 100 -g DiscountGrid --discount 0.9 --noise 0.1 --livingReward -1
    """
    answerDiscount = 0.9
    answerNoise = 0.1
    answerLivingReward = -0.1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question3e():
    """
    e. Avoid both exits and the cliff (so an episode should never terminate)
    python autograder.py -q q3
    python gridworld.py -a value -i 100 -g DiscountGrid --discount 0.9 --noise 0.1 --livingReward -1
    """
    answerDiscount = 0.9
    answerNoise = 0.1
    answerLivingReward = 1
    return answerDiscount, answerNoise, answerLivingReward
    # If not possible, return 'NOT POSSIBLE'


def question8():
    """
    python gridworld.py -a q -k 50 -n 0 -g BridgeGrid -e 1
    python autograder.py -q q8
    """
    answerEpsilon = 0.0
    answerLearningRate = 0.8
    # return answerEpsilon, answerLearningRate
    return 'NOT POSSIBLE'
    # If not possible, return 'NOT POSSIBLE'


if __name__ == '__main__':
    print('Answers to analysis questions:')
    import analysis

    for q in [q for q in dir(analysis) if q.startswith('question')]:
        response = getattr(analysis, q)()
        print('  Question %s:\t%s' % (q, str(response)))
