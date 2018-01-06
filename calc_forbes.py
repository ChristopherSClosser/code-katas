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
    return{
        'youngest': youngest,
        'oldest': oldest
    }


if __name__ == '__main__':
    print(youngest_oldest(FORBES))
