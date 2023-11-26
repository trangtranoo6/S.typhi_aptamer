import numpy as np

alpha_pool = np.array([*'ALRMKQEH'])
beta_pool = np.array([*'IVTFYNWCMLSQ'])
probs = np.array([[0.6,0.4], #P(a|a), P(b|a)
                [0.4, 0.6]]) #P(a|b), P(b|b)
peptide_length = 15
max_run_length = 4

def AlphaBeta(uniform=True, isalpha=0):
    if uniform:
        return 0 if np.random.rand() < 0.5 else 1
    return isalpha if np.random.rand() < probs[isalpha][isalpha] else 1-isalpha

def pickfrompool(isalpha = 0):
    return np.random.choice(alpha_pool if isalpha == 0 else beta_pool)

def _generate_sample(peptide_length):
    choose = AlphaBeta()
    current_state = pickfrompool(choose) 
    sample = [current_state]
    run_length = 0
    for i in range(1,peptide_length):
        next_choose = AlphaBeta(uniform = False, isalpha = choose)
        next_state = pickfrompool(next_choose)
        if next_state == current_state:
            run_length+=1
        else:
            run_length = 0
        if run_length > max_run_length:
            return _generate_sample() 
        sample.append(next_state)
        choose = next_choose
        current_state = next_state
    return ''.join(sample)

def generate_samples(number = 500, peptide_length = 15):
    return [_generate_sample(peptide_length) for i in range(number)]
