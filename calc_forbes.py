"""Forbes top 40."""

from forbes_listing import FORBES


def youngest_oldest(_dict):
    """Return youngest and oldest billionaires."""
    oldest = None
    youngest = float('inf')
    for person in _dict:
        if person['age'] < 80:
            if oldest is not None:
                if person['age'] > oldest['age']:
                    oldest = person
            else:
                oldest = person
        if youngest == float('inf'):
            youngest = person
        elif person['age'] < youngest['age'] and person['age'] > 0:
            youngest = person
    output = """
    The oldest billionaire under 80 is {0}.
    {0} is {1} years old and worth {2}.
    His industry is {3}.

    The youngest billionaire is {4}.
    {4} is {5} years old and worth {6}.
    His industry is {7}.
    """.format(
        oldest['name'],
        oldest['age'],
        oldest['net_worth (USD)'],
        oldest['source'],
        youngest['name'],
        youngest['age'],
        youngest['net_worth (USD)'],
        youngest['source']
    )
    # print(output)
    return{
        'youngest': youngest,
        'oldest': oldest
    }


if __name__ == '__main__':
    print(youngest_oldest(FORBES))
