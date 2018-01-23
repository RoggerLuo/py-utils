
def 求最大值(encoding1, repo, model):
    scores = [model.predict(encoding1, item['encoding']) for item in repo]
    ind = scores.index(max(scores))

    return repo[ind]['name'], scores[ind]

