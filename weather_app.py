distance_mi = 7
is_raining = True
has_bike = True
has_car = False
has_ride_share_app = True


# If the distance is less than or equal to 1 mile:
# You should print True only if it is not raining.
# Otherwise, you should print False.

if distance_mi <= 0:
	print(False)


# If the distance is less than or equal to 1 mile:
# You should print True only if it is not raining.
# Otherwise, you should print False.

if distance_mi > 1 or distance_mi == 0:
	pass
elif distance_mi <= 1 and is_raining == False:
	print(True)
else:
	print(False)

# If the distance is greater than 1 mile and less than or equal to 6 miles:
# You should print True only if the person has a bike and it is not raining.
# Otherwise, you should print False.

if distance_mi > 1 and distance_mi <= 6:
	if has_bike and is_raining == False:
		print(True)
	else:
		print(False)
	

# If the distance is greater than 6 miles:
# You should print True if the person has a car or has a ride-share app.
# Otherwise, you should print False.


if distance_mi > 6 and (has_ride_share_app or has_car):
	print(True)
elif distance_mi < 6 or distance_mi == 6:
	pass
else:
	print(False)