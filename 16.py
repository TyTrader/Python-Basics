import geopy
from geopy.distance import geodesic as GD  

Nairobi= (1.2921, 36.8219)
Ksm = (0.0917, 34.7680)

print("The distance between Nairobi and Ksm is: ", GD(Nairobi, Ksm).km)