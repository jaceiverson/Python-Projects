"""https://www.codewars.com/kata/59016379ee5456d8cc00000f"""
squirrel=lambda h,H,S:round((S**2+h**2)**.5*H/h,4)

"""
Using a^2 + b^2 = c^2 we can find the distance traveled for one spiral
(think of flattening the cylinder to a rectangle)

Then we multiply that by the total height/one rotation height to
find how many rotations to reach the top

Last we round our answer to 4 decimal places

One of the more enjoyable solutions I have found
"""