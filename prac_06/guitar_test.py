"""
Estimated Time: 10 Minutes
Actual Time: 4 minutes
"""

from guitar import Guitar

electric_guitar = Guitar("Electric Guitar", 2002, 2000)
print(f"{electric_guitar.name} get_age() - Expected 23. Got {electric_guitar.get_age()}")
print(f"{electric_guitar.name} is_vintage() - Expected False. Got {electric_guitar.is_vintage()}")