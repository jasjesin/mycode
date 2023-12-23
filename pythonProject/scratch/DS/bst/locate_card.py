list_cards1 = [9, 7, 6, 4, 2, 1]
list_cards2 = [9]
list_cards3 = []
list_cards4 = [9, 4, 1, 0, -2, -7]

cards_range = [list_cards1, list_cards2, list_cards3, list_cards4]


def check_location(cards, query, mid):
    mid_number = cards[mid]
    if mid_number == query:
        if (mid-1) >= 0 and cards[mid-1] == query:
            return 'left'
        else:
            return 'found'
    elif mid_number < query:
        return 'right'
    elif mid_number > query:
        return 'left'


def locate_card(cards, query):
    lo = 0
    hi = len(cards) - 1
    print("\nList Content: ")
    [[print(x, end=' ') for x in cards]]
    print("\n")
    while lo <= hi:
        mid = (lo + hi) // 2
        mid_number = cards[mid]
        print(f"lo: {lo}, mid: {mid}, hi: {hi}, mid number: {mid_number}")
        result = check_location(cards, query, mid)
        if result == 'found':
            return f'{query} is located 1st time at position {mid}'
        elif result == 'left':
            hi = mid - 1
        elif result == 'right':
            lo = mid + 1

    print(f"\n{query} is not present in current list")



print("Sorted lists with Binary Tree Search:")
for y in cards_range:
    print(sorted(int(x) for x in y))
    y = sorted(int(x) for x in y)
    print(locate_card(y, query=4))
"""
list_sorted = sorted(int(x) for x in list_cards1)
print(list_sorted)
print(locate_card(list_sorted, query=4))
"""
"""
    mid = (lo + hi) // 2
    mid_number = cards[mid]
    print(f"\nBefore 1st iteration\nlo: {lo}, hi: {hi}, mid: {mid}, mid number: {mid_number}, query: {query}")
    if mid_number == query:
        return f"{query} is located at {mid} position"
    elif mid_number < query:
        print("\nam less")
        hi = mid - 1
    elif mid_number > query:
        print("\nam more")
        lo = mid + 1
    print(f"\nAfter 1st iteration\nlo: {lo}, hi: {hi}, mid: {mid}, mid number: {mid_number}, query: {query}")
    mid = (lo + hi) // 2
    mid_number = cards[mid]
    print(f"\nBefore 2nd iteration\nlo: {lo}, hi: {hi}, mid: {mid}, mid number: {mid_number}, query: {query}")
    if mid_number == query:
        return f"{query} is located at {mid} position"
    elif mid_number < query:
        print("\nam less")
        hi = mid - 1
    elif mid_number > query:
        print("\nam more")
        lo = mid + 1
    print(f"\nAfter 2nd iteration\nlo: {lo}, hi: {hi}, mid: {mid}, mid number: {mid_number}, query: {query}")
    mid = (lo + hi) // 2
    mid_number = cards[mid]
    print(f"\nBefore 3rd iteration\nlo: {lo}, hi: {hi}, mid: {mid}, mid number: {mid_number}, query: {query}")
    if mid_number == query:
        return f"{query} is located at position number {mid}"
    elif mid_number < query:
        print("\nam less")
        hi = mid - 1
    elif mid_number > query:
        print("\nam more")
        lo = mid + 1
    print(f"\nAfter 3rd iteration\nlo: {lo}, hi: {hi}, mid: {mid}, mid number: {mid_number}, query: {query}")
    [[print(x, end=' ') for x in cards]]
"""
