def debug(text):
    res = text[:]
    bug_idx = [i for i in range(len(text)) if text.startswith('bug', i)]
    bugs_idx = text.find('bugs')
    # for 'bug' in text:
    #     bug_idx += 1
    # for 'bugs' in text:
    #     bugs_idx += 1
    if bug_idx and bugs_idx == -1:
        import pdb; pdb.set_trace()
        res = res.replace('bug', '')
        return res
    if bug_idx == -1:
        return res
    for char in res:
        if char == 'b':
            idx = res.index(char)
            if res[idx + 1] == 'u' and res[idx + 2] == 'g':
                if res[idx + 3] != 's':
                    res = res.replace('bug', '', 1)
            idx += 1
    return res


if __name__ == '__main__':
    print(debug('obbugubuggo'))
