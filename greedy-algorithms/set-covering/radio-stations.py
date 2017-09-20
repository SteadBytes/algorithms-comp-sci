# Starting a radio show.
# Need to reach listeners in all 50 states of America.
# Must decide which radio stations to play on to reach all states whilst
# minimising cost of paying to be on each station#
# i.e. minimise number of stations played on.
# uses a GREEDY APPROXIMATION ALGORITHM

states_needed = set(['mt', 'wa', 'or', 'id', 'nv', 'ut',
                     'ca', 'az'])
stations = {}
stations['kone'] = set(['id', 'nv', 'ut'])
stations['ktwo'] = set(['wa', 'id', 'mt'])
stations['kthree'] = set(['or', 'nv', 'ca'])
stations['kfour'] = set(['nv', 'ut'])
stations['kfive'] = set(['ca', 'az'])

final_stations = set()


while states_needed:
    best_station = None
    states_covered = set()
    for station, states_for_stations in stations.items():
        # Intersection = uncovered states that current station covers
        covered = states_needed & states_for_stations
        # compare current station cover to current best_station cover
        if len(covered) > len(states_covered):
            best_station = station
            states_covered = covered
    # update states still uncovered
    states_needed -= states_covered
    final_stations.add(best_station)

print(final_stations)
