import HW8Classes as HW8Cls
import scr.StatisticalClasses as Stat
import scr.FormatFunctions as Format

#Parameters for the simulations below?
number_of_games_per_set = 1000
alpha = 0.05
number_of_sets_per_multiset = 10

#Question 1 (Steady state)
print('Question 1')

#Create a set of games with 50% heads
SS_50_SetofGames = HW8Cls.SetOfGames(
            id=1,
            prob_head=0.5,
            n_games=number_of_games_per_set)
SS_50_SetofGames.simulation()
SS_50_SetofGamesOutcomes = HW8Cls.SetOfGamesOutcomes(SS_50_SetofGames)

# average reward across all games
SS_50_SetofGamesOutcomes._sumStat_gameRewards.get_mean()
# CI of rewards from all games
SS_50_SetofGamesOutcomes._sumStat_gameRewards.get_t_CI(alpha)

print('Average return 50%', SS_50_SetofGamesOutcomes._sumStat_gameRewards.get_mean())
print('95% CI:', SS_50_SetofGamesOutcomes._sumStat_gameRewards.get_t_CI(alpha))

#Create a set of games with 45% heads
SS_45_SetofGames = HW8Cls.SetOfGames(
            id=1,
            prob_head=0.45,
            n_games=number_of_games_per_set)
SS_45_SetofGames.simulation()
SS_45_SetofGamesOutcomes = HW8Cls.SetOfGamesOutcomes(SS_45_SetofGames)

# average reward across all games
SS_45_SetofGamesOutcomes._sumStat_gameRewards.get_mean()
# CI of rewards from all games
SS_45_SetofGamesOutcomes._sumStat_gameRewards.get_t_CI(alpha)

print('Average return 45%', SS_45_SetofGamesOutcomes._sumStat_gameRewards.get_mean())
print('95% CI:', SS_45_SetofGamesOutcomes._sumStat_gameRewards.get_t_CI(alpha))

#Compare them
# increase in average return
increase = Stat.DifferenceStatIndp(
            name='Increase in average return for gambler',
            x=SS_45_SetofGamesOutcomes.get_rewards(),
            y_ref=SS_50_SetofGamesOutcomes.get_rewards())
# estimate and CI
estimate_CI = Format.format_estimate_interval(
            estimate=increase.get_mean(),
            interval=increase.get_t_CI(alpha=alpha),
            deci=1
        )
print("Average increase in average return ($) and {:.{prec}%} confidence interval:".format(1 - alpha, prec=0),
              estimate_CI)




print(' ')
print('Question 2')
#Question 2 (Transient state)
#Create MULTIPLE sets of games with 50% heads
TS_50_MultiSet = HW8Cls.MultipleGameSets(
    ids=range(number_of_sets_per_multiset),
    prob_head=0.5,
    n_games_in_a_set=number_of_sets_per_multiset
)
# simulate all cohorts
TS_50_MultiSet.simulation()

# get the mean of total rewards (after 10 games)
TS_50_MultiSet.get_mean_total_reward()
# get prediction interval for total reward
TS_50_MultiSet.get_PI_total_reward(alpha=alpha)

print('Expected return 50% after a set of 10 games', TS_50_MultiSet.get_mean_total_reward())
print('95% CI:', TS_50_MultiSet.get_PI_total_reward(alpha=alpha))

# get mean per game (after 10 games)
TS_50_Multiset_Average_reward = TS_50_MultiSet.get_mean_total_reward()/number_of_sets_per_multiset
#print('Average return PER GAME after 10 games with 50% prob heads',TS_50_Multiset_Average_reward)


#Create MULTIPLE sets of games with 45% heads
TS_45_MultiSet = HW8Cls.MultipleGameSets(
    ids=range(number_of_sets_per_multiset),
    prob_head=0.45,
    n_games_in_a_set=number_of_sets_per_multiset
)

# simulate all cohorts
TS_45_MultiSet.simulation()

# get the mean of total rewards
TS_45_MultiSet.get_mean_total_reward()
#divide by 1000 (number of games) to get the return PER GAME
TS_45_MultiSet_Average = TS_45_MultiSet.get_mean_total_reward()/number_of_sets_per_multiset
# get prediction interval for total reward
TS_45_MultiSet.get_PI_total_reward(alpha=alpha)

#create a list of all rewards
List_of_all_rewards_45 = TS_45_MultiSet.get_all_total_rewards

print('Expected return 45% after a set of 10 games', TS_45_MultiSet.get_mean_total_reward())
print('95% CI:', TS_45_MultiSet.get_PI_total_reward(alpha=alpha))

#Compare them
increase = Stat.DifferenceStatIndp(
            name='Increase in average return for gambler',
            x=TS_45_MultiSet.get_all_total_rewards(),
            y_ref=TS_50_MultiSet.get_all_total_rewards())
# estimate and CI
estimate_CI = Format.format_estimate_interval(
            estimate=increase.get_mean(),
            interval=increase.get_t_CI(alpha=alpha),
            deci=1
        )
print("Average increase in average return ($) and {:.{prec}%} confidence interval:".format(1 - alpha, prec=0),
              estimate_CI)



#REMEMBER: Rewards are reported for the player... The homework is asking about rewards for the owner in both states, so would need to adjust (negatives), assuming steady vs transient state are written as intended
