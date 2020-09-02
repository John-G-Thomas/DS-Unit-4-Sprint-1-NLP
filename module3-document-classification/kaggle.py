import pandas as pd

files = [
    'data/submission1.csv',
    'data/submission2.csv',
    'data/submission3.csv',
    'data/submission4.csv',
    'data/submission5.csv',
    'data/submission6.csv',
    'data/submission7.csv',
    'data/submission8.csv',
    'data/submission9.csv',
]
submissions = (pd.read_csv(file)[['ratingCategory']] for file in files)
ensemble = pd.concat(submissions, axis='columns')
majority_vote = ensemble.mode(axis='columns')[0]

test = pd.read_csv("data/test.csv")
submissions = pd.DataFrame({'id': test['id'], 'ratingCategory': test['id']})
submissions['ratingCategory'] = majority_vote.astype('int64')

submissions.to_csv('submission-ultra.csv', index=False)
