import numpy as np
from collections import OrderedDict
#-----------
# YOUR CODE STARTS HERE ()
# NOTE! do not change anything out of this boundary
#-----------
class WeatherSimulation:
    def __init__(self, transition_probabilities, holding_times):
        self.transition_probabilities = transition_probabilities
        self.holding_times = holding_times
        self.currState = 'sunny'
        self.count = 1
        for key in self.transition_probabilities:
            sum_probabilities = sum(self.transition_probabilities[key].values())
            if sum_probabilities != 1:
                raise RuntimeError("f Sum of probabilities for {key} should be 1")
                
    def get_states(self):
        return list(self.holding_times.keys())
        
    def current_state(self):
        return self.currState
        
    def set_state(self, new_state):
        self.currState = new_state
        
    def current_state_remaining_hours(self):
        return self.holding_times[self.currState] - self.count
        
    def next_state(self):
        probs = list(self.transition_probabilities[self.currState].values())
        if self.current_state_remaining_hours() <= 0:
            out = np.random.choice(list(self.transition_probabilities[self.currState].keys()), 1, p=probs)[0]
            self.set_state(out)
            self.count = 1
        else:
            self.count += 1
        return
    
    def iterable(self):
        '''
            generator to yield the current state
        '''
        while True:
            self.next_state()
            yield current_state()
            
    def simulate(self, hours):
        percentages = {key: 0 for key in self.get_states()}
        percentages[self.currState] += 1
        for h in range(hours):
            self.next_state()
            percentages[self.currState] += 1
        percentages_list = list(percentages.values())
        final_list = [(i / hours) * 100 for i in percentages_list]
        return final_list
    
#-----------
# YOUR CODE ENDS HERE 
#-----------
def mlog(msg):
    # print(msg)
    pass
def check_formalities(transitions, holding_time):
    ITERATING_ROUNDS = 100
    try:
        weather_sim = WeatherSimulation(transitions, holding_time)
    except:
        mlog('ERROR! Error in create WeatherSimulation object.')
        mlog('NOK!')
    methods = ['get_states', 'set_state', 'current_state',  'current_state_remaining_days', 'next_state', 'iterable', 'simulate']
    if not all(map(lambda x: hasattr(weather_sim, x) and callable(getattr(weather_sim, x)), methods)):
        mlog('ERROR! Not all methods has been implemented.')
        mlog('NOK!')
    mlog('\nTesting iterating (for {} rounds):'.format(ITERATING_ROUNDS))
    try:
        sim_iter = weather_sim.iterable()
        for i in range(ITERATING_ROUNDS):
            mlog(next(sim_iter))
    except:
        mlog('ERROR! Problem in iterating!')
        mlog('NOK!')
def check_exception(wrong_transitions, holding_time):
    mlog('\nCheck exception handling')
    try:
        weather_sim = WeatherSimulation(wrong_transitions, holding_time)
    except RuntimeError as err:
        mlog('Exception raised (correctly) with details: {}'.format(err))
        result = True
    except:
        mlog('Exception raised but not with RuntimeError object')
        result = False
    else:
        result = False
    return result
def check_holding_times(transitions, holding_time):
    mlog('\nCheck holding times')
    NUM_CHANGES = 20
    weather_sim = WeatherSimulation(transitions, holding_time)
    for i in range(NUM_CHANGES):
        last_state = weather_sim.current_state()
        hd = holding_time[last_state]
        for j in range(hd):
            if weather_sim.current_state() != last_state:
                mlog('Error: State {} changed before holding time {} to {}!'.format(last_state, hd, weather_sim.current_state()))
                return False
            weather_sim.next_state()
    return True
def run_test(transitions, holding_time, avg, tolerance):
    STATES = ['sunny', 'cloudy', 'rainy', 'snowy']
    DAYS = 1000#1_000_000
    weather_sim = WeatherSimulation(transitions, holding_time)
    mlog('\nTesting simulation function for {} days:'.format(DAYS))
    freq = weather_sim.simulate(DAYS)
    mlog('Simulation resulted in {}'.format(list(zip(STATES,freq))))
    if round(np.sum(freq)) != 100:
        mlog('ERROR! Summarization percentages do not add up to 100.')
    diff = list(map(lambda x: np.round(abs(x[0]-x[1]),0), zip(freq,avg)))
    # print(diff)
    if any(list(map(lambda x: x[0]>x[1] , zip(diff,tolerance)))):
        mlog('Some of your results are out of the acceptable range.')
        mlog('Higher range: {}'.format(list(map(lambda x: round(x[0]+x[1],2), zip(avg,tolerance)))))
        mlog('Your result: {}'.format(freq))        
        mlog('Lower range: {}'.format(list(map(lambda x: round(x[0]-x[1],2), zip(avg,tolerance)))))
        return False
    else:
        mlog('Results are in the acceptable range.')
        mlog('Higher range: {}'.format(list(map(lambda x: round(x[0]+x[1],2), zip(avg,tolerance)))))
        mlog('Your result: {}'.format(freq))        
        mlog('Lower range: {}'.format(list(map(lambda x: round(x[0]-x[1],2), zip(avg,tolerance)))))
        return True
def avg_run_test(transitions, holding_time, avg, tolerance, n):
    # results = [bool(run_test(transitions, holding_time, avg, tolerance)) for _ in range(n)]
    # result_avg = sum(results)
    np.random.seed(0)
    result_avg = 0
    for i in range(n):
        if run_test(transitions, holding_time, avg, tolerance):
            result_avg+=1
    return result_avg
def run_all():
    # transitions = {
    #     'sunny':{'sunny':0.7, 'cloudy':0.3, 'rainy':0, 'snowy':0}, 
    #     'cloudy':{'sunny':0.5, 'cloudy': 0.3, 'rainy':0.15, 'snowy':0.05}, 
    #     'rainy':{'sunny':0.6, 'cloudy':0.2, 'rainy':0.15, 'snowy':0.05}, 
    #     'snowy':{'sunny':0.7, 'cloudy':0.1, 'rainy':0.05, 'snowy':0.15} 
    # }
    # Just for Python 3.5 compatibility
    transitions = OrderedDict([
    ('sunny', OrderedDict([('sunny', 0.7), ('cloudy', 0.3), ('rainy', 0), ('snowy', 0)])),
    ('cloudy', OrderedDict([('sunny', 0.5), ('cloudy', 0.3), ('rainy', 0.15), ('snowy', 0.05)])),
    ('rainy', OrderedDict([('sunny', 0.6), ('cloudy', 0.2), ('rainy', 0.15), ('snowy', 0.05)])),
    ('snowy', OrderedDict([('sunny', 0.7), ('cloudy', 0.1), ('rainy', 0.05), ('snowy', 0.15)]))
    ])
    # wrong_transitions = {
    #     'sunny':{'sunny':0.7, 'cloudy':0.3, 'rainy':0.1, 'snowy':0}, 
    #     'cloudy':{'sunny':0.5, 'cloudy': 0.3, 'rainy':0.15, 'snowy':0.05}, 
    #     'rainy':{'sunny':0.6, 'cloudy':0.2, 'rainy':0.15, 'snowy':0.05}, 
    #     'snowy':{'sunny':0.7, 'cloudy':0.1, 'rainy':0.05, 'snowy':0.15} 
    # }
    
    # Just for Python 3.5 compatibility
    wrong_transitions = OrderedDict([
            ('sunny', OrderedDict([('sunny', 0.7), ('cloudy', 0.3), ('rainy', 0.1), ('snowy', 0)])),
            ('cloudy', OrderedDict([('sunny', 0.5), ('cloudy', 0.3), ('rainy', 0.15), ('snowy', 0.05)])),
            ('rainy', OrderedDict([('sunny', 0.6), ('cloudy', 0.2), ('rainy', 0.15), ('snowy', 0.05)])),
            ('snowy', OrderedDict([('sunny', 0.7), ('cloudy', 0.1), ('rainy', 0.05), ('snowy', 0.15)]))
        ])
    
    
    
    # holding_time = {'sunny':1, 'cloudy':2, 'rainy':2, 'snowy':1}
    # Just for Python 3.5 compatibility
    holding_time = OrderedDict([
    ('sunny', 1),
    ('cloudy', 2),
    ('rainy', 2),
    ('snowy', 1)
    ])
    # avg = [47.4975, 43.332, 7.697, 1.4735]
    avg = [47.40, 43.25, 7.85, 1.5] #1e6
    # tolerance = [3.14, 2.38, 1.18, 0.47]
    tolerance  = [a * b for a, b in zip(avg, [0.5,0.5,1,1])] #more tolerant
    np.random.seed(0)
    check_formalities(transitions, holding_time)
    if not check_exception(wrong_transitions, holding_time):
        mlog("Exception handling did not work as instructed.")
        mlog('NOK!')
        print(0)
    elif not check_holding_times(transitions, holding_time):
        mlog("Probably a problem with holding times")
        mlog('NOK!')
        print(0)
    elif avg_run_test(transitions, holding_time, avg, tolerance, 10) < 5:
        mlog("\nCould not pass the calculation test")
        mlog('NOK!')
        print(0)
    else:
        print(1)
    # else:
        # mlog("Correct holding times")
    #     print(0)
a = int(input())
run_all()





# Testfall #	Input	Förväntad output
# 1	1	1
