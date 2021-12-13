from mlproject.distance import haversine

def test_distance():
    assert type(haversine(1.0,2.0,3.0, 4.0)) == float

# def test_distance():
#     assert type(haversine(lon1, lat1, lon2, lat2)) == float  
